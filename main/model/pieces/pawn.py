from .piece import *
from .piece_type import *

class pawn(piece):

	TOP_START_SQUARE = (4, 1)
	BOTTOM_START_SQUARE = (0, 3)

	PIECE_TYPE = piece_type.PAWN

	def get_moves(self):
		return valid_moves([move_forward(self.square, self.side)])

	def get_promotions(self):
		return [piece_type.GOLD_GENERAL, piece_type.SILVER_GENERAL]


