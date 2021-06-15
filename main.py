from ticTacToe import Game

def main ():
	game = Game()
	inGame = True

	print ("TIC TAC TOE")
	print ("-----------")


	game.printBoard()

	while inGame:

		print (game.currentTurn)

		isValid = False

		while not isValid:
			print () 
			x = input("X value: ")
			y = input("Y value: ")
			print ()

			try:
				x = int (x)
				y = int (y)
				
				isValid = True

			except:
				print ("Invalid input!")

		winner = game.play (x, y)

		game.printBoard()

		if winner != 0:

			if (game.getWinner() == 1):
				print ('Winner: X')

			elif (game.getWinner() == -1):
				print ('Winner: O')

			inGame = False

main()
