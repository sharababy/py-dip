import cv2
import numpy as np

'''
Question 2:
Implement back projection algorithm.
You can consider row-wise, column-wise and 2 diagonal projections as the input. 
'''

img = cv2.imread("./images/square.jpg",0);

bp_img = np.zeros((img.shape[0],img.shape[1],1),np.float32)
nimg = np.zeros((img.shape[0],img.shape[1],1),np.uint8)

v_sum = np.sum(img,axis=0);
h_sum = np.sum(img,axis=1);

d1_sum = [np.sum(np.diagonal(img,offset)) for offset in range(-1*(img.shape[0] -1),img.shape[1])]

d2_sum = [np.sum(np.diagonal(img[:,::-1],offset)) for offset in range((img.shape[0] -1),-1*img.shape[1],-1)]


norm_v_sum = np.zeros(v_sum.shape,np.uint8)
norm_s_sum = np.zeros(v_sum.shape,np.uint8)

for x in range(0,img.shape[0]):
	for y in range(0,img.shape[1]):
		bp_img[x,y] = v_sum[y];

for x in range(0,img.shape[0]):
	for y in range(0,img.shape[1]):
		bp_img[x,y] += h_sum[x];


n = img.shape[0];

for z in range(0,(img.shape[0]-1)+img.shape[1]):
	for x in range(1,img.shape[0]+1):
		for y in range(0,img.shape[1]):
			
			_x = n-x;
			if _x-y == n-z:
				# print(_x,y)
				bp_img[_x,y] += d1_sum[z]
				

for z in range(0,(img.shape[0]-1)+img.shape[1]):
	for x in range(0,img.shape[0]):
		for y in range(0,img.shape[1]):
			
			if x+y == z:
				# print(_x,y)
				bp_img[x,y] += d2_sum[z]
		


for x in range(0,img.shape[0]):
	for y in range(0,img.shape[1]):
		nimg[x,y] = np.uint8(bp_img[x,y]/255);


cv2.imshow('Original Image',img)
cv2.moveWindow("Original Image",400,0);
cv2.imshow('After back projection ',nimg)
cv2.waitKey(0)
cv2.destroyAllWindows()