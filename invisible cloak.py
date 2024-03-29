#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torchvision
import time
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from PIL import Image


# In[2]:


capture_video = cv2.VideoCapture("Vedio.mp4") 


# In[3]:


time.sleep(1)  
count = 0 
background = 0


# In[4]:


for i in range(60): 
    return_val, background = capture_video.read() 
    if return_val == False : 
        continue


# In[5]:


background = np.flip(background, axis = 1)


# In[6]:


while (capture_video.isOpened()): 
    return_val, img = capture_video.read() 
    if not return_val : 
        break 
    count = count + 1
    img = np.flip(img, axis = 1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,120,70])        
    upper_red = np.array([10,255,255]) 
    mask1 = cv2.inRange(hsv, lower_red, upper_red) 
 
    lower_red = np.array([170,120,70]) 
    upper_red = np.array([180,255,255]) 
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    mask1 = mask1 + mask2 
  
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3),np.uint8), iterations = 2) 
    mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations = 1) 
    mask2 = cv2.bitwise_not(mask1)

    res1 = cv2.bitwise_and(background, background, mask = mask1) 
    res2 = cv2.bitwise_and(img, img, mask = mask2) 
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0) 
  
    cv2.imshow("MASQUERADE", final_output) 
    k = cv2.waitKey(10) 
    if k == 27: 
        break


# In[ ]:




