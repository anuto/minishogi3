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
		return [move]

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

# returns [] of moves lists as [] in each direction
# ex. [[(left), (left)], [(bottom)]]
def move_orthogonally(square):
	moves = []

	# left
	left = []
	for x in range(square[0] - 1,-1, -1):
		left.append((x, square[1]))

	if left:
		moves.append(left)

	# right
	right = []
	for x in range(square[0] + 1, 5):
		right.append((x, square[1]))

	if right:
		moves.append(right)

	# up
	up = []
	for y in range(square[1] - 1, -1, -1):
		up.append((square[0], y))

	if up:
		moves.append(up)

	# down
	down = []
	for y in range(square[1] + 1, 5):
		down.append((square[0], y))

	if down:
		down.append(down)

	return moves

# returns [] of moves lists as [] in each direction
# ex. [[(upper left 1), (upper left 2)], [(bottom right)]]
def move_diagonally(square):
	moves = []


	# upper left
	x = square[0] - 1
	y = square[1] - 1
	upper_left = []

	while (x >= 0 and y >= 0):
		upper_left.append((x, y))
		x -= 1
		y -= 1

	if upper_left:
		moves.append(upper_left)

	# upper right
	x = square[0] + 1
	y = square[1] - 1
	upper_right = []

	while (x <= 4 and y >= 0):
		upper_right.append((x, y))
		x += 1
		y -= 1

	if upper_right:
		moves.append(upper_right)

	# bottom left
	x = square[0] - 1
	y = square[1] + 1

	bottom_left = []

	while (x >= 0 and y <= 4):
		bottom_left.append((x, y))
		x -= 1
		y += 1

	if bottom_left:
		moves.append(bottom_left)

	# bottom right
	x = square[0] + 1
	y = square[1] + 1

	bottom_right = []

	while (x <= 4 and y <= 4):
		bottom_right.append((x, y))
		x += 1
		y += 1

	if bottom_right:
		moves.append(bottom_right)
	return moves