import sys
sys.path.append('../')
from components.pieces.piece import piece

class board(object):
	def __init__(self):
		self.top_pieces = []
		self.bottom_pieces = []

		one_piece = piece([0,2], "TOP")
		return