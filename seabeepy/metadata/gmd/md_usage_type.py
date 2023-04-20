from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.abstract_object_type import AbstractObjectType
from seabeepy.metadata.gmd.character_string_property_type import CharacterStringPropertyType
from seabeepy.metadata.gmd.ci_responsible_party_property_type import CiResponsiblePartyPropertyType
from seabeepy.metadata.gmd.date_time_property_type import DateTimePropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdUsageType(AbstractObjectType):
    """
    Brief description of ways in which the dataset is currently used.
    """
    class Meta:
        name = "MD_Usage_Type"

    specific_usage: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "specificUsage",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    usage_date_time: Optional[DateTimePropertyType] = field(
        default=None,
        metadata={
            "name": "usageDateTime",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    user_determined_limitations: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "userDeterminedLimitations",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    user_contact_info: List[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "userContactInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )
