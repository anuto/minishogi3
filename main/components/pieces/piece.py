import sys
sys.path.append('../')
from components.players.Side import Side

class piece(object):

    def __init__(self, start_square, side):
        self.square = start_square
        #self.side = Side.TOP

    def available_moves_from_spot(self):
        return ["[error] default piece behavior not overridden"]

    def promotions(self):
        return ["[error] default promotions not overridden"]


