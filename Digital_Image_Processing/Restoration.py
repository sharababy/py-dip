import cv2
import numpy as np

def GaussianFilter(shape=(512,512),sigma=1):
    m,n = [(ss-1.)/2. for ss in shape]
    y,x = np.ogrid[-m:m+1,-n:n+1]
    h = np.exp( -(x*x + y*y) / (2.*sigma*sigma) )
    h[ h < np.finfo(h.dtype).eps*h.max() ] = 0
    sumh = h.sum()
    if sumh != 0:
        h /= sumh
    return h


def restoreImage(deg):       
	DFT = np.fft.fft2(deg)
	H = np.fft.fft2(GaussianFilter())  #frequency domain gaussian filter
	dft =np.zeros((512,512),dtype=np.complex_)   #matrix to store the restored image
	epsilon=1

	for i in range(512):            #logic to eliminate small values to ensure divide by zero error
		for j in range(512):
			H[i][j]= H[i][j] if H[i][j]>epsilon else epsilon

	for i in range(512):            #retrieving the image 
		for j in range(512):
			dft[i][j]=DFT[i][j]/H[i][j]

	
	res=np.fft.ifft2(dft)    

	cv2.imshow('restored image',np.uint8(res))
	cv2.waitKey(0)
	cv2.destroyAllWindows()


im = cv2.imread('./images/lena.png',0)
img = cv2.filter2D(im,-1,GaussianFilter())
noise=cv2.randn(im,(0),(10))
deg=img+noise

cv2.imshow('with noise',np.uint8(deg))

restoreImage(deg)

