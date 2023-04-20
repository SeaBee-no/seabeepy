from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.abstract_object_type import AbstractObjectType
from seabeepy.metadata.gmd.character_string_property_type import CharacterStringPropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiSeriesType(AbstractObjectType):
    class Meta:
        name = "CI_Series_Type"

    name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    issue_identification: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "issueIdentification",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    page: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
