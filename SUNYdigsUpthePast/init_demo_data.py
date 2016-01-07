from pymongo import MongoClient
from bson.json_util import dumps


#add data for demo

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

addTest(d)
