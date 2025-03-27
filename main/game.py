from game_controller import *

def main():

	game = game_controller()
	
	print("~~~~~~~~~~~~~")

	print("top:")
	top_pieces = game.get_top_pieces()
	process_pieces(top_pieces)

	print()

	print("bottom:")
	bottom_pieces = game.get_bottom_pieces()
	process_pieces(bottom_pieces)

	print("~~~~~~~~~~~~~")

def process_pieces(pieces):
	for piece in pieces:
		print(piece)
		print(piece.get_moves())

		promotions = piece.get_promotions()
		for promotion in promotions:
			print("promotable: " + str(promotion))
		print()
		
if __name__ == '__main__':
	main()