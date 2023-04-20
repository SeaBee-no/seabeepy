from dataclasses import dataclass, field
from typing import List, Union
from seabeepy.metadata.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DoubleOrNilReasonTupleList:
    """gml:doubleOrNilReasonList consists of a list of gml:doubleOrNilReason
    values, each separated by a whitespace.

    The gml:doubleOrNilReason values are grouped into tuples where the
    dimension of each tuple in the list is equal to the number of range
    parameters.
    """
    class Meta:
        name = "doubleOrNilReasonTupleList"
        namespace = "http://www.opengis.net/gml"

    value: List[Union[str, NilReasonEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
