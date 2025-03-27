from .piece import *
from .piece_type import *

class bishop(piece):

	TOP_START_SQUARE = (1, 0)
	BOTTOM_START_SQUARE = (3, 4)

	PIECE_TYPE = piece_type.BISHOP

	def get_moves(self):
		return move_diagonally(self.square)

	def get_promotions(self):
		return [piece_type.DRAGON_HORSE]


