import cv2

print("Python Tester Started.")

img = cv2.imread("love.jpg",0)


for x in xrange(1,10):
	for y in xrange(1,10):
		print(img[x][y])


# Display an image in a window
#
# cv2.imshow("LOVE",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()