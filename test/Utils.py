import pytest

class Utils:

    @staticmethod
    def get_all_squares():
        squares = []

        for y in range(0, 5):
            for x in range(0, 5):
                squares.append((x, y))

        return squares