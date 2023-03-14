from dataclasses import dataclass
from seabeepy.metadata.gmd.operation_property_type import OperationPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationRef(OperationPropertyType):
    class Meta:
        name = "operationRef"
        namespace = "http://www.opengis.net/gml"
