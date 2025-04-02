import pytest
import collections

from main.model.pieces.side import *
from main.model.pieces.gold_general import *

class TestGoldGeneral():

    def test_initialize_top_gold_general(self, utils):
        test_gold_general = gold_general(side.TOP)

        expected_moves = [[(2, 1)], [(3, 1)], [(4, 1)], [(2, 0)], [(4, 0)]]

        assert test_gold_general.get_piece_type() == piece_type.GOLD_GENERAL
        assert test_gold_general.get_square() == (3, 0)
        utils.assert_lists_of_lists_equal(expected_moves, test_gold_general.get_moves())
        assert test_gold_general.get_side() == side.TOP
        
        promotions = test_gold_general.get_promotions()
        expected_promotions = []

        utils.assert_lists_equal(promotions, expected_promotions)

        utils.assert_can_only_move_to_expected_squares(test_gold_general, expected_moves)

        assert not test_gold_general.is_captured()

    def test_initialize_bottom_gold_general(self, utils):
        test_gold_general = gold_general(side.BOTTOM)

        expected_moves = [[(0, 3)], [(1, 3)], [(2, 3)], [(0, 4)], [(2, 4)]]

        assert test_gold_general.get_piece_type() == piece_type.GOLD_GENERAL
        assert test_gold_general.get_square() == (1, 4)
        utils.assert_lists_of_lists_equal(expected_moves, test_gold_general.get_moves())
        assert test_gold_general.get_side() == side.BOTTOM
        
        promotions = test_gold_general.get_promotions()
        expected_promotions = []

        utils.assert_lists_equal(promotions, expected_promotions)

        utils.assert_can_only_move_to_expected_squares(test_gold_general, expected_moves)

        assert not test_gold_general.is_captured()

    def test_move_top_gold_general(self, utils):
        test_gold_general = gold_general(side.TOP)

        test_gold_general.move((3, 1))

        expected_moves = [[(2, 2)], [(3, 2)], [(4, 2)], [(2, 1)], [(4, 1)], [(3, 0)]]

        assert test_gold_general.get_square() == (3, 1)

        utils.assert_lists_of_lists_equal(expected_moves, test_gold_general.get_moves())
        utils.assert_can_only_move_to_expected_squares(test_gold_general, expected_moves)


    def test_move_bottom_gold_general(self, utils):
        test_gold_general = gold_general(side.BOTTOM)

        test_gold_general.move((1, 3))

        expected_moves = [[(0, 2)], [(1, 2)], [(2, 2)], [(0, 3)], [(2, 3)], [(1, 4)]]

        assert test_gold_general.get_square() == (1, 3)

        utils.assert_lists_of_lists_equal(expected_moves, test_gold_general.get_moves())
        utils.assert_can_only_move_to_expected_squares(test_gold_general, expected_moves)


    def test_captured_by_bottom(self):
        test_gold_general = gold_general(side.TOP)
        assert test_gold_general.get_side() == side.TOP
        assert test_gold_general.get_square()
        assert test_gold_general.get_piece_type() == piece_type.GOLD_GENERAL

        test_gold_general.set_captured()
        assert test_gold_general.get_side() == side.BOTTOM
        assert not test_gold_general.get_square()
        assert test_gold_general.get_piece_type() == piece_type.GOLD_GENERAL

    def test_captured_by_top(self):
        test_gold_general = gold_general(side.BOTTOM)
        assert test_gold_general.get_side() == side.BOTTOM
        assert test_gold_general.get_square()
        assert test_gold_general.get_piece_type() == piece_type.GOLD_GENERAL

        test_gold_general.set_captured()
        assert test_gold_general.get_side() == side.TOP
        assert not test_gold_general.get_square()
        assert test_gold_general.get_piece_type() == piece_type.GOLD_GENERAL

    def test_drop_top_gold_general(self):
        test_gold_general = gold_general(side.TOP)

        test_gold_general.set_captured()
        test_gold_general.drop((2, 2))

        assert test_gold_general.get_square() == (2, 2)
        assert test_gold_general.get_side() == side.BOTTOM

    def test_drop_bottom_gold_general(self):
        test_gold_general = gold_general(side.BOTTOM)

        test_gold_general.set_captured()
        test_gold_general.drop((2, 2))

        assert test_gold_general.get_square() == (2, 2)
        assert test_gold_general.get_side() == side.TOP

if __name__ == '__main__':
    unittest.main()