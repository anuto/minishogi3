from .side import *
from .move_utils import *

# removes Nones
def valid_moves(moves):
	return [move for move in moves if move is not None]

# within board boundaries. 
# ideally board logic, but necessary evil to cap search space for infinite
# movement pieces like rook / bishop
def is_valid(square):
	return square[0] >= 0 and \
		square[0] <= 4 and \
		square[1] >= 0 and \
		square[1] <= 4

def move(top_square, bottom_square, side):
	if side == side.TOP:
		move = top_square

	elif side == side.BOTTOM:
		move = bottom_square

	if is_valid(move):
		return move

	else:
		return None

def move_left(square, side):
	top_square = (square[0] + 1, square[1])
	bottom_square = (square[0] - 1, square[1])
	return move(top_square, bottom_square, side)

def move_right(square, side):
	top_square = (square[0] - 1, square[1])
	bottom_square = (square[0] + 1, square[1])
	return move(top_square, bottom_square, side)

def move_forward(square, side):
	top_square = (square[0], square[1] + 1)
	bottom_square = (square[0], square[1] - 1)
	return move(top_square, bottom_square, side)

def move_backward(square, side):
	top_square = (square[0], square[1] - 1)
	bottom_square = (square[0], square[1] + 1)
	return move(top_square, bottom_square, side)

def move_forward_left(square, side):
	top_square = (square[0] + 1, square[1] + 1)
	bottom_square = (square[0] - 1, square[1] - 1)
	return move(top_square, bottom_square, side)

def move_forward_right(square, side):
	top_square = (square[0] - 1, square[1] + 1)
	bottom_square = (square[0] + 1, square[1] - 1)
	return move(top_square, bottom_square, side)

def move_backward_left(square, side):
	top_square = (square[0] + 1, square[1] - 1)
	bottom_square = (square[0] - 1, square[1] + 1)
	return move(top_square, bottom_square, side)

def move_backward_right(square, side):
	top_square = (square[0] - 1, square[1] - 1)
	bottom_square = (square[0] + 1, square[1] + 1)
	return move(top_square, bottom_square, side)

def move_orthogonally(square):
	moves = []

	# left
	for x in range(0, square[0]):
		moves.append((x, square[1]))

	# right
	for x in range(square[0] + 1, 5):
		moves.append((x, square[1]))

	# up
	for y in range(0, square[1]):
		moves.append((square[0], y))

	# down
	for y in range(square[1] + 1, 5):
		moves.append((square[0], y))

	return moves

def move_diagonally(square):
	moves = []

	# upper left
	x = square[0] - 1
	y = square[1] - 1

	while (x >= 0 and y >= 0):
		moves.append((x, y))
		x -= 1
		y -= 1

	# upper right
	x = square[0] + 1
	y = square[1] - 1

	while (x <= 4 and y >= 0):
		moves.append((x, y))
		x += 1
		y -= 1

	# bottom left
	x = square[0] - 1
	y = square[1] + 1

	while (x >= 0 and y <= 4):
		moves.append((x, y))
		x -= 1
		y += 1

	# bottom right
	x = square[0] + 1
	y = square[1] + 1

	while (x <= 4 and y <= 4):
		moves.append((x, y))
		x += 1
		y += 1

	return moves