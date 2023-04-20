from dataclasses import dataclass
from seabeepy.metadata.gmd.abstract_general_operation_parameter_type import AbstractGeneralOperationParameterType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationParameterType(AbstractGeneralOperationParameterType):
    pass
