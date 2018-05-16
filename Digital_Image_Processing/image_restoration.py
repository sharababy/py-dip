import cv2
import numpy as np
'''
Question 3
Implement image restoration problem.
From the given degraded image g, find the restored image f'.
Assume that the degradation function is Gaussian filtering and 
additive noise term is salt and pepper noise.
'''
def restoreImage(deg):       
	DFT_image = np.fft.fft2(deg)
	H_filter = np.fft.fft2(applyGaussian())  #frequency domain gaussian filter
	final_dft =np.zeros((512,512),dtype=np.complex_)   #matrix to store the restored image
	epsilon=1
	for i in range(512):            #logic to eliminate small values to ensure divide by zero error
		for j in range(512):
			H_filter[i][j]= H_filter[i][j] if H_filter[i][j]>epsilon else epsilon
	for i in range(512):            #retrieving the image 
		for j in range(512):
			final_dft[i][j]=DFT_image[i][j]/H_filter[i][j]
	res=np.fft.ifft2(final_dft)    
	cv2.imshow('restored image',np.uint8(res))
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def applyGaussian(shape=(512,512),sigma=1):
    i,j = [(coordinate-1.)/2. for coordinate in shape]
    y,x = np.ogrid[-i:i+1,-j:j+1]
    outMatrix = np.exp( -(x*x + y*y) / (2.*sigma*sigma) )
    outMatrix[ outMatrix < np.finfo(outMatrix.dtype).eps*outMatrix.max() ] = 0
    out_total = outMatrix.sum()
    if out_total != 0:
        outMatrix /= out_total
    return outMatrix

if __name__ == "__main__":

	im = cv2.imread('./images/lena.png',0)
	img = cv2.filter2D(im,-1,applyGaussian())
	noise=cv2.randn(im,(0),(10))
	deg=img+noise
	cv2.imshow('with noise',np.uint8(deg))
	restoreImage(deg)
