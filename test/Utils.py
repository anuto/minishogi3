import pytest
import collections

class Utils:


    def assert_lists_equal(expected, actual):
        assert sorted(expected) == sorted(actual)

    def assert_lists_of_lists_equal(expected, actual):
        sorted_expected = []
        for lists in expected:
            sorted_expected.append(tuple(sorted(lists)))

        sorted_actual = []
        for lists in actual:
            sorted_actual.append(tuple(sorted(lists)))

        sorted_expected = sorted(sorted_expected)
        sorted_actual = sorted(sorted_actual)

        assert sorted_expected == sorted_actual
        # assert collections.Counter(sorted_expected) == collections.Counter(sorted_actual)


    def assert_can_only_move_to_expected_squares(piece, expected_moves):
        # get all squares
        unreachable_squares = []

        for y in range(0, 5):
            for x in range(0, 5):
                unreachable_squares.append((x, y))

        # validate we can move where we should be able to
        for direction in expected_moves:
            for move in direction:
                assert piece.can_move_to(move)
                unreachable_squares.remove(move)

        # validate we can't move where we shouldn't be able to
        for square in unreachable_squares:
            assert not piece.can_move_to(square)
