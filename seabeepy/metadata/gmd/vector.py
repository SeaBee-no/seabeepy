from dataclasses import dataclass
from seabeepy.metadata.gmd.vector_type import VectorType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Vector(VectorType):
    class Meta:
        name = "vector"
        namespace = "http://www.opengis.net/gml"
