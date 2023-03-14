from dataclasses import dataclass
from seabeepy.metadata.gmd.operation_method_property_type import OperationMethodPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Method(OperationMethodPropertyType):
    """
    gml:method is an association role to the operation method used by a
    coordinate operation.
    """
    class Meta:
        name = "method"
        namespace = "http://www.opengis.net/gml"
