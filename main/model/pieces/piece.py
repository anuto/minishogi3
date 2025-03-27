from .side import *
from .move_utils import *

class piece(object):

    def __init__(self, side, square = None):
        self.side = side

        if square:
            self.square = square

        elif side == side.TOP:
            self.square = self.TOP_START_SQUARE

        elif side == side.BOTTOM:
            self.square = self.BOTTOM_START_SQUARE
        else:
            raise Exception("invalid side: " + str(side))

    def move(self, new_square):
        self.square = new_square

    def is_valid_move(self, new_square):
        return new_square in self.get_moves()

    def get_moves(self):
        raise Exception("[error] default piece behavior not overridden")

    def get_promotions(self):
        raise Exception("[error] default promotions not overridden")

    def get_piece_type(self):
        return self.PIECE_TYPE

    def get_square(self):
        return self.square

    def get_side(self):
        return self.side

    def __str__(self):
        return "[" + str(self.PIECE_TYPE)+ "]"
