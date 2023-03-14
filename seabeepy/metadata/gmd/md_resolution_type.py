from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.distance_property_type import DistancePropertyType
from seabeepy.metadata.gmd.md_representative_fraction_property_type import MdRepresentativeFractionPropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdResolutionType:
    class Meta:
        name = "MD_Resolution_Type"

    equivalent_scale: Optional[MdRepresentativeFractionPropertyType] = field(
        default=None,
        metadata={
            "name": "equivalentScale",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    distance: Optional[DistancePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
