from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.abstract_object_type import AbstractObjectType
from seabeepy.metadata.gmd.character_string_property_type import CharacterStringPropertyType
from seabeepy.metadata.gmd.ci_contact_property_type import CiContactPropertyType
from seabeepy.metadata.gmd.ci_role_code_property_type import CiRoleCodePropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiResponsiblePartyType(AbstractObjectType):
    """
    Identification of, and means of communication with, person(s) and
    organisations associated with the dataset.
    """
    class Meta:
        name = "CI_ResponsibleParty_Type"

    individual_name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "individualName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    organisation_name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "organisationName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    position_name: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "positionName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    contact_info: Optional[CiContactPropertyType] = field(
        default=None,
        metadata={
            "name": "contactInfo",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    role: Optional[CiRoleCodePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
