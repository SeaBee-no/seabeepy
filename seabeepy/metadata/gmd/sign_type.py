from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml"


class SignType(Enum):
    """
    gml:SignType is a convenience type with values “+” (plus) and “-“ (minus).
    """
    VALUE = "-"
    VALUE_1 = "+"
