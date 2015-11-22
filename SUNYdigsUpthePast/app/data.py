from pymongo import MongoClient
from bson.json_util import dumps


conn = MongoClient()


db = conn['word_images']

def addTest():
    i = 7
    
    while i > -4:
        d = {"author":"a"+str(i),
             "bookyr":"by"+str(i),
             "imgpage":"img"+str(i),
             "word":[str(i) + "lkasdjfa",
                     "translated.....",
                     i]
             }
        #db.word_images.insert(d)
        i-=1

        
def getOrderedElements():
    x = db.word_images.find()
    results = list(x)
    #print x
    #print results
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
    


    positives = sorted(positives,key=lambda x: x["word"][2], reverse=True)
    negatives = sorted(negatives,key=lambda x: x["word"][2], reverse=True)
    return positives + negatives + zeros
