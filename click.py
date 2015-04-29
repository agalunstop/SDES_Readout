def click(image_name="photo.bmp"):
	import pygame.camera
	pygame.camera.init()
	cam = pygame.camera.Camera\
		(pygame.camera.list_cameras()[0])
	cam.start()
	img = cam.get_image()
	import pygame.image
	pygame.image.save(img, image_name)
	pygame.camera.quit()
	cam.stop()

import sys
click(sys.argv[1])
