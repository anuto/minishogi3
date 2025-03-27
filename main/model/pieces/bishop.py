from .piece import *
from .dragon_horse import *
from .piece_type import *

class bishop(piece):

	TOP_START_SQUARE = (1, 0)
	BOTTOM_START_SQUARE = (3, 4)

	PIECE_TYPE = piece_type.BISHOP

	def get_moves(self):
		if self.promoted_type:
			return dragon_horse.get_moves()
		else:
			return move_diagonally(self.square)

	def get_promotions(self):
		if self.promoted_type:
			return dragon_horse.get_promotions()
		else:
			return [piece_type.DRAGON_HORSE, piece_type.BISHOP]


