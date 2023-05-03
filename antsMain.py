import pygame
from antTypes import *
import random
import board

teams = [DumbAnts]
antsPerTeam = 5
rocks = 0
foods = 1200
zoom = 10

class Game:

	def __init__( self, width, height ):
		self.mWidth = width
		self.mHeight = height
		self.mMapWidth = int(width/zoom-1)
		self.mMapHeight = int(height/zoom-1)
		self.teams = []
		self.rocks = []
		self.foods = []
		self.makeSmells()
		#make homes
		for team in teams:
			home = board.Home(team,random.randrange(self.mMapWidth),random.randrange(self.mMapHeight),(random.randrange(255),random.randrange(255),random.randrange(255)))
			self.teams.append(home)
		#make starter ants
		for (i,home) in enumerate(self.teams):
			for j in range(antsPerTeam):
				self.addAnt(home,teams[i])
		#make rocks
		for i in range(rocks):
			rock = board.Rock(random.randrange(self.mMapWidth),random.randrange(self.mMapHeight))
			self.rocks.append(rock)
		#make food
		for i in range(foods):
			food = board.Food(random.randrange(self.mMapWidth),random.randrange(self.mMapHeight))
			self.foods.append(food)

	def addAnt( self, home, kind ):
		ant = kind(home.x,home.y,home.teamColor)
		home.ants.append(ant)
		print(len(home.ants))

	def isRock( self, ant, dire ):
		try:
			if dire == "up":
				return board.items[ant.x][ant.y-1]
			elif dire == "down":
				return board.items[ant.x][ant.y+1]
			elif dire == "left":
				return board.items[ant.x-1][ant.y]
			else:
				return board.items[ant.x+1][ant.y]
		except:
			return False

	def makeSmells ( self ):
		board.smells = [None]*(self.mMapWidth+1)
		for i in range(len(board.smells)):
			board.smells[i] = [None]*(self.mMapHeight+1)

	def canMove( self, ant, dire ):
		if dire == "up":
			return ant.y > 0 and not self.isRock(ant,"up")
		elif dire == "down":
			return ant.y < self.mMapHeight and not self.isRock(ant,"down") 
		elif dire == "right":
			return ant.x < self.mMapWidth and not self.isRock(ant,"right")
		elif dire == "left":
			return ant.x > 0 and not self.isRock(ant,"left")

	def updateBoard ( self ):
		board.items = [None]*(self.mMapWidth+1)
		for i in range(len(board.items)):
			board.items[i] = [None]*(self.mMapHeight+1)
		for rock in self.rocks:
			if not rock.held:
				board.items[rock.x][rock.y] = rock
		for i,food in enumerate(self.foods):
			if not food.held:
				board.items[food.x][food.y] = food
				for home in self.teams:
					if home.x == food.x and home.y == food.y:
						self.addAnt(home,home.type)
						self.foods.pop(i)
	
	def evolve( self, dt ):
		self.updateBoard()
		for team in self.teams:
			for ant in team.ants:
				act = ant.act()
				if act == "moveDown":
					if self.canMove(ant,"down"):
						ant.y += 1
				elif act == "moveUp":
					if self.canMove(ant,"up"):
						ant.y -= 1
				elif act == "moveLeft":
					if self.canMove(ant,"left"):
						ant.x -= 1
				elif act == "moveRight":
					if self.canMove(ant,"right"):
						ant.x += 1
				elif act == "getUp":
					if not ant.holding:
						item = self.isRock(ant,"up")
						if item:
							ant.holding = item
							item.pickUp()
				elif act == "getDown":
					if not ant.holding:
						item = self.isRock(ant,"down")
						if item:
							ant.holding = item
							item.pickUp()
				elif act == "getRight":
					if not ant.holding:
						item = self.isRock(ant,"right")
						if item:
							ant.holding = item
							item.pickUp()
				elif act == "getLeft":
					if not ant.holding:
						item = self.isRock(ant,"left")
						if item:
							ant.holding = item
							item.pickUp()
				elif act == "putUp":
					if ant.holding:
						if self.canMove(ant,"up"):
							ant.holding.putDown(ant.x,ant.y-1)
							ant.holding = None
				elif act == "putDown":
					if ant.holding:
						if self.canMove(ant,"down"):
							ant.holding.putDown(ant.x,ant.y+1)
							ant.holding = None
				elif act == "putRight":
					if ant.holding:
						if self.canMove(ant,"right"):
							ant.holding.putDown(ant.x+1,ant.y)
							ant.holding = None
				elif act == "putLeft":
					if ant.holding:
						if self.canMove(ant,"left"):
							ant.holding.putDown(ant.x-1,ant.y)
							ant.holding = None


	def draw( self, surface ):
		#background
		board.backGround.draw(surface,int(self.mWidth),int(self.mHeight),int(zoom))
		#homes
		for home in self.teams:
			home.draw(surface, zoom)
		#ants
		for team in self.teams:
			for ant in team.ants:
				ant.draw(surface, zoom)
		#rocks
		for rock in self.rocks:
			if not rock.getHeld():
				rock.draw(surface, zoom)
		#foods
		for food in self.foods:
			if not food.getHeld():
				food.draw(surface, zoom)

 
