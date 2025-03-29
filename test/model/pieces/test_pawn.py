import pytest
import collections

from main.model.pieces.side import *
from main.model.pieces.pawn import *

class TestPawn():

    def test_initialize_top_pawn(self, utils):
        test_pawn = pawn(side.TOP)

        assert test_pawn.get_piece_type() == piece_type.PAWN
        assert test_pawn.get_square() == (4, 1)
        assert test_pawn.get_moves() == [[(4, 2)]]
        assert test_pawn.get_side() == side.TOP
        
        promotions = test_pawn.get_promotions()
        expected_promotions = [piece_type.SILVER_GENERAL, piece_type.GOLD_GENERAL]

        self.assert_contains_equal(promotions, expected_promotions)
        assert test_pawn.can_move_to((4,2))

        all_squares = utils.get_all_squares()

        # the one square it should be able to go to...
        all_squares.remove((4, 2))

        self.validate_cannot_move_to_squares(test_pawn, all_squares)

        assert not test_pawn.is_captured()

    def test_initialize_bottom_pawn(self, utils):
        test_pawn = pawn(side.BOTTOM)

        assert test_pawn.get_piece_type() == piece_type.PAWN
        assert test_pawn.get_square() == (0, 3)
        assert test_pawn.get_moves() == [[(0, 2)]]
        assert test_pawn.get_side() == side.BOTTOM
        
        promotions = test_pawn.get_promotions()
        expected_promotions = [piece_type.SILVER_GENERAL, piece_type.GOLD_GENERAL]

        assert collections.Counter(expected_promotions) == collections.Counter(expected_promotions)

        assert test_pawn.can_move_to((0, 2))

        all_squares = utils.get_all_squares()

        # the one square it should be able to go to...
        all_squares.remove((0, 2))

        self.validate_cannot_move_to_squares(test_pawn, all_squares)

        assert not test_pawn.is_captured()

    def test_move_bottom_pawn(self, utils):
        test_pawn = pawn(side.BOTTOM)

        test_pawn.move((0, 2))

        assert test_pawn.get_square() == (0, 2)
        assert test_pawn.get_moves() == [[(0, 1)]]
        assert test_pawn.can_move_to((0, 1))

        all_squares = utils.get_all_squares()

        # the one square it should be able to go to...
        all_squares.remove((0, 1))

        for square in all_squares:
            assert not test_pawn.can_move_to(square)

    def test_move_top_pawn(self, utils):
        test_pawn = pawn(side.TOP)

        test_pawn.move((4, 2))

        assert test_pawn.get_square() == (4, 2)
        assert test_pawn.get_moves() == [[(4, 3)]]
        assert test_pawn.can_move_to((4, 3))

        all_squares = utils.get_all_squares()

        # the one square it should be able to go to...
        all_squares.remove((4, 3))

        for square in all_squares:
            assert not test_pawn.can_move_to(square)

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

    def test_promote_top_pawn_to_silver_general(self):
        test_pawn = pawn(side.TOP)

        test_pawn.promote(piece_type.SILVER_GENERAL)

        assert test_pawn.get_piece_type() == piece_type.SILVER_GENERAL
        assert test_pawn.get_piece_type() != piece_type.PAWN
        assert test_pawn.get_piece_type() != piece_type.GOLD_GENERAL

        expected_moves = []

    def test_promote_bottom_pawn_to_silver_general(self):
        pass

    def test_promote_top_pawn_to_gold_general(self):
        pass

    def test_promote_bottom_pawn_to_gold_general(self):
        pass

    def test_promote_top_pawn_to_silver_general_to_gold_general(self):
        pass

    def test_promote_bottom_pawn_to_silver_general_to_gold_general(self):
        pass

    def test_top_gold_general_captured(self):
        pass

    def test_bottom_gold_general_captured(self):
        pass

    def test_top_silver_general_captured(self):
        pass

    def test_bottom_silver_general_captured(self):
        pass

    def test_double_promoted_top_gold_general_captured(self):
        pass

    def test_double_promoted_bottom_gold_general_captured(self):
        pass

    def test_drop_pawn(self):
        pass


    # ~ helpers ~
    def assert_contains_equal(self, collection_1, collection_2):
        assert collections.Counter(collection_1) == collections.Counter(collection_2)

    def validate_cannot_move_to_squares(self, test_pawn, squares):
        for square in squares:
            assert not test_pawn.can_move_to(square)

if __name__ == '__main__':
    unittest.main()