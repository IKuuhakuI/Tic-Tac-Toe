from ticTacToe import Game

def main ():
	game = Game()
	inGame = True	

	print ("TIC TAC TOE")
	print ("-----------")


	while inGame:
		game.printBoard()

		print (game.currentTurn)

		isValid = False

		while not isValid: 
			x = input("X value: ")
			y = input("Y value: ")

			try:
				x = int (x)
				y = int (y)
				
				isValid = True

			except:
				print ("Invalid input!")

		game.play (x, y)

main()
