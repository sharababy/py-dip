import cv2
import numpy as np
import math
from random import *


def project(img,angle):
    
    if angle in [0,180]:
        return np.sum(img,axis=1)
    elif angle in [90,270]:
        return np.sum(img,axis=0)
    elif angle in [45,225]:
        return [ np.sum(np.diagonal(img,offset)) for offset in range(-1*(img.shape[0] -1),img.shape[1])]
    elif angle in [135,315]:
        return [ np.sum(np.diagonal(img[:,::-1],offset)) for offset in range((img.shape[0] -1),-1*img.shape[1],-1)]



def back_projection(img,projections,angle):
    if angle in [0,180]:
        for i in range(img.shape[0]):
            img[i,:] = img[i,:] + projections[i]

    elif angle in [90,270]:
        for i in range(img.shape[1]):
            img[:,i] = img[:,i] + projections[i]
    
    elif angle in [45,225]:
        p = 0
        # filling lower triangle including diagonal
        temp_img = np.zeros(img.shape,np.uint8)
        for offset in range(temp_img.shape[0]-1,-1,-1): 
            np.fill_diagonal(temp_img[offset:],projections[p])
            p = p + 1

        # filling upper triagle
        for offset in range(1,temp_img.shape[1]):
            np.fill_diagonal(temp_img[:,offset:],projections[p])
            p = p + 1
        
        img = img + temp_img

    elif angle in [135,315]:       
        p = 0
        temp_img = np.zeros(img.shape,np.uint8)

        # filling upper left triagle including anti-diagonal
        for offset in range(temp_img.shape[1]):
            np.fill_diagonal(temp_img[:,offset::-1],projections[p])
            p = p + 1
        
        # filling lower right triangle 
        for offset in range(1,temp_img.shape[0]): 
            np.fill_diagonal(temp_img[offset:,::-1],projections[p])
            p = p + 1
        
        img = img + temp_img

    return img
        


import itertools

def powerset(L):
  pset = set()
  for n in range(len(L) + 1):
    for sset in itertools.combinations(L, n):
      pset.add(sset)
  return pset





def process(dir,img,angles):
    if not angles:
        new_img = img
    else:
        new_img = np.zeros(img.shape,np.uint8)

    name = 'bp_'
    for angle in angles:
        new_img = back_projection(new_img,project(img,angle),angle=angle)
        name = name + ' -- '+str(angle)
   
    name = name + '.jpg'
    normalizedImg = np.zeros(new_img.shape,np.uint8)
    normalizedImg = cv2.normalize(new_img,  normalizedImg, 0, 255, cv2.NORM_MINMAX)
    
    cv2.imwrite(dir+name,normalizedImg)
    cv2.imshow('After back projection ',normalizedImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



        
        

image_name = './images/square.jpg'
img = cv2.imread(image_name,0)


dir = './output/a6/'

img_dir = dir + image_name + '/'

import os
if not os.path.exists(img_dir):
    os.makedirs(img_dir)

process(img_dir,img,[])
for angles in powerset([0,90,45,135]):
    process(img_dir,img,angles)


