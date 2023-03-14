from dataclasses import dataclass
from seabeepy.metadata.gmd.abstract_general_operation_parameter_property_type import AbstractGeneralOperationParameterPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class IncludesParameter(AbstractGeneralOperationParameterPropertyType):
    class Meta:
        name = "includesParameter"
        namespace = "http://www.opengis.net/gml"
