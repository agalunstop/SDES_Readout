##Authors: Neeraj Babu & Sonal Gupta
## TDD for Click function

##Modules needed here for execution
import pygame.camera
import pygame.image
import os
class Click():
	def __init__(self):
		pygame.camera.init()
	def clickphoto(self):
		self.image_name="clicked.bmp"
		self.cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
		self.cam.start()
		self.img = self.cam.get_image()
		pygame.image.save(self.img, self.image_name)
		pygame.camera.quit()
		self.cam.stop()
	def __del__(self):
		os.remove(self.image_name)

###Test for Click()

