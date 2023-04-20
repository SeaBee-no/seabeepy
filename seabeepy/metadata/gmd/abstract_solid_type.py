from dataclasses import dataclass
from seabeepy.metadata.gmd.abstract_geometric_primitive_type import AbstractGeometricPrimitiveType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractSolidType(AbstractGeometricPrimitiveType):
    """gml:AbstractSolidType is an abstraction of a solid to support the
    different levels of complexity.

    The solid may always be viewed as a geometric primitive, i.e. is
    contiguous.
    """
