from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml"


class DegreesTypeDirection(Enum):
    N = "N"
    E = "E"
    S = "S"
    W = "W"
    VALUE = "+"
    VALUE_1 = "-"
