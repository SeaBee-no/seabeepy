from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.integer_property_type import IntegerPropertyType
from seabeepy.metadata.gmd.md_range_dimension_type import MdRangeDimensionType
from seabeepy.metadata.gmd.real_property_type import RealPropertyType
from seabeepy.metadata.gmd.uom_length_property_type import UomLengthPropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdBandType(MdRangeDimensionType):
    class Meta:
        name = "MD_Band_Type"

    max_value: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "maxValue",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    min_value: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "minValue",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    units: Optional[UomLengthPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    peak_response: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "peakResponse",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    bits_per_value: Optional[IntegerPropertyType] = field(
        default=None,
        metadata={
            "name": "bitsPerValue",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    tone_gradation: Optional[IntegerPropertyType] = field(
        default=None,
        metadata={
            "name": "toneGradation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    scale_factor: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "scaleFactor",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    offset: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
