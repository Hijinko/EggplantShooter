import pygame
from pygame.sprite import Sprite
class Peach(Sprite):
	"""A Class to represent a single peach in the fleet"""
	def __init__(self, es_game):
		"""initialize the peach"""
		super().__init__()
		self.screen = es_game.screen
		#load the peach image and set its rect
		self.image = pygame.image.load('images/peach.bmp')
		self.image = pygame.transform.scale(self.image, (50, 41))
		self.rect = self.image.get_rect()
		#start each new peach near the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		#store the peaches exact horizontal position
		self.x = float(self.rect.x)
		
		
