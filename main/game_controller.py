from model.board import board
from model.pieces.side import *
from model.pieces.piece_type import *

class game_controller(object):

	def __init__(self):
		self.board = board()

	def is_game_over(self):
		pieces = self.board.get_pieces()

		for piece in pieces:
			if piece.get_piece_type() == piece_type.KING:
				return False

		return True

	def move_piece(self, start_square, end_square, side):
		self.board.move_piece(start_square, end_square, side)

	def get_squares(self):
		return self.board.get_squares()

	def get_pieces(self):
		return self.board.get_pieces()

	def get_top_captured_pieces(self):
		return self.board.get_top_captured_pieces()

	def get_bottom_captured_pieces(self):
		return self.board.get_bottom_captured_pieces()

	def get_top_pieces(self):
		return self.board.get_top_pieces()

	def get_bottom_pieces(self):
		return self.board.get_bottom_pieces()