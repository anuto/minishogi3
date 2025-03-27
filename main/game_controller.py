from model.board import board
from model.pieces.side import *
from model.pieces.piece_type import *

class game_controller(object):

	def __init__(self):
		self.board = board()
		self.winner = None

	def is_game_over(self):
		top_captured_pieces = self.board.get_top_captured_pieces()
		bottom_captured_pieces = self.board.get_bottom_captured_pieces() 

		for piece in top_captured_pieces:
			if piece.get_piece_type() == piece_type.KING:
				self.winner = side.TOP
				return True

		for piece in bottom_captured_pieces:
			if piece.get_piece_type() == piece_type.KING:
				self.winner = side.BOTTOM
				return True

		return False

	def promotion_possible(self, start_square, end_square, side):
		return self.board.promotion_possible(start_square, end_square, side)

	def promote(self, square, piece_type, side):
		self.board.promote(square, piece_type, side)

	# returns promotable or not. but shouldn't. fix in a moment TODO
	def move_piece(self, start_square, end_square, side):
		return self.board.move_piece(start_square, end_square, side)

	def get_squares(self):
		return self.board.get_squares()

	def get_piece(self, square):
		squares = self.get_squares()
		return squares[square]

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