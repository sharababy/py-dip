import cv2
import numpy as np
import scipy.fftpack as fft
import random as rand

print("-- DCT Watermarking -- ")

img 	= cv2.imread("lena.jpg",0)
wm 		= cv2.imread("watermark.jpeg",0)

height 	= img.shape[0]
width 	= img.shape[1]

# l = []
# for x in range(0,height):
# 	for y in range(0,width):
# 		l.append(img[x,y])			

# dimg = fft.dct(img)
dimg = cv2.dct(np.float32(img))
# dimg = np.uint8(dimg) * 255
# cimg = cv2.idct(dimg).astype(np.uint8)

# eimg = np.zeros(( height, width, 1), np.uint8)

# for x in range(0,height):
# 	for y in range(0,width):
# 		eimg[x,y] = cimg[x*10 + y];

# print(cimg.shape)

# dimg = np.real(np.fft.fft2(img));
# cimg = np.real(np.fft.ifft2(dimg));

hwm = wm.shape[0];
wwm = wm.shape[1];

_wm = np.zeros(( hwm, wwm, 1), np.float32)

for x in range(0,hwm):
	for y in range(0,wwm):
		_wm[x,y] = 255;

location = []

for x in range(0,hwm):
	for y in range(0,wwm):
		location.append([rand.randrange(0,height),rand.randrange(0,width)])

alpha = 0.4;


dwm = cv2.dct(np.float32(wm))

i = 0;

for x in range(0,hwm):
	for y in range(0,wwm):
		_x = location[i][0]
		_y = location[i][1]
		i+=1
		# dimg[_x,_y] = np.float32(alpha*(dwm[x,y]) + (1-alpha)*(dimg[_x,_y]))
		dimg[_x,_y] = dwm[x,y];

# print(len(location))

cimg = cv2.idct(dimg).astype(np.uint8)

rdimg = cv2.dct(np.float32(cimg))

# rcimg = cv2.idct(rdimg).astype(np.uint8)

i=0

for x in range(0,hwm):
	for y in range(0,wwm):
		_x = location[i][0]
		_y = location[i][1]
		i+=1
		_wm[x,y] = rdimg[_x,_y]

# _cwm = fft.idct(_wm);

_cwm = cv2.idct(_wm).astype(np.uint8)

cv2.imshow("Original",img)
#cv2.moveWindow("Original", 800,0);



# cv2.imshow("dct",dimg)
# cv2.moveWindow("dct",400,0);

cv2.imshow("converted",cimg)
cv2.moveWindow("converted",900,0);

# cv2.imshow("re idct",rcimg)
# cv2.moveWindow("re idct",900,0);


cv2.imshow("wm",wm)
cv2.moveWindow("wm",300,0);

cv2.imshow("cwm",_cwm)
cv2.moveWindow("cwm",10,0);


cv2.waitKey(0)
cv2.destroyAllWindows()
