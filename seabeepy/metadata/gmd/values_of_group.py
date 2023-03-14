from dataclasses import dataclass
from seabeepy.metadata.gmd.operation_parameter_group_property_type import OperationParameterGroupPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ValuesOfGroup(OperationParameterGroupPropertyType):
    class Meta:
        name = "valuesOfGroup"
        namespace = "http://www.opengis.net/gml"
