from dataclasses import dataclass
from seabeepy.metadata.gmd.coordinates_type import CoordinatesType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TupleList(CoordinatesType):
    """gml:CoordinatesType consists of a list of coordinate tuples, with each
    coordinate tuple separated by the ts or tuple separator (whitespace), and
    each coordinate in the tuple by the cs or coordinate separator (comma).

    The gml:tupleList encoding is effectively “band-interleaved”.
    """
    class Meta:
        name = "tupleList"
        namespace = "http://www.opengis.net/gml"
