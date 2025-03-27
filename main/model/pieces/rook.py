from .piece import *
from .piece_type import *

class rook(piece):

	TOP_START_SQUARE = (0, 0)
	BOTTOM_START_SQUARE = (4, 4)

	PIECE_TYPE = piece_type.ROOK

	def get_moves(self):
		return move_orthogonally(self.square)

	def get_promotions(self):
		return [piece_type.DRAGON_KING]


