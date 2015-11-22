"""
Text-based image segmentation
"""

import cv2
import os
from matplotlib import pyplot as plt
import numpy as np


#data_dir =

#for filename in os.listdir(""):

image = cv2.imread("/Users/smritijha/amnh/printed_text.png")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # grayscale
img = cv2.medianBlur(gray,5)

#cv2.imshow('gray_image',gray)


#th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)


ret,th1 = cv2.threshold(gray,170,255,cv2.THRESH_BINARY)



th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,11,2)

#kernel
kernel = np.ones((2,2),np.uint8)

#noise removal
#-------------------
opening = cv2.morphologyEx(th3,cv2.MORPH_OPEN,kernel, iterations = 2)
#--------------------


#dilate to get connected components
dilation = cv2.dilate(opening,kernel,iterations = 5)


#cv2.imshow('gray_image',gray)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
'''
contours,hierarchy = cv2.findContours(dilation,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print contours

for contour in contours:
    # get rectangle bounding contour
    [x,y,w,h] = cv2.boundingRect(contour)

    # discard areas that are too large
    if h>300 and w>300:
        continue

    # discard areas that are too small
    if h<40 or w<40:
        continue

    # draw rectangle around contour on original image
    cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,255),2)
'''

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

'''
_,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV) # threshold
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
dilated = cv2.dilate(thresh,kernel,iterations = 13) # dilate
contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) # get contours



for contour in contours:
    # get rectangle bounding contour
    [x,y,w,h] = cv2.boundingRect(contour)

    # discard areas that are too large
    if h>300 and w>300:
        continue

    # discard areas that are too small
    if h<40 or w<40:
        continue

    # draw rectangle around contour on original image
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,255),2)

'''# for each contour found, draw a rectangle around it on original image

# write original image with added contours to disk
#cv2.imwrite("/Users/smritijha/amnh/contoured.jpg", image)
