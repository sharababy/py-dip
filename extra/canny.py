import cv2
import numpy as np

print("Image Edge Detection");

# img = cv2.imread("circle.grey.jpg",0);

img = cv2.imread("lab.jpg",0);


edges = cv2.Canny(img,50,150,apertureSize = 3)

cv2.imwrite('cannyEdges.jpg',edges)
# cv2.waitKey(0);
# cv2.destroyAllWindows();