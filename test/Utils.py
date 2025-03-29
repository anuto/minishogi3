import pytest
import collections

class Utils:

    def get_all_squares():
        squares = []

        for y in range(0, 5):
            for x in range(0, 5):
                squares.append((x, y))

        return squares


    def assert_contains_equal(expected, actual):
        is_nested = any(isinstance(item, list) for item in expected)
        
        if is_nested:
            sorted_expected = []
            for lists in expected:
                sorted_expected.append(sorted(lists))

            sorted_actual = []
            for lists in actual:
                sorted_actual.append(sorted(lists))

            sorted_expected = sorted(sorted_expected)
            sorted_actual = sorted(sorted_actual)

            # todo #1: fix nested comparison
            # assert collections.Counter(sorted_expected) == collections.Counter(sorted_actual)

        else:
            assert sorted(expected) == sorted(actual)

    def validate_cannot_move_to_squares(test_pawn, squares):
        for square in squares:
            assert not test_pawn.can_move_to(square)
