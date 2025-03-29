import unittest
import collections
# move to point to outer directory
from os import sys,path
FILE_PATH = path.abspath(__file__)
intended_path = FILE_PATH
for layer in range(4):
    intended_path = path.dirname(intended_path)
sys.path.append(intended_path)

from main.model.pieces.side import *
from main.model.pieces.pawn import *


class pawn_test(unittest.TestCase):

    def test_initialize_top_pawn(self):
        test_pawn = pawn(side.TOP)

        assert test_pawn.get_piece_type() == piece_type.PAWN
        assert test_pawn.get_square() == (4, 1)
        assert test_pawn.get_moves() == [[(4, 2)]]
        assert test_pawn.get_side() == side.TOP
        
        promotions = test_pawn.get_promotions()
        expected_promotions = [piece_type.SILVER_GENERAL, piece_type.GOLD_GENERAL]

        assert collections.Counter(expected_promotions) == collections.Counter(expected_promotions)

        assert test_pawn.can_move_to((4,2))

        all_squares = self.get_all_squares()

        # the one square it should be able to go to...
        all_squares.remove((4, 2))

        for square in all_squares:
            assert not test_pawn.can_move_to(square)

        assert not test_pawn.is_captured()

    def test_initialize_bottom_pawn(self):
        test_pawn = pawn(side.BOTTOM)

        assert test_pawn.get_piece_type() == piece_type.PAWN
        assert test_pawn.get_square() == (0, 3)
        assert test_pawn.get_moves() == [[(0, 2)]]
        assert test_pawn.get_side() == side.BOTTOM
        
        promotions = test_pawn.get_promotions()
        expected_promotions = [piece_type.SILVER_GENERAL, piece_type.GOLD_GENERAL]

        assert collections.Counter(expected_promotions) == collections.Counter(expected_promotions)

        assert test_pawn.can_move_to((0, 2))

        all_squares = self.get_all_squares()

        # the one square it should be able to go to...
        all_squares.remove((0, 2))

        for square in all_squares:
            assert not test_pawn.can_move_to(square)

        assert not test_pawn.is_captured()

    def test_move_pawn(self):
        pass

    def test_drop_pawn(self):
        pass

    def test_captured(self):
        pass

    def test_change_side(self):
        pass

    def test_promote_to_silver_general(self):
        pass

    def test_promote_to_gold_general(self):
        pass

    def get_all_squares(self):
        squares = []

        for y in range(0, 5):
            for x in range(0, 5):
                squares.append((x, y))

        return squares

if __name__ == '__main__':
    unittest.main()