import sys
import pygame
from settings import Settings
from eggplant import Eggplant
from bullet import Bullet
from peach import Peach

class EggplantShooter:
	"""main class for game environment"""
	def __init__(self):
		"""initialize pygame and set environment"""
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width,
												self.settings.screen_height))
		#self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		#self.settings.screen_width = self.screen.get_rect().width
		#self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Eggplant Shooter")
		self.eggplant = Eggplant(self)
		self.bullets = pygame.sprite.Group()
		self.peaches = pygame.sprite.Group()
		self._create_fleet()
		
	def run_game(self):
		"""main game loop"""
		while True:
			self._check_events()
			self.eggplant.update()
			self.bullets.update()
			self._update_screen()
			#get rid of bullets that have disappeared
			for bullet in self.bullets.copy():
				if bullet.rect.bottom <0:
					self.bullets.remove(bullet)
			
	def _check_events(self):
		"""main modlue used to check events"""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _update_screen(self):
		"""update events and show them to the screen"""
		self.screen.fill(self.settings.bg_color)
		self.eggplant.blitme()
		self.peaches.draw(self.screen)
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		pygame.display.flip()
		
	def _check_keydown_events(self, event):
		"""method to check what button was pressed"""
		if event.key == pygame.K_q:
				sys.exit()
		elif event.key == pygame.K_RIGHT:
			self.eggplant.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.eggplant.moving_left = True
		elif event.key == pygame.K_UP:
			self.eggplant.moving_up = True
		elif event.key == pygame.K_DOWN:
			self.eggplant.moving_down = True
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
			
	def _check_keyup_events(self, event):
		"""method to check what button was released"""
		if event.key == pygame.K_RIGHT:
			self.eggplant.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.eggplant.moving_left = False
		elif event.key == pygame.K_UP:
			self.eggplant.moving_up = False
		elif event.key == pygame.K_DOWN:
			self.eggplant.moving_down = False
			
	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group."""
		if len(self.bullets) < 3:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _create_fleet(self):
		"""Create the fleet of peaches"""
		#Create a peach and find the number of peaches in a row
		#Spacing between each peach is equal to on peach width
		peach = Peach(self)
		peach_width = peach.rect.width
		available_space_x = self.settings.screen_width - (2 * peach_width)
		number_peaches_x = available_space_x // (2 * peach_width)
		for peach_number in range(number_peaches_x):
			#create a peach and place it in the row
			peach = Peach(self)
			peach.x = peach_width + 2* peach_width * peach_number
			peach.rect.x = peach.x
			self.peaches.add(peach)
if __name__ == '__main__':
	es = EggplantShooter()
	es.run_game()
