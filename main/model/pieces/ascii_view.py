from .game import game

def draw_board(game):
	squares = game.get_squares()

	for x in range(0, 5):
		for y in range(0, 5):
			piece =  squares[x, y]
			if piece:
				print(piece)
			else:
				print "[ ] "