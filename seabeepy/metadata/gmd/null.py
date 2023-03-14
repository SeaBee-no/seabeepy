from dataclasses import dataclass, field
from typing import Union
from seabeepy.metadata.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Null:
    class Meta:
        namespace = "http://www.opengis.net/gml"

    value: Union[str, NilReasonEnumerationValue] = field(
        default="",
        metadata={
            "pattern": r"other:\w{2,}",
        }
    )
