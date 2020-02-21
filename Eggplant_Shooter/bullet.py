import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to manage bullets fired from the eggplant"""
	def __init__(self, es_game):
		"""Create a bullet object at the eggplants current position"""
		super().__init__()
		self.screen = es_game.screen
		self.settings = es_game.settings
		self.eggplant = es_game.eggplant
		self.color = self.settings.bullet_color
		# Creat a bullet rect at (0, 0) and then set currect position
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
								self.settings.bullet_height)
		self.rect.midtop = self.eggplant.rect.midtop
		# Store the ships current position as a decimal value
		self.y = float(self.rect.y)
		
	def update(self):
		"""Move the bullet up the screen"""
		self.y -= self.settings.bullet_speed
		#Update the rect postion.
		self.rect.y = self.y
		
	def draw_bullet(self):
		"""Draw the bullet to the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)
