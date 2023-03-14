from dataclasses import dataclass
from seabeepy.metadata.gmd.abstract_geometry_type import AbstractGeometryType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeometricPrimitiveType(AbstractGeometryType):
    """gml:AbstractGeometricPrimitiveType is the abstract root type of the
    geometric primitives.

    A geometric primitive is a geometric object that is not decomposed
    further into other primitives in the system. All primitives are
    oriented in the direction implied by the sequence of their
    coordinate tuples.
    """
