import pytest

from main.model.pieces.side import *
from main.model.pieces.pawn import *

# massive TODO
class TestBoard:

    def top_promote_logic_correct(self):
    	pass
    	
    # def top_promote_logic_correct(self):
    #     test_pawn = pawn(side.TOP)

    #     top_promote_zone = []

    #     for x in range(0, 5):
    #         top_promote_zone.append((x, 4))

    #     for square in top_promote_zone:
    #         test_pawn.move(square)
    #         if not test_pawn.is

    #     not_top_promote_zone = []
    #     for y in range(0, 4):
    #         for x in range(0, 5):
    #             top_promote_zone.append((x, y))


    def test_top_cannot_place_on_square_with_comrade_piece(self):
        pass

    def test_bottom_cannot_place_on_square_with_comrade_piece(self):
        pass

    def test_top_cannot_place_on_square_with_enemy_piece(self):
        pass

    def test_bottom_cannot_place_on_square_with_enemy_piece(self):
        pass

    def test_top_cannot_drop_last_row(self):
        pass

    def test_bottom_cannot_drop_last_row(self):
        pass

    def test_top_cannot_drop_on_same_file_as_other_pawn(self):
        pass

    def test_bottom_cannot_drop_on_same_file_as_other_pawn(self):
        pass

    def test_top_cannot_drop_checkmate(self):
        pass

    def test_bottom_cannot_drop_checkmate(self):
        pass