import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread(r'temp.jpg',0)
#cv2.imshow('image',img)
canny=cv2.Canny(img,100,200)
_,th1=cv2.threshold(canny,225,255,cv2.THRESH_BINARY)
kernal=np.ones((2,2),np.uint8)
th2=cv2.dilate(th1,kernal)
#cv2.imshow('th1',th1)
titles=['img','canny']
#cv2.imshow('th2',th2)
images=[img,canny]
for i in range(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
