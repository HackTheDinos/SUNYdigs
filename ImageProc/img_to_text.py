"""
smritijha
Text-based image segmentation
"""

import cv2
import os
from matplotlib import pyplot as plt
import numpy as np
import re
import json
import string

rootdir = '/Users/smritijha/AMNH/demo/'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if not file.endswith('.txt'):
            if not file.startswith('.'):
                #print file
                img_file = os.path.join(subdir, file)

                image = cv2.imread(img_file)
                gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # grayscale
                img = cv2.medianBlur(gray,5)

                th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)

                #kernel
                kernel = np.ones((2,2),np.uint8)

                #noise removal  
                #-------------------
                opening = cv2.morphologyEx(th3,cv2.MORPH_OPEN,kernel, iterations = 1)
                #-------------------

                morphKernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))

                #dilate to get connected components
                dilation = cv2.dilate(opening,morphKernel,iterations = 3)

                contours,hierarchy = cv2.findContours(dilation,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)



                #write words to image directory
                #create a directory with image name as folder name
                path = os.path.join(subdir, os.path.splitext(file)[0])

                #print path

                #check if we are in the /images directory or not
                curr_dir = os.path.split(os.path.realpath(subdir))[1]
                #print curr_dir

                working_dir = str(os.getcwd())
                
                #if directory already exists no need to extract images
                #if any other directiry than images no extraction should be carried out
                #this is for the case when we have already extracted words as image files
                #and we don't want the word-image files to get segmented
                if not os.path.isdir(path) and curr_dir == 'images':
                    os.makedirs(path)
                
                    #parse enclosing journal folder
                    author_year = os.path.split(os.path.dirname(os.path.dirname(path)))[1]
                    author_year = re.split(r'\s|-', author_year)
                    author = author_year[0]
                    year = author_year[1]

                    count = 0
                    data = {}
                    json_list = []
                    
                    for contour in contours:
                            # get rectangle bounding contour
                            [x,y,w,h] = cv2.boundingRect(contour)
    
                             # discard areas that are too large
                            if h>30:
                                continue
    
                            # discard areas that are too small
                            if h<10 or w<20:
                                continue
    
                             # draw rectangle around contour on original image
                            cv2.rectangle(gray,(x,y),(x+w,y+h),(100,0,100),1)

                            #save filename as a counter
                            count = count + 1
                            filenum = "{0:0>3}".format(count) #format for filename counter 
                            #print filenum
    
                            filename = str(filenum)+'.png' 
                            fullpath = os.path.join(path, filename) 

                            # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
                            crop_img = image[y:y+h, x:x+w]
                            cv2.imwrite(fullpath, crop_img)  

                            parent_img = str(subdir)
                            word_path = str(path)            
                            
                            parent_img = string.replace(parent_img, working_dir, '.')
                            word_path = string.replace(word_path, working_dir, '.')

                            #create a json object for the corresponding 
                            data['author'] = author
                            data['year'] = year
                            data['img_page'] = parent_img
                            data['word'] = [word_path, "!@#$%",0]

                            json_list.append(data)

                    #dump the list of json objects in 
                    jsondata = os.path.join(subdir, 'jsondata.txt')

                    with open(jsondata, 'w') as f:
                        json.dump(json_list, f, ensure_ascii=False)


print '-*-end scene-*-'
