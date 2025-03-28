from game_controller import *
from ascii_view import *
from model.pieces.side import *
from model.pieces.piece_type import *

def main():

	game = game_controller()
	
	print_full_state(game)

	game.move_piece((0, 3), (0, 2), side.BOTTOM)

	print_board_state(game)

	game.move_piece((4, 1), (4, 2), side.TOP)

	print_board_state(game)

	game.move_piece((4, 4), (4, 2), side.BOTTOM)

	print_board_state(game)

	game.move_piece((3, 0), (4, 1), side.TOP)

	print_board_state(game)

	game.move_piece((0, 2), (0, 1), side.BOTTOM)

	print_board_state(game)

	game.move_piece((4, 1), (4, 2), side.TOP)

	print_board_state(game)

	game.move_piece((0, 1), (0, 0), side.BOTTOM)

	if (game.promotion_possible((0, 1), (0, 0), side.BOTTOM)):
		promotion = prompt_promotion(game, (0, 0))
		game.promote((0, 0), promotion, side.BOTTOM)

	print_board_state(game)

	game.move_piece((1, 0), (2, 1), side.TOP)

	print_board_state(game)

	game.drop_piece((1, 2), piece_type.ROOK, side.BOTTOM)

	print_board_state(game)

	game.move_piece((2, 1), (0, 3), side.TOP)

	print_board_state(game)

if __name__ == '__main__':
	main()