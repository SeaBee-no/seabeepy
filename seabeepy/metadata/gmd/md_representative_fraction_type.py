from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.abstract_object_type import AbstractObjectType
from seabeepy.metadata.gmd.integer_property_type import IntegerPropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdRepresentativeFractionType(AbstractObjectType):
    class Meta:
        name = "MD_RepresentativeFraction_Type"

    denominator: Optional[IntegerPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
