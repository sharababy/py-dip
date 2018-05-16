import cv2
import numpy as np

print("Image Edge Detection");

# img = cv2.imread("circle.grey.jpg",0);

img = cv2.imread("lab.jpg",0);

cv2.imshow("Circle",img);

height = img.shape[0];
width = img.shape[1];

print("Height of image",height);

print("width of image",width);

binzed = np.zeros((height,width ,1), np.uint8);
edgeX = np.zeros((height,width ,1), np.uint8)

# for x in range(0,height):
# 	for y in range(0,width):
# 		if img[x,y] > 70:
# 			binzed[x,y] = 255;
# 		else:
# 			binzed[x,y] = 0;



for x in range(1,height):
	for y in range(1,width):
		
		a = int((img[x,y]));
		ax_1 = int((img[x-1,y]));
		ay_1 = int((img[x,y-1]));


		if (abs( ax_1 - a)) > 26:
			edgeX[x,y] = 255;
		if (abs( ay_1 - a)) > 26:
			edgeX[x,y] = 255;


# cv2.imwrite("lab-b.jpg",binzed);
cv2.imwrite("lab-e.jpg",edgeX);



# cv2.imshow("Binarized",binzed);
# cv2.moveWindow("Binarized",400,50);

# cv2.imshow("EdgeX",edgeX);
# cv2.moveWindow("EdgeX",850,50);

# cv2.waitKey(0);
# cv2.destroyAllWindows();