def draw_board(game):
	squares = game.get_squares()

	for y in range(0, 5):
		for x in range(0, 5):

			if (x, y) in squares.keys():
				print(squares[(x, y)], end = '')

			else:
				print("[ ]", end = '')

		print()

def print_initial_state(game):
	print("~~~~~~~~~~~~~")

	print("top:")
	top_pieces = game.get_top_pieces()
	print_pieces(top_pieces)

	print()

	print("bottom:")
	bottom_pieces = game.get_bottom_pieces()
	print_pieces(bottom_pieces)

	print()

	draw_board(game)

	print("~~~~~~~~~~~~~")

def print_pieces(pieces):
	for piece in pieces:
		print(piece)
		print("location: " + str(piece.get_square()))
		print("moves: " + str(piece.get_moves()))

		promotions = piece.get_promotions()
		for promotion in promotions:
			print("promotable: " + str(promotion))
		print()
		