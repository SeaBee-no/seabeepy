from dataclasses import dataclass
from seabeepy.metadata.gmd.operation_parameter_property_type import OperationParameterPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationParameterRef(OperationParameterPropertyType):
    class Meta:
        name = "operationParameterRef"
        namespace = "http://www.opengis.net/gml"
