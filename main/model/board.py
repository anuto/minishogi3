from .pieces.piece import *

from .pieces.king import *
from .pieces.gold_general import *
from .pieces.silver_general import *
from .pieces.bishop import *
from .pieces.rook import *
from .pieces.pawn import *

from .pieces.side import *

class board(object):

	def __init__(self):

		self.top_pieces = self.setup_pieces(Side.TOP)
		self.bottom_pieces = self.setup_pieces(Side.BOTTOM)

	def setup_pieces(self, side):
		return [
			king(side),
			gold_general(side),
			silver_general(side),
			bishop(side),
			rook(side),
			pawn(side)
		]

	def get_top_pieces(self):
		return self.top_pieces

	def get_bottom_pieces(self):
		return self.bottom_pieces

	def get_pieces(self):
		return self.top_pieces + self.bottom_pieces