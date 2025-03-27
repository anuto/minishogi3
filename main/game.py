from game_controller import *
from ascii_view import *

def main():

	game = game_controller()
	
	print_initial_state(game)

	game.move_piece((0, 3), (0, 2))

	draw_board(game)

if __name__ == '__main__':
	main()