import cv2
import numpy as np
from helper import linearSolver,truncate
import random as rd

print("Line Detection");

# img = cv2.imread("line3.jpeg",0);

def lineDetect(imgName):

	img = cv2.imread(imgName,0);

	height = img.shape[0];
	width = img.shape[1];


	print(imgName)
	print("Height of image",height);
	print("width of image",width);


	binzed = np.zeros((height,width ,1), np.uint8);

	for x in range(0,height):
		for y in range(0,width):
			if img[x,y] > 100:
				binzed[x,y] = 255;
			else:
				binzed[x,y] = 0;


	onEdge = [];

	for x in range(0,height):
		for y in range(0,width):
			if binzed[x,y] < 50:
				onEdge.append([x,y]); 


	print(" Edge Length",len(onEdge))

	mcSpace = []

	# x = rd.randint(1,len(onEdge))

	for x in range(0,len(onEdge)):
		for z in range(x+1,len(onEdge)):
			
			ax = (onEdge[x])[0];
			ay = (onEdge[x])[1];

			ax_1 = (onEdge[z])[0];
			ay_1 = (onEdge[z])[1];

			if ( abs(ax - ax_1) > 10  and abs(ay - ay_1) > 10):
				[m,c] = linearSolver( ax,ay , ax_1,ay_1 )

				for y in range(0,len(mcSpace)):
					if ((mcSpace[y])[0][0] == [m,c][0] and abs((mcSpace[y])[0][1] - [m,c][1]) < 5 ):
						(mcSpace[y])[1] += 1;
						break;
				else:

					mcSpace.append([[m,c],1])

		prcnt = int((x/len(onEdge))*100)
		print("MC space = ",len(mcSpace),prcnt,"% done",end='\r')
	print()


	sortedMc = sorted(mcSpace, key=lambda mcIndex: mcIndex[1])


	thefile = open('mcSpace.txt', 'w')
	for item in sortedMc:
	  thefile.write("%s,\n" % item)

	totalInter = 0
	totalSlope = 0

	for x in range(0,len(sortedMc)):
		totalInter += sortedMc[x][0][1]
		totalSlope += float(sortedMc[x][0][0])

	avgInter = int(totalInter/len(sortedMc))
	avgSlope = truncate(totalSlope/len(sortedMc) , 2)


	print("AVG Inter:", avgInter)
	print("AVG Slope:", avgSlope)

	# for w in range(1,10):
		
	mcMostFreq = sortedMc[-1];

	print(mcMostFreq)

	# for x in range(0,height):
	# 	for y in range(0,width):
	# 		slope = avgSlope#(mcMostFreq[0])[0]
	# 		intercept =avgInter#(mcMostFreq[0])[1]
	# 		rhs = int((float(slope)*y) + intercept);
	# 		if( x == rhs):
	# 			binzed[x,y] = 50;

	# cv2.imshow("AVG",binzed);
	# cv2.moveWindow("AVG",400,50);

	slope = avgSlope
	intercept = avgInter


	# slope = (mcMostFreq[0])[0]
	# intercept =(mcMostFreq[0])[1]

	for x in range(0,height):
		for y in range(0,width):		
			rhs = int((float(slope)*x) + intercept);
			if( y == rhs):
				img[x,y] = 50;
		

	# for w in range(0,len(mcSpace)):
	# 		print(mcSpace[w])


	# lined = np.zeros((height,width ,3), np.uint8);

	# cv2.imshow("Lined",lined);
	# cv2.moveWindow("Lined",400,50);

	cv2.imshow(imgName,img);


	# cv2.imshow("Binarized",binzed);
	# cv2.moveWindow("Binarized",400,50);


lineDetect("line.jpeg")
lineDetect("line2.jpeg")
lineDetect("line3.jpeg")
lineDetect("line4.jpeg")
lineDetect("line5.jpeg")
lineDetect("line6.jpeg")
lineDetect("line7.jpeg")
lineDetect("line8.jpeg")


cv2.waitKey(0);
cv2.destroyAllWindows();