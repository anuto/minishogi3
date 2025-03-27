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

		top_pieces = self.setup_pieces(side.TOP)
		bottom_pieces = self.setup_pieces(side.BOTTOM)

		self.setup_squares(top_pieces, bottom_pieces)

		self.top_captured_pieces = []
		self.bottom_captured_pieces = []

	def setup_pieces(self, side):
		return [
			king(side),
			gold_general(side),
			silver_general(side),
			bishop(side),
			rook(side),
			pawn(side)
		]

	def promote(self, square, piece_type, side):
		if side == side.TOP:
			squares = self.top_squares

		elif side == side.BOTTOM:
			squares = self.bottom_squares

		if square in squares:
			squares[square].promote(piece_type)

		else:
			raise Exception(str(side) + " does not have a piece at " + str(square))


	# moves the piece belonging to player of `side` from start_square
	# to end_square if valid. 
	# returns where the moved piece can be promoted or not
	def move_piece(self, start_square, end_square, side):
		if side == side.TOP:
			comrade_pieces = self.top_squares
			enemy_pieces = self.bottom_squares
			comrade_captured_pieces = self.top_captured_pieces

		elif side == side.BOTTOM:
			comrade_pieces = self.bottom_squares
			enemy_pieces = self.top_squares
			comrade_captured_pieces = self.bottom_captured_pieces

		else:
			raise Exception("piece side unknown")

		# invalid piece
		if start_square not in comrade_pieces:
			raise Exception(str(start_square) + " not found for " + str(side))

		piece = comrade_pieces[start_square]

		# not consistent w how piece moves / in bounds
		if not piece.is_valid_move(end_square):
			raise Exception("invalid move. " + str(piece) + " cannot go to " + str(end_square))

		# illegal move
		if end_square in comrade_pieces:
			raise Exception("cannot move to a square you already occupy!")
		
		# capture
		if end_square in enemy_pieces:
			captured_piece = enemy_pieces[end_square]
			comrade_captured_pieces.append(captured_piece)
			enemy_pieces.pop(end_square)

		piece.move(end_square)
		comrade_pieces.pop(start_square)
		comrade_pieces[end_square] = piece

	def promotion_possible(self, start_square, end_square, side):
		if side == side.TOP:
			return start_square[1] == 4 or end_square[1] == 4

		elif side == side.BOTTOM:
			return start_square[1] == 0 or end_square[1] == 0

	# returns {square (x, y) => piece } for both players
	def get_squares(self):
		return self.top_squares | self.bottom_squares

	# returns {square (x, y) => piece } for top player
	def get_top_squares(self):
		return self.top_squares

	# returns {square (x, y) => piece } for top player
	def get_bottom_squares(self):
		return self.bottom_squares

	# returns pieces belonging to top player as []
	def get_top_pieces(self):
		return list(self.top_squares.values())

	# returns pieces belonging to bot player as []
	def get_bottom_pieces(self):
		return list(self.bottom_squares.values())

	# returns pieces belonging to either players as []
	def get_pieces(self):
		return self.get_top_pieces() + self.get_bottom_pieces()

	# returns pieces captured by top player as []
	def get_top_captured_pieces(self):
		return self.top_captured_pieces

	# returns pieces captured by bottom player as []
	def get_bottom_captured_pieces(self):
		return self.bottom_captured_pieces

	def setup_squares(self, top_pieces, bottom_pieces):
		self.top_squares = {}
		self.bottom_squares = {}

		for piece in top_pieces:
			square = piece.get_square()
			self.top_squares[square] = piece

		for piece in bottom_pieces:
			square = piece.get_square()
			self.bottom_squares[square] = piece

