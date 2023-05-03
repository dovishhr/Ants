import board

def look(ant,dire):
	space = False
	if dire == "up" and ant.y != 0:
		space = board.items[ant.x][ant.y-1]
	if dire == "down" and ant.y != len(board.items[0])-1:
		space = board.items[ant.x][ant.y+1]
	if dire == "right" and ant.x != len(board.items)-1:
		space = board.items[ant.x+1][ant.y]
	if dire == "left" and ant.x != 0:
		space = board.items[ant.x-1][ant.y]
	if space:
		return space.getType()
	return False
	
def smell(ant,dire):
	space = False
	if dire == "up" and ant.y != 0:
		space = board.smells[ant.x][ant.y-1]
	if dire == "down" and ant.y != len(board.items[0])-1:
		space = board.smells[ant.x][ant.y+1]
	if dire == "right" and ant.x != len(board.items)-1:
		space = board.smells[ant.x+1][ant.y]
	if dire == "left" and ant.x != 0:
		space = board.smells[ant.x-1][ant.y]
	return space
	
def spit(ant, dire, smell):
	if dire == "up" and ant.y != 0:
		board.smells[ant.x][ant.y-1] = smell
	if dire == "down" and ant.y != len(board.items[0])-1:
		board.smells[ant.x][ant.y+1] = smell
	if dire == "right" and ant.x != len(board.items)-1:
		board.smells[ant.x+1][ant.y] = smell
	if dire == "left" and ant.x != 0:
		board.smells[ant.x-1][ant.y] = smell
	return False
	
