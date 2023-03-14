from dataclasses import dataclass
from seabeepy.metadata.gmd.operation_method_type import OperationMethodType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationMethod(OperationMethodType):
    """gml:OperationMethod is a method (algorithm or procedure) used to perform
    a coordinate operation.

    Most operation methods use a number of operation parameters,
    although some coordinate conversions use none. Each coordinate
    operation using the method assigns values to these parameters. The
    generalOperationParameter elements are an unordered list of
    associations to the set of operation parameters and parameter groups
    used by this operation method.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
