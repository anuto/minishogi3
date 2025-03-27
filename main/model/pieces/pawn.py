from .piece import *
from .gold_general import *
from .silver_general import *
from .piece_type import *

class pawn(piece):

	TOP_START_SQUARE = (4, 1)
	BOTTOM_START_SQUARE = (0, 3)

	PIECE_TYPE = piece_type.PAWN

	def get_moves(self):
		if self.promoted_type == piece_type.GOLD_GENERAL:
			return gold_general.get_moves(self)

		elif self.promoted_type == piece_type.SILVER_GENERAL:
			return silver_general.get_moves(self)

		else:
			return valid_moves([move_forward(self.square, self.side)])

	def get_promotions(self):
		if self.promoted_type == piece_type.GOLD_GENERAL:
			return gold_general.get_promotions()

		elif self.promoted_type == piece_type.SILVER_GENERAL:
			return silver_general.get_promotions()

		else:
			return [piece_type.GOLD_GENERAL, piece_type.SILVER_GENERAL]


