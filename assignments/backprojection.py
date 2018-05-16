import cv2
import numpy as np
import random as rn


img = cv2.imread("./images/square.jpg",0);

v_sum = np.sum(img,axis=0);