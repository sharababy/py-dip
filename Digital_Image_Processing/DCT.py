import cv2
import numpy as np
import random as rd

'''
Question 1:
Implement DCT based watermarking scheme. 
Implement the watermark extraction procedure. 
Find the correlation between inserted watermark and extracted watermark.
'''

originalImage = cv2.imread('./images/lena.png',0) 

#take dct
dctImage	= cv2.dct(np.float32(originalImage)) 
_1dImage = dctImage.ravel()

markLocation= [rd.randrange(512*512) for x in range(512)]

#normal distributed watermark
watermark = np.random.normal(0,1,512)

alpha = 0.3   

#placing the watermark in random location
for i in range(512):
	_1dImage[markLocation[i]]=_1dImage[markLocation[i]]*(1+alpha*watermark[i])


dctImage =_1dImage.reshape((512,512))
idctImage	= cv2.idct(dctImage).astype(np.uint8)

dct_again = cv2.dct(np.float32(idctImage))
_1d_DCT = dct_again.ravel()
extracted_watermark =np.zeros(512)


for i in range(512):
	extracted_watermark[i]=(_1d_DCT[markLocation[i]]/_1dImage[markLocation[i]]-1)/alpha


#find correlation between the extracted watermark and original
print("Correlation between Extracted Watermark and Actual Watermark:")
print(np.corrcoef(extracted_watermark ,watermark))



cv2.imshow('With Watermark',idctImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

