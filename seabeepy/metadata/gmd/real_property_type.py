from dataclasses import dataclass, field
from typing import Optional, Union
from seabeepy.metadata.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class RealPropertyType:
    class Meta:
        name = "Real_PropertyType"

    real: Optional[float] = field(
        default=None,
        metadata={
            "name": "Real",
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
