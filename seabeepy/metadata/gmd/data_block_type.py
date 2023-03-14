from dataclasses import dataclass, field
from typing import List, Optional, Union
from seabeepy.metadata.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue
from seabeepy.metadata.gmd.range_parameters import RangeParameters
from seabeepy.metadata.gmd.tuple_list import TupleList

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DataBlockType:
    range_parameters: Optional[RangeParameters] = field(
        default=None,
        metadata={
            "name": "rangeParameters",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    tuple_list: Optional[TupleList] = field(
        default=None,
        metadata={
            "name": "tupleList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    double_or_nil_reason_tuple_list: List[Union[str, NilReasonEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "name": "doubleOrNilReasonTupleList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
