import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

class UnderlinedWordExtract():
	'''class containing modules to extract underlined word from an image'''
	def __init__(self):
		pass
	def read_image_binary(self,in_img,thresh_val=100):
		'''
		in_img : input image file
		thresh_val = threshhold value taken in normal mode
		returns binary inverted image 
		'''
		self.img = cv2.imread(in_img)
		self.img_orig = np.copy(self.img)
		self.gray = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
		ret,self.binar = cv2.threshold(self.gray,thresh_val,255,\
			cv2.THRESH_BINARY_INV)

	def detect_lines(self,minLineLength=30,maxLineGap=2,threshold=100):
		'''
		detect lines in the binary image. read_image_binary should
		be run before
		also gives a lined image which can be plotted to show 
		lines
		'''
		self.img_lined = np.copy(self.img)
		self.lines = cv2.HoughLinesP(self.binar,1,np.pi/180,\
			threshold,minLineLength=minLineLength,maxLineGap=maxLineGap)
		print "lines:"
		i = 0
		for x1,y1,x2,y2 in self.lines[0]:
			i = i+1
			print (x1,y1)
#			cv2.circle(self.img_lined,(x1,y1),i,(0,255,0))
#			cv2.line(self.img_lined,(x1,y1),(x2,y2),(0,255,0),2)



	def dilate_image(self,kern_N=5,n_iter=1):
		'''Dilating the image to form each word as a single contour'''
		kernel = np.ones((kern_N,kern_N),np.uint8)
		self.img_dilated = cv2.dilate(self.binar,kernel,iterations = n_iter)
	
	def erode_image(self,kern_N=5,n_iter=1):
		kernel = np.ones((kern_N,kern_N),np.uint8)
		self.img_eroded = cv2.erode(self.img_dilated,kernel,iterations = n_iter)


	def detect_contour(self,image):
		'''Detect contours in the dilated image'''
		temp = np.copy(image)
		self.contours, a = cv2.findContours\
			(temp,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	def draw_rect(self):
		'''Draw rectangle around detected contours'''
		self.underlined_coord = []
		self.img_contoured = np.copy(self.img)
		print "contours:"
		for i in range(len(self.contours)):
			rect = cv2.boundingRect(self.contours[i])
			pt1 = (rect[0],rect[1])
			pt2 = (rect[0]+rect[2],rect[1]+rect[3])
			lb_pt = (rect[0],rect[1]+rect[3])
			for x1,y1,x2,y2 in self.lines[0]:
				if abs(x1-lb_pt[0])<5 and abs(lb_pt[1]-y1)<5:
					self.underlined_coord.append((rect[0],\
						rect[1],rect[2],rect[3]))
#					print (x1,y1), lb_pt
#					cv2.circle(self.img_lined,(x1,y1),i,(0,255,0))
#					cv2.circle(self.img_contoured,lb_pt,i+1,(255,0,0))
					cv2.rectangle(self.img_contoured,pt1,pt2,(100,100,100),thickness=2)

	def crop_rect(self,out_img='image_underlined.png'):
		'''Crop from the image the contour which matches the underlines'''
		rect = []
		for i in range(4):
			rect.append(self.underlined_coord[0][i])
		self.img_underlined = self.img[rect[1]-5:rect[1]+rect[3]+5,rect[0]:rect[0]+rect[2]+5]
		cv2.imwrite(out_img,self.img_underlined)
#tests

read_text = UnderlinedWordExtract()
read_text.read_image_binary(sys.argv[1])
read_text.detect_lines()
read_text.dilate_image(kern_N=5,n_iter=2)
read_text.erode_image(kern_N=5,n_iter=2)
read_text.detect_contour(read_text.img_eroded)
read_text.draw_rect()
read_text.crop_rect()

plt.subplot(221),plt.imshow(read_text.img_lined,cmap = 'gray')
plt.title('Lined Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(read_text.img_dilated,cmap = 'gray')
plt.title('Dilated Image'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(read_text.img_contoured,cmap = 'gray')
plt.title('Contoured Image'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(read_text.img_underlined,cmap = 'gray')
plt.title('Underlined Image'), plt.xticks([]), plt.yticks([])
plt.show()
