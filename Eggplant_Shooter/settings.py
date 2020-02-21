"""Settings file for eggplant shooter game"""
class Settings:
	def __init__(self):
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (100, 200, 200)
		self.eggplant_speed = .2
		# Bullet settings
		self.bullet_speed = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3
