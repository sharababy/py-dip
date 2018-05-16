import cv2
import numpy as np

print("-- Scaling an Image -- ")

img 	= cv2.imread("lena.jpg",0)

height 	= img.shape[0]
width 	= img.shape[1]

scaledd2 = np.zeros(( int(height/2), int(width/2) ,3), np.uint8)
scaledu2 = np.zeros(( int(height*2), int(width*2) ,3), np.uint8)

for x in range(0,int(height/2)):
	for y in range(0,int(width/2)):

		ax = x*2
		ay = y*2

		if ax > 512 :
			ax = 511

		if ay > 512 :
			ay = 511

		a = ((img[ax-1,ay])/5)
		b = ((img[ax,ay-1])/5)
		c = ((img[ax+1,ay])/5)
		d = ((img[ax,ay+1])/5)
		e = ((img[ax,ay])/5)
		avgsum = a + b + c + d + e
		scaledd2[x,y] = int(avgsum)

for x in range(0,int(height*2)):
	for y in range(0,int(width*2)):

		ax = 0
		ay = 0
		if int(x/2) < 511 :
			ax = int(x/2)
		else:
			ax = int(x/2)-1

		if int(y/2) < 511 :
			ay = int(y/2)
		else:
			ay = int(y/2)-1
		

		a = ((img[ax-1,ay])/5)
		b = ((img[ax,ay-1])/5)
		c = ((img[ax+1,ay])/5)
		d = ((img[ax,ay+1])/5)
		e = ((img[ax,ay])/5)
		avgsum = a + b + c + d + e
		scaledu2[x,y] = int(avgsum)




cv2.imshow("Original",img)
cv2.moveWindow("Original", 800,0);


cv2.imshow("Scaled 1/2 - Neighbour",scaledd2)
cv2.moveWindow("Scaled 1/2 - Neighbour",0,0);

cv2.imshow("Scaled 2 - Neighbour",scaledu2)
cv2.moveWindow("Scaled 2 - Neighbour",200,0);


cv2.waitKey(0)
cv2.destroyAllWindows()

