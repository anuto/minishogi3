from .side import *
from .move_utils import *

class piece(object):

    def __init__(self, side, square = None):
        self.side = side

        if square:
            self.square = square

        elif side == Side.TOP:
            self.square = self.TOP_START_SQUARE

        else: # bottom side
            self.square = self.BOTTOM_START_SQUARE


    def get_moves(self):
        return ["[error] default piece behavior not overridden"]

    def get_promotions(self):
        return ["[error] default promotions not overridden"]

    def get_square(self):
        return self.square

    def get_side(self):
        return self.side

    def __str__(self):
        return "[" + str(self.PIECE_TYPE)+ "]"
