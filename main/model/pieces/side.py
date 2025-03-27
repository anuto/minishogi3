from enum import Enum

class side(Enum):

    TOP = "TOP"
    BOTTOM = "BOTTOM"

    def __new__(cls, value):
        
        # Check if the value is a valid enum value
        if value not in ["TOP", "BOTTOM"]:
            raise ValueError(f"'{value}' is not a valid value for {cls.__name__} Enum")

        obj = object.__new__(cls)
        obj._value_ = value
        return obj
