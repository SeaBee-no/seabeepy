from dataclasses import dataclass
from seabeepy.metadata.gmd.abstract_geometric_primitive_type import AbstractGeometricPrimitiveType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractSurfaceType(AbstractGeometricPrimitiveType):
    """gml:AbstractSurfaceType is an abstraction of a surface to support the
    different levels of complexity.

    A surface is always a continuous region of a plane.
    """
