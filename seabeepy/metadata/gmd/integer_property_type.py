from dataclasses import dataclass, field
from typing import Optional, Union
from seabeepy.metadata.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class IntegerPropertyType:
    class Meta:
        name = "Integer_PropertyType"

    integer: Optional[int] = field(
        default=None,
        metadata={
            "name": "Integer",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )
