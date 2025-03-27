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
		self.setup_squares()

	def setup_pieces(self, side):
		return [
			king(side),
			gold_general(side),
			silver_general(side),
			bishop(side),
			rook(side),
			pawn(side)
		]

	def move_piece(self, start_square, end_square):
		piece = self.squares[start_square]

		if piece.get_side() == Side.TOP:
			comrade_pieces = self.top_squares
			enemy_pieces = self.bottom_squares

		elif piece.get_side() == Side.BOTTOM:
			comrade_pieces = self.bottom_squares
			enemy_pieces = self.top_squares

		else:
			error("piece side unknown: " + str(piece))

		# not consistent w how piece moves / in bounds
		if not piece.is_valid_move(end_square):
			error("invalid move. " + str(piece) + " cannot go to " + str(end_square))

		# illegal move
		if end_square in comrade_pieces:
			error("cannot move to a square you already occupy!")
		
		# capture
		if end_square in enemy_pieces:
			piece.move(end_square)

		else:
			piece.move(end_square)

			self.squares.pop(start_square)
			self.squares[end_square] = piece

	def get_squares(self):
		return self.squares

	def get_top_squares(self):
		return self.top_squares

	def get_bottom_squares(self):
		return self.bottom_squares

	def get_top_pieces(self):
		return self.top_pieces

	def get_bottom_pieces(self):
		return self.bottom_pieces

	def get_pieces(self):
		return self.top_pieces + self.bottom_pieces

	def setup_squares(self):
		self.top_squares = {}
		self.bottom_squares = {}
		self.squares = {}

		for piece in self.top_pieces:
			square = piece.get_square()
			self.top_squares[square] = piece
			self.squares[square] = piece

		for piece in self.bottom_pieces:
			square = piece.get_square()
			self.bottom_squares[square] = piece
			self.squares[square] = piece

