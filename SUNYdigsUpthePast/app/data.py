from pymongo import MongoClient
from bson.json_util import dumps


conn = MongoClient()


db = conn['word_images']


'''
d = [
["brown","1899","images/06.jpg","images/06/059.png"],
["brown","1899","images/06.jpg","images/06/060.png"],
["brown","1899","images/06.jpg","images/06/064.png"],
["brown","1899","images/06.jpg","images/06/065.png"],
["brown","1899","images/06.jpg","images/06/083.png"],
["brown","1899","images/06.jpg","images/06/090.png"],
["brown","1899","images/06.jpg","images/06/091.png"],

["brown","1899","images/06.jpg","images/06/006.png"],
["brown","1899","images/06.jpg","images/06/008.png"],
["brown","1899","images/06.jpg","images/06/010.png"],
["brown","1899","images/06.jpg","images/06/011.png"],
["brown","1899","images/06.jpg","images/06/012.png"],
["brown","1899","images/06.jpg","images/06/013.png"],
["brown","1899","images/06.jpg","images/06/017.png"],
["brown","1899","images/06.jpg","images/06/018.png"],
["brown","1899","images/06.jpg","images/06/022.png"],
]

#MOVED TO ../init_demo_data.py
def clearALL():
    db.word_images.remove()
    db.validated.remove()

def addTest(L):
    clearALL()
    for i in L:
        d = {"author":i[0],
             "bookyr":i[1],
             "imgpage":"/static/"+i[0]+"-"+i[1]+"/"+i[2],
             "word":[ "/static/" + i[0]+"-"+i[1]+"/"+i[3],
                     "translated",
                     0]
             }
        db.word_images.insert(d)
    print "ADDED demo data"

#addTest(d)

'''

# Every element of crowsource value above and equal to THRESHOLD is deemed okay and moved to another database         

# Get ordered elements from word_image database (positive to zeros to negatives) 
def getOrderedElements():
    x = db.word_images.find()
    results = list(x)
    positives = []
    negatives = []
    zeros = []
    
    for img in results:
        print img
        author = img["author"] 
        bookyr = img["bookyr"]
        imgpage_url = img["imgpage"]
        wordimg_url = img["word"][0]
        translation = img["word"][1]
        if translation != "!@#$%":
            value = img["word"][2]
            if value > 0:
                positives.append(img)
            elif value < 0:
                negatives.append(img)
            else:
                zeros.append(img)
    print "\n\n"
    positives = sorted(positives,key=lambda x: x["word"][2], reverse=True)
    negatives = sorted(negatives,key=lambda x: x["word"][2], reverse=True)
    return positives + negatives + zeros


#updates Element and checks to see if THRESHOLD is met
# if so, removed from word_image db and moved to the "validated" collection
def updateElement(id, increment):
    L = getOrderedElements()
    new_value = L[id]["word"][2]
    orig = L[id]
    new_value += increment
    update = L[id]["word"]
    if new_value >= 5:
        #pass into good database
        L[id]["word"][2] = new_value
        insertGood(L[id])
    else:
        update[2] = new_value
    key = L[id]["_id"]
    db.word_images.update_one({"_id":key},{"$set":{"word":update}})
    print getOrderedElements()
    if new_value >=5:
        return False
    return True

#removes element from "word_images" and inserts validated element into the "validated" collection
def insertGood(item):
    # add to validated collection
    db2 = conn["validated"]
    db2.validated.insert(item)
    # remove from old collection
    db.word_images.remove({"_id":item["_id"]})
    db.word_images.find()
    #print db2.validated.find({"_id":item["_id"]})
   
# count of current word_images collection    
def dbcount():
    i = 0
    db_data = list(db.word_images.find())
    for img in db_data:
        #double check to see if it is in the list
        if img["word"][2] < 5:
            i+=1
    return i
