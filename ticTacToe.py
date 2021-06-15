class Game ():
	def __init__ (self):
		self.board = [[0,0,0],[0,0,0],[0,0,0]] # Empty board
		self.currentTurn = 1 # 1 = X / -1 = O
		self.winner = 0

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

			self.checkWinner()

			if self.winner == 0:
				self.switchTurn()

		return self.winner

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

	def checkWinner (self):
		idx = 0

		while self.winner == 0 and idx < len(self.board):
			if self.board[idx][0] == self.board[idx][1] == self.board[idx][2]:
				self.winner = self.board[idx][0]

			elif self.board[0][idx] == self.board[1][idx] == self.board[2][idx]:
				self.winner = self.board[0][idx]

			idx += 1

		if (self.board[0][0] == self.board[1][1] == self.board[2][2] or\
		self.board[0][2] == self.board[1][1] == self.board[2][0]) and\
		self.winner == 0:
			self.winner = self.board[1][1]

	def getWinner (self):
		return self.winner
