from .piece import *
from .piece_type import *

class dragon_horse(piece):

	PIECE_TYPE = piece_type.DRAGON_HORSE

	def get_moves(self):
		bishop_moves = move_diagonally(self.square)
		return bishop_moves + valid_moves([
			move_forward(self.square, self.side),
			move_left(self.square, self.side),
			move_right(self.square, self.side),
			move_backward(self.square, self.side)
		])

	def get_promotions(self):
		return []

