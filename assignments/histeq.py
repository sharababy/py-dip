import cv2
import numpy as np
import math

print("-- Histogram Equalized Image -- ")

# img 	= cv2.imread("pollen.tif",0)

img 	= cv2.imread("medow.jpg",0)

height 	= img.shape[0]
width 	= img.shape[1]

uniformImg = np.zeros(( height, width ,3), np.uint8)

levels = []

total = height*width

for x in range(0,256):
	levels.append(0)


for x in range(0,height):
	for y in range(0,width):
		levels[img[x,y]] += 1;

for x in range(0,256):
	levels[x] = levels[x]/total


sums = 0;

clevels = []


for x in range(0,256):
	for y in range(0,x+1):
		sums += levels[y]
		# print(l[y])
	clevels.append(sums)
	# print()
	sums = 0

# for x in range(0,256):
# 	print(x,clevels[x])


for x in range(0,256):
	clevels[x] = int(clevels[x]*255)


for x in range(0,height):
	for y in range(0,width):
		uniformImg[x,y] = clevels[img[x,y]];



# for x in range(0,256):
# 	print(x,clevels[x])

cv2.imshow("Original",img)
cv2.moveWindow("Original", 800,0);

cv2.imshow("Equalized",uniformImg)
cv2.moveWindow("Equalized",0,0);

cv2.waitKey(0)
cv2.destroyAllWindows()
