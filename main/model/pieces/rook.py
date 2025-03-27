from .piece import *
from .dragon_king import *
from .piece_type import *

class rook(piece):

	TOP_START_SQUARE = (0, 0)
	BOTTOM_START_SQUARE = (4, 4)

	PIECE_TYPE = piece_type.ROOK

	def get_moves(self):
		if self.promoted_type:
			return dragon_king.get_moves()
		else:
			return move_orthogonally(self.square)

	def get_promotions(self):
		if self.promoted_type:
			return dragon_king.get_promotions()
		else:
			return [piece_type.DRAGON_KING, piece_type.ROOK]


