from dataclasses import dataclass, field
from typing import List, Union
from seabeepy.metadata.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CountExtent:
    class Meta:
        namespace = "http://www.opengis.net/gml"

    value: List[Union[str, NilReasonEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "length": 2,
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
