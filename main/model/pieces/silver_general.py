from .piece import *
from .gold_general import *
from .piece_type import *

class silver_general(piece):

	TOP_START_SQUARE = (2, 0,)
	BOTTOM_START_SQUARE = (2, 4)

	PIECE_TYPE = piece_type.SILVER_GENERAL

	def get_moves(self):
		if self.promoted_type:
			return gold_general.get_moves()
		else:
			return valid_moves([
				move_forward(self.square, self.side),
				move_forward_left(self.square, self.side),
				move_forward_right(self.square, self.side),
				move_backward_left(self.square, self.side),
				move_backward_right(self.square, self.side)
			])


	def get_promotions(self):
		if self.promoted_type:
			return gold_general.get_promotions()
		else:
			return [piece_type.GOLD_GENERAL, piece_type.SILVER_GENERAL]