from dataclasses import dataclass, field
from typing import Optional, Union
from seabeepy.metadata.gmd.md_pixel_orientation_code_type import MdPixelOrientationCodeType
from seabeepy.metadata.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdPixelOrientationCodePropertyType:
    class Meta:
        name = "MD_PixelOrientationCode_PropertyType"

    md_pixel_orientation_code: Optional[MdPixelOrientationCodeType] = field(
        default=None,
        metadata={
            "name": "MD_PixelOrientationCode",
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
