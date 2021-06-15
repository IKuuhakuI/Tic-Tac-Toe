from ticTacToe import Game

def main ():
	game = Game()

	print ("TIC TAC TOE")
	print (game.board)

	print (game.currentTurn)
	game.play (1, 1)
main()
