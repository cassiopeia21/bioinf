#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import argparse


# In[5]:


parser = argparse.ArgumentParser(prog = 'edit picture',
                                description = 'make your picture great again!',
                                epilog = 'Enjou you picture!')


# In[6]:


parser.add_argument('-i', '--input_name', required = True, type = str,
                   metavar = 'name of picture', help = 'keep calm and give a name of your picture')


# In[ ]:


args = parser.parse_args()


# In[13]:


args = args.__dict__


# In[115]:


img = cv2.imread('cat.jpg')


# #### Make filters

# In[84]:


kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)


# In[85]:


figure(num=None, figsize=(10, 8), dpi=80, edgecolor='k')
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(erosion),plt.title('Erosion')
plt.xticks([]), plt.yticks([])
plt.show()


# In[90]:


dilation = cv2.dilate(img,kernel,iterations = 2)


# In[91]:


figure(num=None, figsize=(10, 8), dpi=80, edgecolor='k')
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dilation),plt.title('Dilation')
plt.xticks([]), plt.yticks([])
plt.show()


# In[98]:


opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)


# In[99]:


figure(num=None, figsize=(10, 8), dpi=80, edgecolor='k')
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(opening),plt.title('Opening')
plt.xticks([]), plt.yticks([])
plt.show()


# In[100]:


closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)


# In[101]:


figure(num=None, figsize=(10, 8), dpi=80, edgecolor='k')
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(closing),plt.title('Closing')
plt.xticks([]), plt.yticks([])
plt.show()


# In[102]:


gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)


# In[103]:


figure(num=None, figsize=(10, 8), dpi=80, edgecolor='k')
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(gradient),plt.title('Gradient')
plt.xticks([]), plt.yticks([])
plt.show()


# In[108]:


tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)


# In[109]:


figure(num=None, figsize=(10, 8), dpi=80, edgecolor='k')
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(tophat),plt.title('Top Hat')
plt.xticks([]), plt.yticks([])
plt.show()


# #### Smoothing Images 

# In[36]:


blur = cv2.blur(img,(5,5))


# In[37]:


figure(num=None, figsize=(10, 8), dpi=80, edgecolor='k')
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()


# In[86]:


blur1 = cv2.GaussianBlur(img,(3,3),0)


# In[87]:


figure(num=None, figsize=(10, 8), dpi=80, edgecolor='k')
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur1),plt.title('Gaussian Blur')
plt.xticks([]), plt.yticks([])
plt.show()


# In[79]:


median = cv2.medianBlur(img,5)


# In[80]:


figure(num=None, figsize=(10, 8), dpi=80, edgecolor='k')
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('Median Filtering')
plt.xticks([]), plt.yticks([])
plt.show()


# In[82]:


blur2 = cv2.bilateralFilter(img,9,75,75)


# In[83]:


figure(num=None, figsize=(10, 8), dpi=80, edgecolor='k')
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur2),plt.title('Bilateral Filtering')
plt.xticks([]), plt.yticks([])
plt.show()


# #### Download new image

# In[19]:


img = cv2.imread('opencv-logo-white.png',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)


# In[21]:


circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    c = cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)


# In[22]:


figure(num=None, figsize=(10, 8), dpi=80, edgecolor='k')
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(c),plt.title('Circles')
plt.xticks([]), plt.yticks([])
plt.show()


# #### One more picture

# In[101]:


img = cv2.imread('space.png',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,35,10,
                            param1=30,param2=20,minRadius=5,maxRadius=150)


# In[102]:


circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    c = cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)


# In[103]:


figure(num=None, figsize=(10, 8), dpi=80, edgecolor='k')
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(c),plt.title('Circles')
plt.xticks([]), plt.yticks([])
plt.show()

