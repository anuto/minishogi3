from .side import *
from .move_utils import *

class piece(object):

    def __init__(self, side, square = None):
        self.side = side
        self.promoted_type = None

        if square:
            self.square = square

        elif side == side.TOP:
            self.square = self.TOP_START_SQUARE

        elif side == side.BOTTOM:
            self.square = self.BOTTOM_START_SQUARE
        else:
            raise Exception("invalid side: " + str(side))

    def move(self, new_square):
        current_square = self.square
        self.square = new_square

        if self.side == side.TOP:
            if current_square[1] == 4 or new_square[1] == 4:
                return True
            else:
                return False

        elif self.side == side.BOTTOM:
            if current_square[1] == 0 or new_square[1] == 0:
                return True
            else: 
                return False

        else:
            raise Exception("invalid side: " + str(self.side))

    def promote(self, piece_type):
        self.promoted_type = piece_type

    def is_valid_move(self, new_square):
        return new_square in self.get_moves()

    def get_moves(self):
        raise Exception("[error] default piece behavior not overridden")

    def get_promotions(self):
        raise Exception("[error] default promotions not overridden")

    def get_piece_type(self):
        if self.promoted_type:
            return self.promoted_type
        else:
            return self.PIECE_TYPE

    def get_square(self):
        return self.square

    def get_side(self):
        return self.side

    def __str__(self):
        return "[" + str(self.get_piece_type()) + "]"
