from game_controller import *
from ascii_view import *
from model.pieces.side import *
from model.pieces.piece_type import *

def main():
	# basic_test()
	pawn_place_test()

def pawn_place_test():
	game = game_controller()

	print_board_state(game)

	game.move_piece((0, 0), (0, 3), side.TOP)
	print_board_state(game)

	# our back row ok test. this should pass
	# game.drop_piece(piece_type.PAWN, (0, 0), side.TOP)

	# same file test: this should fail. 
	# game.drop_piece(piece_type.PAWN, (4, 2), side.TOP)

	# setup for checkmate and backrow test

	game.move_piece((0, 3), (1, 3), side.TOP)
	print_board_state(game)

	game.move_piece((1, 4), (2, 3), side.BOTTOM)
	print_board_state(game)

	game.move_piece((1, 3), (2, 3), side.TOP)
	print_board_state(game)

	game.move_piece((2, 3), (1, 3), side.TOP)
	print_board_state(game)

	game.drop_piece(piece_type.GOLD_GENERAL, (2, 3), side.TOP)
	print_board_state(game)

	# frontest test. this should fail.
	# game.drop_piece(piece_type.PAWN, (1, 4), side.TOP)

	game.move_piece((2, 4), (2, 3), side.BOTTOM)
	print_board_state(game)

	# checkmate test. this should fail.
	game.drop_piece(piece_type.PAWN, (0, 3), side.TOP)
	print_board_state(game)

def basic_test():
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

	game.drop_piece(piece_type.ROOK, (1, 2),  side.BOTTOM)

	print_board_state(game)

	game.drop_piece(piece_type.ROOK, (4, 1), side.TOP)

	print_board_state(game)

	game.move_piece((0, 4), (0, 3), side.BOTTOM)

	print_board_state(game)

	# [x] throws exception, which is good
	# game.move_piece((2, 1), (0, 3), side.TOP)

	game.move_piece((2, 1), (1, 2), side.TOP)

	print_board_state(game)

if __name__ == '__main__':
	main()