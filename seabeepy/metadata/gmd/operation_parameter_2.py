from dataclasses import dataclass
from seabeepy.metadata.gmd.operation_parameter_property_type import OperationParameterPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationParameter2(OperationParameterPropertyType):
    """
    gml:operationParameter is an association role to the operation parameter of
    which this is a value.
    """
    class Meta:
        name = "operationParameter"
        namespace = "http://www.opengis.net/gml"
