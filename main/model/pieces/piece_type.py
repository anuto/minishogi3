from enum import Enum

class piece_type(Enum):

    PAWN = "P"
    KING = "K"
    ROOK = "R"
    BISHOP = "B"
    GOLD_GENERAL = "G"
    SILVER_GENERAL = "S"
    DRAGON_KING = "D"
    DRAGON_HORSE = "H"

    def __new__(cls, value):
        
        # Check if the value is a valid enum value
        if value not in ["P", "K", "R", "B", "G", "S", "D", "H"]:
            raise ValueError(f"'{value}' is not a valid value for {cls.__name__} Enum")

        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    def __str__(self):
        return self.value

    def __lt__(self, other):
        if self.__class__ == other.__class__:
            return self.value < other.value

    def __gt__(self, other):
        if self.__class__ == other.__class__:
            return self.value > other.value