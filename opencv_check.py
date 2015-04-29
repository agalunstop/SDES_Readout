#from cv2.cv import *
import sys
#
#img = LoadImage(sys.argv[1])
#NamedWindow("opencv")
#ShowImage("opencv",img)
#WaitKey(0)
import cv2
import numpy
from matplotlib import pyplot as plt

img = cv2.imread(sys.argv[1])
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,binar = cv2.threshold(gray,100,255,cv2.THRESH_BINARY_INV)

lines = cv2.HoughLinesP(binar,1,numpy.pi/180,2,minLineLength=200,maxLineGap=10)
print lines


for x1,y1,x2,y2 in lines[0]:
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(binar,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
cv2.imwrite('houghlines5.jpg',img)


#lines = cv2.HoughLines(binar,1,numpy.pi/180,150)

#for rho,theta in lines[0]:
#    a = numpy.cos(theta)
#    b = numpy.sin(theta)
#    x0 = a*rho
#    y0 = b*rho
#    x1 = int(x0 + 1000*(-b))
#    y1 = int(y0 + 1000*(a))
#    x2 = int(x0 - 1000*(-b))
#    y2 = int(y0 - 1000*(a))
#    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
#
#cv2.imwrite('houghlines.jpg',img)
#
