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

        unreachable_squares = utils.get_all_squares()

        for direction in expected_moves:
            for move in direction:
                assert test_gold_general.can_move_to(move)
                unreachable_squares.remove(move)

        utils.validate_cannot_move_to_squares(test_gold_general, unreachable_squares)

        assert not test_gold_general.is_captured()

    # TODO: :)
    # def test_initialize_bottom_pawn(self, utils):
    #     test_pawn = pawn(side.BOTTOM)

    #     assert test_pawn.get_piece_type() == piece_type.GOLD_GENERAL
    #     assert test_pawn.get_square() == (0, 3)
    #     assert test_pawn.get_moves() == [[(0, 2)]]
    #     assert test_pawn.get_side() == side.BOTTOM
        
    #     promotions = test_pawn.get_promotions()
    #     expected_promotions = [piece_type.SILVER_GENERAL, piece_type.GOLD_GENERAL]

    #     assert collections.Counter(expected_promotions) == collections.Counter(expected_promotions)

    #     assert test_pawn.can_move_to((0, 2))

    #     all_squares = utils.get_all_squares()

    #     # the one square it should be able to go to...
    #     all_squares.remove((0, 2))

    #     utils.validate_cannot_move_to_squares(test_pawn, all_squares)

    #     assert not test_pawn.is_captured()

    # def test_move_bottom_pawn(self, utils):
    #     test_pawn = pawn(side.BOTTOM)

    #     test_pawn.move((0, 2))

    #     assert test_pawn.get_square() == (0, 2)
    #     assert test_pawn.get_moves() == [[(0, 1)]]
    #     assert test_pawn.can_move_to((0, 1))

    #     all_squares = utils.get_all_squares()

    #     # the one square it should be able to go to...
    #     all_squares.remove((0, 1))

    #     for square in all_squares:
    #         assert not test_pawn.can_move_to(square)

    # def test_move_top_pawn(self, utils):
    #     test_pawn = pawn(side.TOP)

    #     test_pawn.move((4, 2))

    #     assert test_pawn.get_square() == (4, 2)
    #     assert test_pawn.get_moves() == [[(4, 3)]]
    #     assert test_pawn.can_move_to((4, 3))

    #     all_squares = utils.get_all_squares()

    #     # the one square it should be able to go to...
    #     all_squares.remove((4, 3))

    #     for square in all_squares:
    #         assert not test_pawn.can_move_to(square)

    # def test_captured_by_bottom(self):
    #     test_pawn = pawn(side.TOP)
    #     assert test_pawn.get_side() == side.TOP
    #     assert test_pawn.get_square()
    #     assert test_pawn.get_piece_type() == piece_type.PAWN

    #     test_pawn.set_captured()
    #     assert test_pawn.get_side() == side.BOTTOM
    #     assert not test_pawn.get_square()
    #     assert test_pawn.get_piece_type() == piece_type.PAWN

    # def test_captured_by_top(self):
    #     test_pawn = pawn(side.BOTTOM)
    #     assert test_pawn.get_side() == side.BOTTOM
    #     assert test_pawn.get_square()
    #     assert test_pawn.get_piece_type() == piece_type.PAWN

    #     test_pawn.set_captured()
    #     assert test_pawn.get_side() == side.TOP
    #     assert not test_pawn.get_square()
    #     assert test_pawn.get_piece_type() == piece_type.PAWN

    # def test_drop_top_gold_general(self):
    #     test_pawn = pawn(side.TOP)

    #     test_pawn.set_captured()
    #     test_pawn.drop((2, 2))

    #     assert test_pawn.get_square() == (2, 2)
    #     assert test_pawn.get_side() == side.BOTTOM

    # def test_drop_bottom_gold_general(self):
    #     test_pawn = pawn(side.BOTTOM)

    #     test_pawn.set_captured()
    #     test_pawn.drop((2, 2))

    #     assert test_pawn.get_square() == (2, 2)
    #     assert test_pawn.get_side() == side.TOP

if __name__ == '__main__':
    unittest.main()