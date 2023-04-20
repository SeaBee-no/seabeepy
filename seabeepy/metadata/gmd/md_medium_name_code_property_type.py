from dataclasses import dataclass, field
from typing import Optional, Union
from seabeepy.metadata.gmd.md_medium_name_code import MdMediumNameCode
from seabeepy.metadata.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdMediumNameCodePropertyType:
    class Meta:
        name = "MD_MediumNameCode_PropertyType"

    md_medium_name_code: Optional[MdMediumNameCode] = field(
        default=None,
        metadata={
            "name": "MD_MediumNameCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
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
