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
			comrade_squares = self.top_squares
			enemy_squares = self.bottom_squares
			moves = self.top_moves
			captured_pieces = self.top_captured_pieces

		elif side == side.BOTTOM:
			comrade_squares = self.bottom_squares
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

		if piece_type == piece_type.PAWN:
			self.validate_legal_pawn_drop(square, comrade_squares, side)

		removed_piece.drop(square)

		comrade_squares[square] = removed_piece
		moves[square] = self.get_legal_moves_for_piece(removed_piece, comrade_squares, enemy_squares)

		self.update_board(None, square, side)

	def validate_legal_pawn_drop(self, drop_square, squares, side):
		self.validate_not_last_row(drop_square, side)
		self.validate_no_other_pawn_same_file(squares, drop_square)
		self.validate_not_pawn_checkmate(side, drop_square)

	# may need to implement differently unfortunately here and for a generic
	# is_checkmate. Because this encodes a pawn down, whereas the generic is a
	# reflection of the board state.

	# they can probably share code though, similar in concept.
	def validate_not_pawn_checkmate(self, side, drop_square):
		enemy_side = self.get_enemy_side(side)

		# is it blockable? freebie. checkmate by pawn drop can never be 
		# blocked since it only attacks directly in front

		# can the attacker be captured? 

		# ! a problem. if it is just the king, then we need to make sure the escape
		# pieces are also not defended..... sigh.
		defending_pieces = self.pieces_threatening_square(enemy_side, drop_square)

		if defending_pieces:
			if len(defending_pieces) > 1:
				return

			lone_defender_type =  defending_pieces[0].get_piece_type()
			if lone_defender_type != piece_type.KING:
				return

			else:
				drop_square_defended = self.pieces_threatening_square(side, drop_square)
				if not drop_square_defended:
					return

		# can the king move?
		king_moves = self.moves_for_piece(self.get_squares_by_side(enemy_side), self.get_moves_by_side(enemy_side), piece_type.KING)

		# need to know if those spots are also threatened. pawn drop won't attack
		# any other squares but the current one. ie can't check the king and threaten
		# another
		for king_move in king_moves:
			if not self.pieces_threatening_square(side, king_move) \
					and king_move != drop_square:

				return

		raise Exception("pawns cannot drop checkmate! class uprising time.")

	def get_moves_by_side(self, side):
		if side == side.TOP:
			return self.top_moves

		elif side == side.BOTTOM:
			return self.bottom_moves

		else:
			raise Exception("[error] side not recognized: " + str(side))

	def get_squares_by_side(self, side):
		if side == side.TOP:
			return self.top_squares

		elif side == side.BOTTOM:
			return self.bottom_squares

		else:
			raise Exception("[error] side not recognized: " + str(side))		
				
	def get_enemy_side(self, side):
		if side == side.TOP:
			return side.BOTTOM

		elif side == side.BOTTOM:
			return side.TOP

		else:
			raise Exception("[error] side not recognized: " + str(side))

	def pieces_threatening_square(self, side, square):
		moves = self.get_moves_by_side(side)
		squares = self.get_squares_by_side(side)

		threats = []

		for piece in moves:
			directions = moves[piece]

			if self.moves_contains_move(directions, square):
				threats.append(squares[piece])

		return threats

	# accepts moves as a [[]], a list of moves in a list of different directions
	# returns if the given move is included
	def moves_contains_move(self, directions, square):
		for direction in directions:
			for move in direction:
				if move == square:
					return True

		return False

	def moves_for_piece(self, squares, moves, piece_type):
		for square in squares:
			piece = squares[square]

			if piece_type == piece_type:
				return moves[square]
	
	def validate_no_other_pawn_same_file(self, squares, drop_square):
		for square in squares:

			if square[0] == drop_square[0]:
				piece = squares[square]

				if piece.get_piece_type() == piece_type.PAWN:
					raise Exception("cannot place pawn at " + str(drop_square) + \
						". Already a pawn at " + str(square))

	def validate_not_last_row(self, square, side):
		if self.is_last_row(square, side):
			raise Exception("pawns cannot be placed on the last row!!")

	def is_last_row(self, square, side):
		if side == side.TOP:
			return square[1] == 4

		elif side == side.BOTTOM:
			return square[1] == 0

		else:
			raise Exception("[error] side not rexognized " + str(side))

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
		if not self.moves_contains_move(comrade_moves[start_square], end_square):
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
		return self.is_last_row(start_square, side) or self.is_last_row(end_square, side)

	# returns {square (x, y) => piece } for both players
	def get_squares(self):
		return {**self.top_squares, **self.bottom_squares}

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