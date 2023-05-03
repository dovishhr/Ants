import pygame
import random

items = []
smells = []

class backGround:
	def draw(surface,x,y,zoom):
		rect = pygame.Rect( 0, 0, x, y)
		pygame.draw.rect(surface, (125,125,0), rect, 0)
		
class Home:
	def __init__(self, kind, x, y, color):
		self.type = kind
		self.x = x
		self.y = y
		self.color = (color[0]//2,color[0]//2,color[0]//2)
		self.teamColor = color
		self.ants = []
	
	def getType(self):
		return ("home")
	
	def draw(self, surface, zoom):
		triangle = [(self.x*zoom,self.y*zoom+zoom),(self.x*zoom+zoom/2,self.y*zoom),(self.x*zoom+zoom,self.y*zoom+zoom)]
		pygame.draw.polygon(surface, self.color, triangle, 0)

class Rock:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.held = False
		self.color = (0,0,0)
	
	def getHeld(self):
		return self.held

	def getType(self):
		return ("rock")
	
	def draw(self, surface, zoom):
		rect = pygame.Rect(int ( self.x*zoom ), int ( self.y*zoom ), int(zoom), int(zoom))
		pygame.draw.ellipse(surface, self.color, rect, 0)

	def pickUp(self):
		self.held = True

	def putDown(self, x, y):
		self.x = x
		self.y = y
		self.held = False

class Food:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.held = False
		self.color = (204,155,86)
	
	def getHeld(self):
		return self.held

	def getType(self):
		return ("food")
	
	def draw(self, surface, zoom):
		rect = pygame.Rect(int ( self.x*zoom ), int ( self.y*zoom ), int(zoom), int(zoom))
		pygame.draw.ellipse(surface, self.color, rect, 0)

	def pickUp(self):
		self.held = True

	def putDown(self, x, y):
		self.x = x
		self.y = y
		self.held = False
