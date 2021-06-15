from ticTacToe import Game

def main ():
	game = Game()
	inGame = True

	print ("TIC TAC TOE")
	print ("-----------")


	game.printBoard()

	while inGame:

		if game.currentTurn == 1:
			print ("X turn")
		else:
			print ("O turn")

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

			elif (game.getWinner() == 2):
				print ('Draw')

			inGame = False

main()
