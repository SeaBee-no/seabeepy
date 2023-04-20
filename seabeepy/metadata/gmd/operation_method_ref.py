from dataclasses import dataclass
from seabeepy.metadata.gmd.operation_method_property_type import OperationMethodPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationMethodRef(OperationMethodPropertyType):
    class Meta:
        name = "operationMethodRef"
        namespace = "http://www.opengis.net/gml"
