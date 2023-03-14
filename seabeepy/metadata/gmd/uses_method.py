from dataclasses import dataclass
from seabeepy.metadata.gmd.operation_method_property_type import OperationMethodPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesMethod(OperationMethodPropertyType):
    class Meta:
        name = "usesMethod"
        namespace = "http://www.opengis.net/gml"
