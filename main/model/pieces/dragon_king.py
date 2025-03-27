from .piece import *
from .piece_type import *

class dragon_king(piece):

	PIECE_TYPE = piece_type.DRAGON_KING

	def get_moves(self):
		rook_moves = move_orthogonally(self.square)
		rook_moves + valid_moves([
			move_forward_left(self.square, self.side),
			move_forward_right(self.square, self.side),
			move_backward_left(self.square, self.side),
			move_backward_right(self.square, self.side)
		])

	def get_promotions(self):
		return []


