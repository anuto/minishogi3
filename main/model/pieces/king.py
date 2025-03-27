from .piece import *
from .piece_type import *

class king(piece):

	TOP_START_SQUARE = (4,0)
	BOTTOM_START_SQUARE = (0, 4)

	PIECE_TYPE = piece_type.KING

	def get_moves(self):
		return valid_moves([
			move_forward(self.square, self.side),
			move_forward_left(self.square, self.side),
			move_forward_right(self.square, self.side),
			move_left(self.square, self.side),
			move_right(self.square, self.side),
			move_backward(self.square, self.side),
			move_backward_left(self.square, self.side),
			move_backward_right(self.square, self.side)
		])
	def get_promotions(self):
		return []