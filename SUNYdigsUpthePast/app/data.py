from pymongo import MongoClient
from bson.json_util import dumps


conn = MongoClient()


db = conn['word_images']


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


def addTest(L):
    for i in L:
        d = {"author":i[0],
             "bookyr":i[1],
             "imgpage":"/static/"+i[0]+"-"+i[1]+"/"+i[2],
             "word":[ "/static/" + i[0]+"-"+i[1]+"/"+i[3],
                    "translated",
                    i]
        }
        db.word_images.insert(d)

def clearALL():
    db.word_images.remove()
    db.validated.remove()
<<<<<<< HEAD


=======
>>>>>>> c5b3ad4a5eb89798b2666025a44fbccb9c2ebf4b
clearALL()
addTest(d)

        
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



def updateElement(id, increment):
    L = getOrderedElements()
    new_value = L[id]["word"][2]
    print new_value
    orig = L[id]
    print orig
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
    print db.word_images.find({"_id":key})
    pass



def insertGood(item):
    db2 = conn["validated"]
    #print item
    #db2.validated.remove()
    db2.validated.insert(item)
    db.word_images.remove({"_id":item["_id"]})
    db.word_images.find()
    #print db2.validated.find({"_id":item["_id"]})
    # remove from old database
    
    
