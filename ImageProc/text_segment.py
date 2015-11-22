"""
Text-based image segmentation
"""

import cv2
import os
from matplotlib import pyplot as plt
import numpy as np

#for filename in os.listdir(""):

image = cv2.imread("/Users/smritijha/amnh/06.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # grayscale
img = cv2.medianBlur(gray,5)

#cv2.imshow('gray_image',gray)

#th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

ret,th1 = cv2.threshold(gray,200,255,cv2.THRESH_BINARY_INV)

th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)

#kernel
kernel = np.ones((2,2),np.uint8)

#noise removal
#-------------------
opening = cv2.morphologyEx(th3,cv2.MORPH_OPEN,kernel, iterations = 1)
#--------------------

morphKernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))

#dilate to get connected components
dilation = cv2.dilate(opening,morphKernel,iterations = 3)

contours,hierarchy = cv2.findContours(dilation,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


#write words to image directory
words_dir = '/Users/smritijha/amnh/img_dir'
count = 0


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
    fullpath = os.path.join(words_dir, filename) 

    # NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
    crop_img = image[y:y+h, x:x+w]
    cv2.imwrite(fullpath, crop_img)


#cv2.imshow('detection_img',gray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


titles = ['Original Image', 'Global Thresholding (v = 180)', 'th3', 'dilated']
images = [gray, th1, th3, dilation]

for i in xrange(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
