from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.abstract_object_type import AbstractObjectType
from seabeepy.metadata.gmd.character_string_property_type import CharacterStringPropertyType
from seabeepy.metadata.gmd.member_name_property_type import MemberNamePropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdRangeDimensionType(AbstractObjectType):
    """
    Set of adjacent wavelengths in the electro-magnetic spectrum with a common
    characteristic, such as the visible band.
    """
    class Meta:
        name = "MD_RangeDimension_Type"

    sequence_identifier: Optional[MemberNamePropertyType] = field(
        default=None,
        metadata={
            "name": "sequenceIdentifier",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    descriptor: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
