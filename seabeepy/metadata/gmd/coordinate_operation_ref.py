from dataclasses import dataclass
from seabeepy.metadata.gmd.pass_through_operation_type import CoordinateOperationPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateOperationRef(CoordinateOperationPropertyType):
    class Meta:
        name = "coordinateOperationRef"
        namespace = "http://www.opengis.net/gml"
