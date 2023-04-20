from dataclasses import dataclass
from seabeepy.metadata.gmd.abstract_coordinate_system_type import AbstractCoordinateSystemType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EllipsoidalCstype(AbstractCoordinateSystemType):
    class Meta:
        name = "EllipsoidalCSType"
