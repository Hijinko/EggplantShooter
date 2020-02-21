"""modlue for the eggplan character"""
import pygame

class Eggplant:
	"""eggplant character class"""
	def __init__(self, es_game):
		self.screen = es_game.screen
		self.screen_rect = es_game.screen.get_rect()
		self.settings = es_game.settings
		#load the image and set its starting position
		self.image = pygame.image.load('images/eggplant.bmp')
		self.image = pygame.transform.scale(self.image, (50, 50))
		self.rect = self.image.get_rect()
		#start each ship at the bottom center of the screen
		self.rect.midbottom = self.screen_rect.midbottom
		#moving flags
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		
	def blitme(self):
		"""Draw the image at its current position"""
		self.screen.blit(self.image, self.rect)
		
	def update(self):
		"""update the eggplants position based on the movement flag"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.eggplant_speed
		if self.moving_left and self.rect.left > self.screen_rect.left:
			self.x -= self.settings.eggplant_speed
		if self.moving_up and self.rect.top > self.screen_rect.top:
			self.y -= self.settings.eggplant_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.eggplant_speed
		
		# set rect to x
		self.rect.x = self.x
		self.rect.y = self.y
