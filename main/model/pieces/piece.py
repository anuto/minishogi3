from .side import *
from .move_utils import *

class piece(object):

    def __init__(self, side):
        self.side = side
        self.promoted_type = None

        if side == side.TOP:
            self.square = self.TOP_START_SQUARE

        elif side == side.BOTTOM:
            self.square = self.BOTTOM_START_SQUARE
        else:
            raise Exception("invalid side: " + str(side))

    def move(self, new_square):
        current_square = self.square
        self.square = new_square

    def drop(self, square):
        if self.square:
            raise Exception("[error] piece is already on the board?")

        self.square = square

    def set_captured(self):
        self.promoted_type = None
        self.change_side()
        self.square = None

    def change_side(self):
        if self.side == side.TOP:
            self.side = side.BOTTOM

        elif self.side == side.BOTTOM:
            self.side = side.TOP

    def promote(self, piece_type):
        self.promoted_type = piece_type

    # this just means valid in terms of the piece, not in the context of the board.
    def can_move_to(self, new_square):
        directions = self.get_moves()

        for direction in directions:
            for move in direction:
                if new_square == move:
                    return True

        return False

    def get_moves(self):
        raise Exception("[error] default piece behavior not overridden")

    def get_promotions(self):
        raise Exception("[error] default promotions not overridden")

    def get_piece_type(self):
        if self.promoted_type:
            return self.promoted_type
        else:
            return self.PIECE_TYPE

    # really necessary due to asymmetry of movement against a static board
    def get_side(self):
        return self.side
        
    def get_square(self):
        return self.square

    def __str__(self):
        return "[" + str(self.get_piece_type()) + "]"
