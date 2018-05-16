import cv2
import numpy as np






def bilinear_interpolation(x, y, points):
    '''Interpolate (x,y) from values associated with four points.

    The four points are a list of four triplets:  (x, y, value).
    The four points can be in any order.  They should form a rectangle.

        >>> bilinear_interpolation(12, 5.5,
        ...                        [(10, 4, 100),
        ...                         (20, 4, 200),
        ...                         (10, 6, 150),
        ...                         (20, 6, 300)])
        165.0

    '''

    points = sorted(points)               # order points by x, then by y
    (x1, y1, q11), (_x1, y2, q12), (x2, _y1, q21), (_x2, _y2, q22) = points

    if x1 != _x1 or x2 != _x2 or y1 != _y1 or y2 != _y2:
        raise ValueError('points do not form a rectangle')
    if not x1 <= x <= x2 or not y1 <= y <= y2:
        raise ValueError('(x, y) not within the rectangle')

    return (q11 * (x2 - x) * (y2 - y) +
            q21 * (x - x1) * (y2 - y) +
            q12 * (x2 - x) * (y - y1) +
            q22 * (x - x1) * (y - y1)
           ) / ((x2 - x1) * (y2 - y1) + 0.0)







print("-- Scaling an Image -- ")

img     = cv2.imread("lena.jpg",0)

height  = img.shape[0]
width   = img.shape[1]

scaledd2 = np.zeros(( int(height/2), int(width/2) ,3), np.uint8)
scaledu2 = np.zeros(( int(height*2), int(width*2) ,3), np.uint8)

for x in range(0,int(height/2)):
    for y in range(0,int(width/2)):
        ax = int(x*2)
        ay = int(y*2)

        if (ax+1) > 511 :
            ax = 510
        if (ax-1) < 0 :
            ay = 0
       
        if (ay+1) > 511 :
            ay = 510
        if (ay-1) < 0 :
            ay = 0

        scaledd2[x,y] = bilinear_interpolation(ax,ay,
            [(ax+1,ay+1,img[ax+1,ay+1]),
            (ax-1,ay+1,img[ax-1,ay+1]),
            (ax-1,ay-1,img[ax-1,ay-1]),
            (ax+1,ay-1,img[ax+1,ay-1]),
            ])


for x in range(0,int(height*2)):
    for y in range(0,int(width*2)):
        ax = int(x/2)
        ay = int(y/2)

        if (ax+1) > 511 :
            ax = 510
        if (ax-1) < 0 :
            ay = 0
       
        if (ay+1) > 511 :
            ay = 510
        if (ay-1) < 0 :
            ay = 0

        scaledu2[x,y] = bilinear_interpolation(ax,ay,
            [(ax+1,ay+1,img[ax+1,ay+1]),
            (ax-1,ay+1,img[ax-1,ay+1]),
            (ax-1,ay-1,img[ax-1,ay-1]),
            (ax+1,ay-1,img[ax+1,ay-1]),
            ])


cv2.imshow("Original",img)
cv2.moveWindow("Original", 800,0);


cv2.imshow("Scaled 1/2 - Bilinear",scaledd2)
cv2.moveWindow("Scaled 1/2 - Bilinear",0,0);

cv2.imshow("Scaled 2 - Bilinear",scaledu2)
cv2.moveWindow("Scaled 2 - Bilinear",200,0);


cv2.waitKey(0)
cv2.destroyAllWindows()



