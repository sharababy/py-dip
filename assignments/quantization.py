import cv2
import numpy as np

print("-- Sampling an Image -- ")


img 	= cv2.imread("lena.jpg",0)


height 	= img.shape[0]
width 	= img.shape[1]

# quantized2 = np.zeros((height,width ,3), np.uint8)
quantized4 = np.zeros((height,width ,3), np.uint8)
quantized8 = np.zeros((height,width ,3), np.uint8)

# for x in range(0,height):
# 	for y in range(0,width):
# 		quantized2[x,y] = img[x,y] - (img[x,y]%2)

for x in range(0,height):
	for y in range(0,width):
		quantized4[x,y] = img[x,y] - (img[x,y]%4)
		quantized8[x,y] = img[x,y] - (img[x,y]%32)
		

# for x in range(0,1):
# 	for y in range(0,1):
# 		print(img[x,y]-quantized8[x,y])



# diff = np.zeros(( height, width ,3), np.uint8)

# for x in range(0,height):
# 	for y in range(0,width):
# 		if (img[x,y] - quantized8[x,y])[0] == 0:
# 			diff[x,y] = img[x,y]
# 		else:
# 			diff[x,y] = 255

# cv2.imshow("Diff = res - quantized2",diff)

cv2.imshow("Original",img)
cv2.moveWindow("Original", 800,0);

# cv2.imshow("Quantized-2",quantized2)
# cv2.moveWindow("Quantized-2",500,0);

cv2.imshow("Quantized-4",quantized4)
cv2.moveWindow("Quantized-4",300,0);

cv2.imshow("Quantized-8",quantized8)
cv2.moveWindow("Quantized-8",0,0);



cv2.waitKey(0)
cv2.destroyAllWindows()

