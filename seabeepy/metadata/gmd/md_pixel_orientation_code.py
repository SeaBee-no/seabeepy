from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.md_pixel_orientation_code_type import MdPixelOrientationCodeType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdPixelOrientationCode:
    class Meta:
        name = "MD_PixelOrientationCode"
        namespace = "http://www.isotc211.org/2005/gmd"

    value: Optional[MdPixelOrientationCodeType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
