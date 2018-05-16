import cv2
import numpy as np
import math

print("-- Histogram Equalized Image -- ")

img 	= cv2.imread("pollen2.tif",0)

height 	= img.shape[0]
width 	= img.shape[1]

final = np.zeros(( height, width ,3), np.uint8)

newImg = np.zeros(( height, width ,3), np.uint8)

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


# for x in range(0,height):
# 	for y in range(0,width):
# 		newImg[x,y] = clevels[img[x,y]];


# ---------------------------------------

imf 	= cv2.imread("org.tif",0)

_height 	= imf.shape[0]
_width 	= imf.shape[1]

newImf = np.zeros(( _height, _width ,3), np.uint8)

_levels = []

total = _height*_width

for x in range(0,256):
	_levels.append(0)


for x in range(0,_height):
	for y in range(0,_width):
		_levels[imf[x,y]] += 1;

for x in range(0,256):
	_levels[x] = _levels[x]/total


sums = 0;

_clevels = []


for x in range(0,256):
	for y in range(0,x+1):
		sums += _levels[y]
		# print(l[y])
	_clevels.append(sums)
	# print()
	sums = 0

# for x in range(0,256):
# 	print(x,_clevels[x])


for x in range(0,256):
	_clevels[x] = int(_clevels[x]*255)


# for x in range(0,_height):
# 	for y in range(0,_width):
# 		newImf[x,y] = _clevels[imf[x,y]];


flevels = []

for x in range(0,256):
	flevels.append(0)

for x in range(0,256):
	if clevels[x] in _clevels:
		flevels[x] = _clevels.index(clevels[x]);
	else:
		for y in range(0,256):
			if abs(_clevels[y] - clevels[x]) <= 5:
				flevels[x] = _clevels[y];		



for x in range(0,height):
	for y in range(0,width):
		final[x,y] = flevels[img[x,y]];


# for x in range(0,256):
# 	print(x,clevels[x])

cv2.imshow("Original",img)
cv2.moveWindow("Original", 800,0);

cv2.imshow("Matched With",imf)
cv2.moveWindow("Matched With", 400,0);


cv2.imshow("Matched",final)
cv2.moveWindow("Matched",0,0);

cv2.waitKey(0)
cv2.destroyAllWindows()
