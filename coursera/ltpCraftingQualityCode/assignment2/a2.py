# The visual representation of a wall.
WALL = '#'
# The visual representation of a hallway.
HALL = '.'
# The visual representation of a brussels sprout.
SPROUT = '@'
# Constants for the directions. Use these to make Rats move.
# The left direction.
LEFT = -1
# The right direction.
RIGHT = 1
# No change in direction.
NO_CHANGE = 0
# The up direction.
UP = -1
# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


### Warning:
### There is the implicit assumption that the maze does not depict the rats.
### The program (also rat-race) is written based on this assumption. 


class Rat:
	""" A rat caught in a maze. """
	def __init__(self, name, row, column):
		self.symbol = name
		self.row = row
		self.col = column
		self.num_sprouts_eaten = 0
	
	
	def set_location(self, row, col):
		self.row = row
		self.col = col


	def eat_sprout(self):
		self.num_sprouts_eaten += 1


	def __str__(self):
		return '%s at (%d, %d) ate %d sprouts.' % (self.symbol, self.row, self.col, self.num_sprouts_eaten)		


class Maze:
	""" A 2D maze. """
	def __init__(self, map, rat_1, rat_2):
		self.maze = map
		self.rat_1 = rat_1
		self.rat_2 = rat_2
		# TODO find a pythonic way to do this: list comprehension or filter?
		num_of_sprouts = 0
		for i in range(len(map)):
			for j in range(len(map[i])):
				if SPROUT == map[i][j]:
					num_of_sprouts += 1
		
		self.num_sprouts_left = num_of_sprouts


	def is_wall(self, row, col):
		if self.get_character(row, col) == WALL:
			return True
		else:
			return False


	def get_character(self, row, col):
		''' 
		If there is a rat there, return the symbol of it. 
		Remember the assumption: Maze.maze contains only HALLs, WALLs and SPROUTs. 
		'''
		if self.rat_1.row == row and self.rat_1.col == col:
			return self.rat_1.symbol # if both rats are on the same spot, the first one gets displayed always!
		elif self.rat_2.row == row and self.rat_2.col == col:
			return self.rat_2.symbol
		else:
			return self.maze[row][col]
		# if the maze could contain rats as well, then a simple return self.maze[row][col] would be enough


	def move(self, rat, vertical, horizontal):
		''' 
		Handles the movements of rats, according to the assumption.
		Checks if there is a wall and a sprout in the new position.
		'''
		new_position = (rat.row + vertical, rat.col + horizontal)
		if not self.is_wall(new_position[0], new_position[1]): # check if new_position is valid

			### The following code is taken care from the rat-race.redraw() method
			### Find which rat this is and compare it with the position of the other one
#			if self.rat_1 == rat:
#				if self.rat_2.row == rat.row and self.rat_2.col == rat.col:
#					self.maze[rat.row][rat.col] = self.rat_2.symbol # leave the other rat there
#				else: # leave a HALL behind
#					self.maze[rat.row][rat.col] = HALL
#			else: # it's the other way around
#				if self.rat_1.row == rat.row and self.rat_1.col == rat.col:
#					self.maze[rat.row][rat.col] = self.rat_1.symbol
#				else:
#					self.maze[rat.row][rat.col] = HALL
				
			# move rat to new position
			rat.set_location(new_position[0], new_position[1])

			if self.maze[rat.row][rat.col] == SPROUT: # is there a SPROUT in the new position - do not use get_character here because it will return the rat symbol - stupid requirement for get_character
				rat.eat_sprout()
				self.maze[rat.row][rat.col] =  HALL # leave a HALL behind - and get_character will take care of the correct representation if a rat is there
				self.num_sprouts_left -= 1
			
#			self.maze[rat.row][rat.col] = rat.symbol # to update the maze - remember the assumption
			return True
		else:
			return False


	def __str__(self):
		string_maze = ''
		for i in range(len(self.maze)):
			for j in range(len(self.maze[i])):
				string_maze += self.get_character(i, j)
			string_maze += '\n'
		# If the maze contained the rats as well this would suffice:
		#for row in self.maze:
		#	string_maze += ''.join(row)
		#	string_maze += '\n'
		
		string_maze += str(self.rat_1) + '\n'
		string_maze += str(self.rat_2)
	
		return string_maze
