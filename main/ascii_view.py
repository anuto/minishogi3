# brief info
def print_board_state(game):
	print_board(game)
	print_captured_pieces(game)
	if game.is_game_over():
		print("game over.")

# all info
def print_full_state(game):

	print("top:")
	top_pieces = game.get_top_pieces()
	print_pieces(top_pieces)
	print_top_captured_pieces(game)

	print()

	print("bottom:")
	bottom_pieces = game.get_bottom_pieces()
	print_pieces(bottom_pieces)
	print_bottom_captured_pieces(game)

	print()

	print_board(game)

# board
def print_board(game):
	print("~~~~~~~~~~~~~")

	squares = game.get_squares()

	for y in range(0, 5):
		for x in range(0, 5):

			if (x, y) in squares.keys():
				print(squares[(x, y)], end = '')

			else:
				print("[ ]", end = '')

		print()
	print("~~~~~~~~~~~~~")

# pieces 
def print_pieces(pieces):
	for piece in pieces:
		print(piece)
		print("location: " + str(piece.get_square()))
		print("moves: " + str(piece.get_moves()))

		promotions = piece.get_promotions()
		for promotion in promotions:
			print("promotable: " + str(promotion))
		print()

# captured pieces
def print_captured_pieces(game):
	print_top_captured_pieces(game)
	print_bottom_captured_pieces(game)

def print_top_captured_pieces(game):
	top_captured_pieces = game.get_top_captured_pieces()

	print("top captured pieces: ", '')
	for piece in top_captured_pieces:
		print(str(piece), ', ')
	print()

def print_bottom_captured_pieces(game):
	bottom_captured_pieces = game.get_bottom_captured_pieces()

	print("bottom captured pieces: ", '')
	for piece in bottom_captured_pieces:
		print(str(piece), ', ')
	print()