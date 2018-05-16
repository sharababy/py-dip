import cv2
import numpy as np
import math

print("-- Scaling an Image -- ")

img 	= cv2.imread("lena.jpg",0)

height 	= img.shape[0]
width 	= img.shape[1]

rotated = np.zeros(( height, width ,3), np.uint8)

# _x = xcos(a) - ysin(a) - height/2
# _y = xsin(a) + ycos(a) - width/2

ang = 0.23

for x in range(0,height):
	for y in range(0,width):
		ax = ((x- (height/2))*math.cos(ang)) - ((y- (width/2))*math.sin(ang)) + (height/2)
		ay = ((x- (height/2))*math.sin(ang)) + ((y- (width/2))*math.cos(ang)) + (width/2)

		if ( (ax < 512 and ax > 0) and (ay < 512 and ay > 0) ):
			rotated[x,y] = img[int(ax),int(ay)]


cv2.imshow("Original",img)
cv2.moveWindow("Original", 800,0);

cv2.imshow("Rotation",rotated)
cv2.moveWindow("Rotation",0,0);

cv2.waitKey(0)
cv2.destroyAllWindows()
