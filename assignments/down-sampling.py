import cv2
import numpy as np

print("-- Sampling an Image -- ")

img 	= cv2.imread("lena.jpg",0)

height 	= img.shape[0]
width 	= img.shape[1]

downsampled2 = np.zeros(( int(height/2), int(width/2) ,3), np.uint8)
downsampled4 = np.zeros(( int(height/4), int(width/4) ,3), np.uint8)
downsampled6 = np.zeros(( int(height/6), int(width/6) ,3), np.uint8)
# upsampled2 	= np.zeros(( int(height*2), int(width*2) ,3), np.uint8)

# res = cv2.resize(img,(int(width/2), int(height/2)), interpolation = cv2.INTER_AREA)

for x in range(0,height):
	for y in range(0,width):
		downsampled2[ int(x/2), int(y/2)] = img[x,y]

# diff = np.zeros(( int(height/2), int(width/2) ,3), np.uint8)

# for x in range(0,int(height/2)):
# 	for y in range(0,int(width/2)):
# 		diff[x,y] = res[x,y] - downsampled2[x,y]

# cv2.imshow("Diff = res - downsampled2",diff)

# for x in range(0,int(height/2)):
# 	for y in range(0,int(width/2)):
# 		diff[x,y] = downsampled2[x,y] - res[x,y]		

# cv2.imshow("Diff = downsampled2 - res ",diff)

for x in range(0,height):
	for y in range(0,width):
		downsampled4[ int(x/4), int(y/4)] = img[x,y]

for x in range(0,int(height/6)):
	for y in range(0,int(width/6)):
		downsampled6[ int(x), int(y)] = img[x*6,y*6]

# for x in range(0,height*2):
# 	for y in range(0,width*2):
# 		upsampled2[x,y] = img[int(x/2),int(y/2)]

# for x in range(0,10):
# 	for y in range(0,10):
# 		print(img[x][y])

# Display an image in a window
#
# cv2.imshow("Up-sampled",upsampled2)
# cv2.moveWindow("Up-sampled", 200,0);

cv2.imshow("Original",img)
cv2.moveWindow("Original", 800,0);

cv2.imshow("Down-sampled-2",downsampled2)
cv2.moveWindow("Down-sampled-2",500,0);
# cv2.imshow("Res",res)

cv2.imshow("Down-sampled-4",downsampled4)
cv2.moveWindow("Down-sampled-4",300,0);

cv2.imshow("Down-sampled-6",downsampled6)
cv2.moveWindow("Down-sampled-6",0,0);



cv2.waitKey(0)
cv2.destroyAllWindows()

