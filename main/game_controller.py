import sys
from model.board import board

class game_controller(object):

	def __init__(self):
		self.board = board()

	def move_piece(self, start_square, end_square):
		self.board.move_piece(start_square, end_square)

	def get_squares(self):
		return self.board.get_squares()

	def get_pieces(self):
		return self.board.get_pieces()

	def get_top_pieces(self):
		return self.board.get_top_pieces()

	def get_bottom_pieces(self):
		return self.board.get_bottom_pieces()