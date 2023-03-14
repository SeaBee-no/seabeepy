from dataclasses import dataclass
from seabeepy.metadata.gmd.concatenated_operation_property_type import ConcatenatedOperationPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ConcatenatedOperationRef(ConcatenatedOperationPropertyType):
    class Meta:
        name = "concatenatedOperationRef"
        namespace = "http://www.opengis.net/gml"
