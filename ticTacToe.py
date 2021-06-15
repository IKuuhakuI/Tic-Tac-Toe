class Game ():
	def __init__ (self):
		self.board = [[0,0,0],[0,0,0],[0,0,0]] # Empty board
		self.currentTurn = 1 # 1 = X / -1 = O

	def switchTurn (self):
		if self.currentTurn == 1:
			self.currentTurn = -1

		else:
			self.currentTurn = 1

	def checkInput (self, xValue, yValue):
		minX = minY = 0
		maxX = maxY = len(self.board)
		
		if (maxX > xValue >= minX and maxY > yValue >= minY):
			if (self.board[xValue][yValue] == 0):
				return True
			else:
				print ("This position has already been chosen")

				return False

		print ("Invalid input!")
		print ("X and Y values must be between 1 and 3")
		
		return False

	def play (self, xInput, yInput):
		xValue = xInput - 1
		yValue = yInput -1

		isValid = self.checkInput (xValue, yValue)

		if (isValid):
			self.board[xValue][yValue] = self.currentTurn

			self.switchTurn()

	def printBoard (self):
		for x in range (0, len(self.board)):
			for y in range (0, len(self.board)):
				if (self.board[x][y] == 1):
					value = 'X'
				elif (self.board[x][y] == -1):
					value = 'O'
				else:
					value = ' '
				print (value, end='')
			
				if y != len(self.board) - 1:
					print (" | ", end='')

			if x != len(self.board) - 1:
				print ()
				print ("__________\n")

		print ("\n")
