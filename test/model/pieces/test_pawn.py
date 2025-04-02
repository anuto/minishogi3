import pytest
import collections

from main.model.pieces.side import *
from main.model.pieces.pawn import *

class TestPawn():

    def test_initialize_top_pawn(self, utils):
        test_pawn = pawn(side.TOP)

        expected_moves = [[(4, 2)]]

        assert test_pawn.get_piece_type() == piece_type.PAWN
        assert test_pawn.get_square() == (4, 1)
        utils.assert_lists_of_lists_equal(expected_moves, test_pawn.get_moves())
        assert test_pawn.get_side() == side.TOP
        
        promotions = test_pawn.get_promotions()
        expected_promotions = [piece_type.SILVER_GENERAL, piece_type.GOLD_GENERAL]

        utils.assert_lists_equal(promotions, expected_promotions)

        utils.assert_can_only_move_to_expected_squares(test_pawn, expected_moves)

        assert not test_pawn.is_captured()

    def test_initialize_bottom_pawn(self, utils):
        test_pawn = pawn(side.BOTTOM)

        expected_moves = [[(0, 2)]]

        assert test_pawn.get_piece_type() == piece_type.PAWN
        assert test_pawn.get_square() == (0, 3)
        utils.assert_lists_of_lists_equal(expected_moves, test_pawn.get_moves())
        assert test_pawn.get_side() == side.BOTTOM
        
        promotions = test_pawn.get_promotions()
        expected_promotions = [piece_type.SILVER_GENERAL, piece_type.GOLD_GENERAL]

        assert collections.Counter(expected_promotions) == collections.Counter(expected_promotions)

        utils.assert_lists_equal(promotions, expected_promotions)

        utils.assert_can_only_move_to_expected_squares(test_pawn, expected_moves)

        assert not test_pawn.is_captured()

    def test_move_bottom_pawn(self, utils):
        test_pawn = pawn(side.BOTTOM)

        test_pawn.move((0, 2))

        expected_moves = [[(0, 1)]]

        assert test_pawn.get_square() == (0, 2)
        utils.assert_lists_of_lists_equal(expected_moves, test_pawn.get_moves())

        utils.assert_can_only_move_to_expected_squares(test_pawn, expected_moves)

        assert not test_pawn.is_captured()

    def test_move_top_pawn(self, utils):
        test_pawn = pawn(side.TOP)

        test_pawn.move((4, 2))

        expected_moves = [[(4, 3)]]

        assert test_pawn.get_square() == (4, 2)
        utils.assert_lists_of_lists_equal(expected_moves, test_pawn.get_moves())

        utils.assert_can_only_move_to_expected_squares(test_pawn, expected_moves)

        assert not test_pawn.is_captured()

    def test_change_top_to_bottom(self):
        test_pawn = pawn(side.TOP)
        assert test_pawn.get_side() == side.TOP

        test_pawn.change_side()

        assert test_pawn.get_side() == side.BOTTOM

    def test_change_bottom_to_top(self):
        test_pawn = pawn(side.BOTTOM)
        assert test_pawn.get_side() == side.BOTTOM

        test_pawn.change_side()

        assert test_pawn.get_side() == side.TOP

    def test_captured_by_bottom(self):
        test_pawn = pawn(side.TOP)
        assert test_pawn.get_side() == side.TOP
        assert test_pawn.get_square()
        assert test_pawn.get_piece_type() == piece_type.PAWN

        test_pawn.set_captured()
        assert test_pawn.get_side() == side.BOTTOM
        assert not test_pawn.get_square()
        assert test_pawn.get_piece_type() == piece_type.PAWN

    def test_captured_by_top(self):
        test_pawn = pawn(side.BOTTOM)
        assert test_pawn.get_side() == side.BOTTOM
        assert test_pawn.get_square()
        assert test_pawn.get_piece_type() == piece_type.PAWN

        test_pawn.set_captured()
        assert test_pawn.get_side() == side.TOP
        assert not test_pawn.get_square()
        assert test_pawn.get_piece_type() == piece_type.PAWN

    def test_promote_top_pawn_to_silver_general(self, utils):
        test_pawn = pawn(side.TOP)

        test_pawn.promote(piece_type.SILVER_GENERAL)

        assert test_pawn.get_piece_type() == piece_type.SILVER_GENERAL
        assert test_pawn.get_piece_type() != piece_type.PAWN
        assert test_pawn.get_piece_type() != piece_type.GOLD_GENERAL

        expected_moves = [[(4, 2)], [(3, 2)], [(3, 0)]]
        utils.assert_lists_of_lists_equal(expected_moves, test_pawn.get_moves())

        test_pawn.move((3, 2))

        assert test_pawn.get_square() == (3, 2)
        expected_moves = [[(2, 3)], [(3, 3)], [(4, 3)], [(2, 1)], [(4, 1)]]
        utils.assert_lists_of_lists_equal(expected_moves, test_pawn.get_moves())

    def test_promote_bottom_pawn_to_silver_general(self, utils):
        test_pawn = pawn(side.BOTTOM)

        test_pawn.promote(piece_type.SILVER_GENERAL)

        assert test_pawn.get_piece_type() == piece_type.SILVER_GENERAL
        assert test_pawn.get_piece_type() != piece_type.PAWN
        assert test_pawn.get_piece_type() != piece_type.GOLD_GENERAL

        expected_moves = [[(1, 4)], [(0, 2)], [(1, 2)]] 
        utils.assert_lists_of_lists_equal(expected_moves, test_pawn.get_moves())

        test_pawn.move((1, 2))

        assert test_pawn.get_square() == (1, 2)
        expected_moves = [[(0, 1)], [(1, 1)], [(2, 1)], [(0, 3)], [(2, 3)]]  
        utils.assert_lists_of_lists_equal(expected_moves, test_pawn.get_moves())

    def test_promote_top_pawn_to_gold_general(self, utils):
        test_pawn = pawn(side.TOP)

        test_pawn.promote(piece_type.GOLD_GENERAL)

        assert test_pawn.get_piece_type() == piece_type.GOLD_GENERAL
        assert test_pawn.get_piece_type() != piece_type.SILVER_GENERAL
        assert test_pawn.get_piece_type() != piece_type.PAWN

        expected_moves = [[(4, 0)], [(3, 1)], [(3, 2)], [(4, 2)]]
        utils.assert_lists_of_lists_equal(expected_moves, test_pawn.get_moves())

        test_pawn.move((3, 2))

        assert test_pawn.get_square() == (3, 2)
        expected_moves = [[(2, 3)], [(3, 3)], [(4, 3)], [(2, 2)], [(4, 2)], [(3, 1)]]
        utils.assert_lists_of_lists_equal(expected_moves, test_pawn.get_moves())

    def test_promote_bottom_pawn_to_gold_general(self, utils):
        test_pawn = pawn(side.BOTTOM)

        test_pawn.promote(piece_type.GOLD_GENERAL)

        assert test_pawn.get_piece_type() == piece_type.GOLD_GENERAL
        assert test_pawn.get_piece_type() != piece_type.SILVER_GENERAL
        assert test_pawn.get_piece_type() != piece_type.PAWN

        expected_moves = [[(0, 2)], [(1, 2)], [(1, 3)], [(0, 4)]]
        utils.assert_lists_of_lists_equal(expected_moves, test_pawn.get_moves())

        test_pawn.move((1, 2))

        assert test_pawn.get_square() == (1, 2)
        expected_moves = [[(0, 1)], [(1, 1)], [(2, 1)], [(0, 2)], [(2, 2)], [(1, 3)]]
        utils.assert_lists_of_lists_equal(expected_moves, test_pawn.get_moves())
    
    def test_promote_top_pawn_to_silver_general_to_gold_general(self, utils):
        test_pawn = pawn(side.BOTTOM)

        test_pawn.promote(piece_type.SILVER_GENERAL)
        test_pawn.promote(piece_type.GOLD_GENERAL)

        assert test_pawn.get_piece_type() == piece_type.GOLD_GENERAL
        assert test_pawn.get_piece_type() != piece_type.SILVER_GENERAL
        assert test_pawn.get_piece_type() != piece_type.PAWN

        expected_moves = [[(0, 2)], [(1, 2)], [(1, 3)], [(0, 4)]]
        utils.assert_lists_of_lists_equal(expected_moves, test_pawn.get_moves())

        test_pawn.move((1, 2))

        assert test_pawn.get_square() == (1, 2)
        expected_moves = [[(0, 1)], [(1, 1)], [(2, 1)], [(0, 2)], [(2, 2)], [(1, 3)]]
        utils.assert_lists_of_lists_equal(expected_moves, test_pawn.get_moves())

    def test_promote_bottom_pawn_to_silver_general_to_gold_general(self, utils):
        test_pawn = pawn(side.BOTTOM)

        test_pawn.promote(piece_type.SILVER_GENERAL)
        test_pawn.promote(piece_type.GOLD_GENERAL)

        assert test_pawn.get_piece_type() == piece_type.GOLD_GENERAL
        assert test_pawn.get_piece_type() != piece_type.SILVER_GENERAL
        assert test_pawn.get_piece_type() != piece_type.PAWN

        expected_moves = [[(0, 2)], [(1, 2)], [(1, 3)], [(0, 4)]]
        utils.assert_lists_of_lists_equal(expected_moves, test_pawn.get_moves())

        test_pawn.move((1, 2))

        assert test_pawn.get_square() == (1, 2)
        expected_moves = [[(0, 1)], [(1, 1)], [(2, 1)], [(0, 2)], [(2, 2)], [(1, 3)]]
        utils.assert_lists_of_lists_equal(expected_moves, test_pawn.get_moves())

    def test_top_gold_general_captured(self):
        test_pawn = pawn(side.TOP)

        test_pawn.promote(piece_type.GOLD_GENERAL)
        test_pawn.set_captured()

        assert not test_pawn.get_square()
        assert test_pawn.get_piece_type() == piece_type.PAWN
        assert test_pawn.get_side() == side.BOTTOM

    def test_bottom_gold_general_captured(self):
        test_pawn = pawn(side.BOTTOM)

        test_pawn.promote(piece_type.GOLD_GENERAL)
        test_pawn.set_captured()

        assert not test_pawn.get_square()
        assert test_pawn.get_piece_type() == piece_type.PAWN
        assert test_pawn.get_side() == side.TOP

    def test_top_silver_general_captured(self):
        test_pawn = pawn(side.TOP)

        test_pawn.promote(piece_type.SILVER_GENERAL)
        test_pawn.set_captured()

        assert not test_pawn.get_square()
        assert test_pawn.get_piece_type() == piece_type.PAWN
        assert test_pawn.get_side() == side.BOTTOM

    def test_bottom_silver_general_captured(self):
        test_pawn = pawn(side.BOTTOM)

        test_pawn.promote(piece_type.SILVER_GENERAL)
        test_pawn.set_captured()

        assert not test_pawn.get_square()
        assert test_pawn.get_piece_type() == piece_type.PAWN
        assert test_pawn.get_side() == side.TOP

    def test_double_promoted_top_gold_general_captured(self):
        test_pawn = pawn(side.TOP)

        test_pawn.promote(piece_type.SILVER_GENERAL)
        test_pawn.promote(piece_type.GOLD_GENERAL)

        test_pawn.set_captured()

        assert not test_pawn.get_square()
        assert test_pawn.get_piece_type() == piece_type.PAWN
        assert test_pawn.get_side() == side.BOTTOM

    def test_double_promoted_bottom_gold_general_captured(self):
        test_pawn = pawn(side.BOTTOM)

        test_pawn.promote(piece_type.SILVER_GENERAL)
        test_pawn.promote(piece_type.GOLD_GENERAL)

        test_pawn.set_captured()

        assert not test_pawn.get_square()
        assert test_pawn.get_piece_type() == piece_type.PAWN
        assert test_pawn.get_side() == side.TOP

    def test_drop_top_pawn_basic(self):
        test_pawn = pawn(side.TOP)

        test_pawn.set_captured()
        test_pawn.drop((2, 2))

        assert test_pawn.get_square() == (2, 2)
        assert test_pawn.get_side() == side.BOTTOM

    def test_drop_bottom_pawn_basic(self):
        test_pawn = pawn(side.BOTTOM)

        test_pawn.set_captured()
        test_pawn.drop((2, 2))

        assert test_pawn.get_square() == (2, 2)
        assert test_pawn.get_side() == side.TOP

    def test_top_drop_captured_promoted_gold_general(self):
        test_pawn = pawn(side.BOTTOM)

        test_pawn.promote(piece_type.GOLD_GENERAL)
        test_pawn.set_captured()
        test_pawn.drop((2, 2))

        assert test_pawn.get_square() == (2, 2)
        assert test_pawn.get_side() == side.TOP
        assert test_pawn.get_piece_type() == piece_type.PAWN

    def test_bottom_drop_captured_promoted_gold_general(self):
        test_pawn = pawn(side.TOP)

        test_pawn.promote(piece_type.GOLD_GENERAL)
        test_pawn.set_captured()
        test_pawn.drop((2, 2))

        assert test_pawn.get_square() == (2, 2)
        assert test_pawn.get_side() == side.BOTTOM
        assert test_pawn.get_piece_type() == piece_type.PAWN

if __name__ == '__main__':
    unittest.main()