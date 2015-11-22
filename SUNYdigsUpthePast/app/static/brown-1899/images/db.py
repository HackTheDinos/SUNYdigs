from pymongo import MongoClient
from bson.json_util import dumps
import json

'''
This python file is built to insert elements from the data structure containing all the paths
and metadata related to the palentology journal entry. 

Data Structure Design:

d = {"author":"brown",
     "bookyr":"1999",
     "imgpage":"stuff",
     "word": [ ["path to the first word", "translation_text", 0],
               ]
     }
'''
# Note the default null symbol for the translation text is: !@#$%
# Value

conn = MongoClient()



############ This section is for populating words ##################
db = conn['word_images']
#print db.collections_names()


with open('../raw_home.json','r') as data_file:
    home = json.load(data_file)
    
    for i in xrange(len(home)):
        
        db.word_images.insert(i)

    print db.word_images.find()
#CREATE d for every image - this may involve some reading into file system stuff -  somehow :S

''''
d = {"author":"yum",
     "bookyr":"1999",
     "imgpage":"stuff",
     "word": [ ["path to the first word", "translation_text", 0],
               ]
     }
#db.word_images.insert(d)

x = db.word_images.find({"author":"yum"})
print x
print dumps(x)
''''
