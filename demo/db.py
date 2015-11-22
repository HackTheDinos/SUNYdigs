from pymongo import MongoClient
from bson.json_util import dumps
import json

s = '''
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

fname = 'brown-1899/images/jsondata.txt'
def insert(fname):
    with open(fname,'r') as data_file:
        home = json.load(data_file)
        print home
        
        for i in xrange(len(home)):
            print home[i]
        #db.word_images.insert(i)
            db.word_images.remove()
   #         print db.word_images.find()
#CREATE d for every image - this may involve some reading into file system stuff -  somehow :S

insert('brown-1899/images/jsondata.txt')

'''
insert('brown-1903/images/jsondata.txt')
insert('brown-1908/images/jsondata.txt')
'''

# "brown-1899/images/"
def openText (file):
    i = 0
    L = []
    filename = file + str(0) + str(i) 
    '''
    while f = open(filename,"r"):
        results = f.read()
        print results.split()
        for x in results:
            L.append(x)
        
        print L
        exit(0)
        if i < 10:
            filename = file + str(0) + str(i) 
'''

