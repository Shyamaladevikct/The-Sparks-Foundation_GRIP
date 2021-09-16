#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip3 install opencv-python')
import numpy as np
import cv2


# In[2]:


body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')


# In[3]:


image = cv2.imread('beach_crop1.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('img',image)
cv2.waitKey(0)


# In[4]:


bodies = body_classifier.detectMultiScale(gray,1.05,10)
print(bodies)


# In[5]:


l=[]
i=1
lf=[]
for (x,y,w,h) in bodies:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
    s=str(i)
    cv2.putText(image,s,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    i+=1
    l=[]
    l.append(x)
    l.append(y)
    lf.append(l)
    print(l)
print(lf)


# In[6]:


close_persons=""
import math
for i in range(len(lf)):
    print(lf[i])
    for j in range(i+1,len(lf)):
        print(lf[j])
        d=math.sqrt(((lf[j][1]-lf[i][1])**2)+(lf[j][0]-lf[i][0])**2)
        print("P"+str(i+1)+" - "+"P"+str(j+1)+" = "+str(d))
    
        if d<72.5:
            close_persons+="Person"+str(i+1)+" and Person"+str(j+1)+"; "
            cv2.line(image,(lf[i][0],lf[i][1]),(lf[j][0],lf[j][1]),(255,0,0),2)

close_persons+=" are not following social distancing"
print(close_persons)


# In[7]:


cv2.imshow('Distance',image)
cv2.waitKey(0)


# In[ ]:





# In[ ]:




