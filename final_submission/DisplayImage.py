
import cv2

class DisplayImage():
	def __init__(self):
		self.image_array=[]

	def display(self):
		self.image_array.append(cv2.imread("1.jpg"))
		self.image_array.append(cv2.imread("2.jpg"))
		self.image_array.append(cv2.imread("3.jpg"))
		self.image_array.append(cv2.imread("4.jpg"))
		cv2.imshow("1",self.image_array[0])
		cv2.imshow("2",self.image_array[1])
		cv2.imshow("3",self.image_array[2])
		cv2.imshow("4",self.image_array[3])
		cv2.waitKey(0)
	def __del__(self):
		pass
