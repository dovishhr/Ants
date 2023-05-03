import pygame
import random
from antActions import *

actions = ["moveUp", "moveDown", "moveLeft", "moveRight", "getUp", "getDown", "getLeft", "getRight", "putUp", "putDown", "putRight", "putLeft"]





class TestAnts:
	def __init__(self, x, y, color):
		self.x=x
		self.y=y
		self.color=color
		self.holding=None

	def draw(self, surface, zoom):
		rect = pygame.Rect(int ( self.x*zoom ), int ( self.y*zoom ), int(zoom), int(zoom))
		pygame.draw.rect(surface, self.color, rect, 0)

	def act(self):
		spit(self, "down", 100)
		print(smell(self, "down"))
		return "moveDown"
		
class DumbAnts:
	def __init__(self, x, y, color):
		self.x=x
		self.y=y
		self.color=color
		self.holding=None

	def draw(self, surface, zoom):
		rect = pygame.Rect(int ( self.x*zoom ), int ( self.y*zoom ), int(zoom), int(zoom))
		pygame.draw.rect(surface, self.color, rect, 0)

	def act(self):
		return actions[random.randrange(len(actions))]


class StinkAnts:
	def __init__(self, x, y, color):
		self.x=x
		self.y=y
		self.color=color
		self.holding=None

	def draw(self, surface, zoom):
		rect = pygame.Rect(int ( self.x*zoom ), int ( self.y*zoom ), int(zoom), int(zoom))
		pygame.draw.rect(surface, self.color, rect, 0)

	def act(self):
		if not random.randrange(10):
			return actions[random.randrange(4)]
			
		direc = ["up","right","down","left"]
		less = ["up"]
		more = ["up"]
		for d in direc:
			stink = smell(self,d)
			print(str(stink))
			if stink == False:
				continue
			if stink == None:
				spit(self,d,1)
			else:
				if self.holding:
					spit(self,d,stink-20)
				spit(self,d,stink+10)
				if stink > smell(self,more[0]):
					more = [d]
				if stink == smell(self,more[0]):
					more.append(d)
				
				if stink < smell(self,less[0]):
					less = [d]
				if stink == smell(self,less[0]):
					less.append(d)
		print()
		more = more[random.randrange(len(more))]
		less = less[random.randrange(len(less))]
		
		if self.holding:
			if self.holding.getType() == "food":
				for d in direc:
					if look(self,d) == "home":
						print("i can see a house.. burning")
						if d == "up":
							return "putUp"
						elif d == "right":
							return "putRight"
						elif d == "down":
							return "putDown"
						elif d == "left":
							return "putLeft"
				if more == "up":
					return "moveUp"
				elif more == "right":
					return "moveRight"
				elif more == "down":
					return "moveDown"
				elif more == "left":
					return "moveLeft"
			return "putUp"
			
		for d in direc:
			if look(self,d) == "food":
				if d == "up":
					return "getUp"
				elif d == "right":
					return "getRight"
				elif d == "down":
					return "getDown"
				elif d == "left":
					return "getLeft"

		if less == "up":
			return "moveUp"
		elif less == "right":
			return "moveRight"
		elif less == "down":
			return "moveDown"
		elif less == "left":
			return "moveLeft"

			

		return actions[random.randrange(len(actions))]
