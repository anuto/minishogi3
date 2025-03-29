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
		self.setup_moves()

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

		else:
			raise Exception("[error] side unknown: " + str(side))

		if square in squares:
			squares[square].promote(piece_type)

		else:
			raise Exception(str(side) + " does not have a piece at " + str(square))


	def drop_piece(self, piece_type, square, side):
		if square in self.top_squares or square in self.bottom_squares:
			raise Exception("Cannot drop piece in ocupied square " + str(square))

		if side == side.TOP:
			pieces = self.top_squares
			enemy_squares = self.bottom_squares
			moves = self.top_moves
			captured_pieces = self.top_captured_pieces

		elif side == side.BOTTOM:
			pieces = self.bottom_squares
			enemy_squares = self.top_squares
			moves = self.bottom_moves
			captured_pieces = self.bottom_captured_pieces

		else:
			raise Exception("[error] side unknown: " + str(side))

		removed_piece = None

		for captured_piece in captured_pieces:

			if captured_piece.get_piece_type() == piece_type:
				captured_pieces.remove(captured_piece)
				removed_piece = captured_piece

				# in case there are duplicate captured pieces
				break

		if not removed_piece:
			raise Exception("[error] could not find captured piece of type " + str(piece_type))

		# todo: add drop restrictions

		removed_piece.drop(square)

		pieces[square] = removed_piece
		moves[square] = self.get_legal_moves_for_piece(removed_piece, pieces, enemy_squares)

		self.update_board(None, square, side)

	# moves the piece belonging to player of `side` from start_square
	# to end_square if valid. 
	# returns where the moved piece can be promoted or not
	def move_piece(self, start_square, end_square, side):
		if side == side.TOP:
			comrade_squares = self.top_squares
			comrade_moves = self.top_moves
			comrade_captured_pieces = self.top_captured_pieces

			enemy_squares = self.bottom_squares
			enemy_moves = self.bottom_moves

		elif side == side.BOTTOM:
			comrade_squares = self.bottom_squares
			comrade_moves = self.bottom_moves
			comrade_captured_pieces = self.bottom_captured_pieces

			enemy_squares = self.top_squares
			enemy_moves = self.top_moves

		else:
			raise Exception("piece side unknown")

		# invalid piece
		if start_square not in comrade_squares:
			raise Exception(str(start_square) + " not found for " + str(side))

		piece = comrade_squares[start_square]

		# not consistent w how piece moves / in bounds / legal
		if not self.is_legal_move(start_square, end_square, comrade_moves):
			raise Exception("invalid move. " + str(piece) + " cannot go to " + str(end_square))

		# capture
		if end_square in enemy_squares:
			captured_piece = enemy_squares[end_square]
			
			captured_piece.set_captured()
			comrade_captured_pieces.append(captured_piece)

			enemy_squares.pop(end_square)
			enemy_moves.pop(end_square)

		piece.move(end_square)

		comrade_squares.pop(start_square)
		comrade_squares[end_square] = piece

		comrade_moves.pop(start_square)
		comrade_moves[end_square] = self.get_legal_moves_for_piece(piece, comrade_squares, enemy_squares)

		self.update_board(start_square, end_square, side)

	def update_board(self, start_square, end_square, side):
		if side == side.TOP:
			comrade_moves = self.top_moves
			comrade_squares = self.top_squares

			enemy_moves = self.bottom_moves
			enemy_squares = self.bottom_squares

		elif side == side.BOTTOM:
			comrade_moves = self.bottom_moves
			comrade_squares = self.bottom_squares

			enemy_moves  = self.top_moves
			enemy_squares = self.top_squares

		else:
			raise Exception("[error] unknown side")

		self.update_board_by_side(comrade_squares, enemy_squares, comrade_moves, start_square, end_square)
		self.update_board_by_side(enemy_squares, comrade_squares, enemy_moves, start_square, end_square)

	def update_board_by_side(self, comrade_squares, enemy_squares, moves, start_square, end_square):
		for square in comrade_squares:

			piece = comrade_squares[square]

			valid_moves = piece.get_moves()
			valid_moves = [move for direction in valid_moves for move in direction]

			if start_square not in valid_moves and end_square not in valid_moves:
				break

			legal_moves = self.get_legal_moves_for_piece(piece, comrade_squares, enemy_squares)
			moves[square] = legal_moves

	def is_legal_move(self, start_square, end_square, directions):
		for direction in directions[start_square]:
			for move in direction:
				if end_square == move:
					return True

		return False

	def promotion_possible(self, start_square, end_square, side):
		if side == side.TOP:
			squares = self.get_top_squares()

		elif side == side.BOTTOM:
			squares = self.get_bottom_squares()

		else:
			raise Exception("[error] unrecognized side: " + side)

		piece = squares[end_square]
		promotions = piece.get_promotions()

		if not promotions:
			return False

		# promotions are valid from previous drops if they are moving within
		# or out of the promotion zone
		if side == side.TOP:
			return start_square[1] == 4 or end_square[1] == 4

		else:
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

	# self.top_squares / bottom_squares = {(square) => < PIECE >}
	def setup_squares(self, top_pieces, bottom_pieces):
		self.top_squares = self.setup_squares_by_side(top_pieces)
		self.bottom_squares = self.setup_squares_by_side(bottom_pieces)

	def setup_squares_by_side(self, pieces):
		squares_to_pieces = {}

		for piece in pieces:
			square = piece.get_square()
			squares_to_pieces[square] = piece

		return squares_to_pieces

	def setup_moves(self):
		self.top_moves = self.setup_moves_by_side(self.get_top_pieces(), self.top_squares, self.bottom_squares)
		self.bottom_moves = self.setup_moves_by_side(self.get_bottom_pieces(), self.bottom_squares, self.top_squares)

	def setup_moves_by_side(self, pieces, comrade_squares, enemy_squares):
		legal_moves = {}

		for piece in pieces:
			legal_moves_for_piece = self.get_legal_moves_for_piece(piece, comrade_squares, enemy_squares)
			legal_moves[piece.get_square()] = legal_moves_for_piece

		return legal_moves

	# returns directions[[squares in order from origin in that direction] ...]
	def get_legal_moves_for_piece(self, piece, comrade_squares, enemy_squares):
		legal_moves_for_piece = []
		directions = piece.get_moves()


		for direction in directions:
			moves = direction
			legal_moves_in_direction = []

			for move in moves:
				if move in comrade_squares:
					# can't move here because another piece occupies here
					break

				elif move in enemy_squares:
					# can't move past an enemy piece. Can capture but stop there then
					legal_moves_in_direction.append(move)
					break

				else:
					legal_moves_in_direction.append(move)

			if legal_moves_in_direction:
				legal_moves_for_piece.append(legal_moves_in_direction)

		return legal_moves_for_piece