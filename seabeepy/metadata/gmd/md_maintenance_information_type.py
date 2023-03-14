from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.abstract_object_type import AbstractObjectType
from seabeepy.metadata.gmd.character_string_property_type import CharacterStringPropertyType
from seabeepy.metadata.gmd.ci_responsible_party_property_type import CiResponsiblePartyPropertyType
from seabeepy.metadata.gmd.date_property_type import DatePropertyType
from seabeepy.metadata.gmd.md_maintenance_frequency_code_property_type import MdMaintenanceFrequencyCodePropertyType
from seabeepy.metadata.gmd.md_scope_code_property_type import MdScopeCodePropertyType
from seabeepy.metadata.gmd.md_scope_description_property_type import MdScopeDescriptionPropertyType
from seabeepy.metadata.gmd.tm_period_duration_property_type import TmPeriodDurationPropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdMaintenanceInformationType(AbstractObjectType):
    """
    Information about the scope and frequency of updating.
    """
    class Meta:
        name = "MD_MaintenanceInformation_Type"

    maintenance_and_update_frequency: Optional[MdMaintenanceFrequencyCodePropertyType] = field(
        default=None,
        metadata={
            "name": "maintenanceAndUpdateFrequency",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    date_of_next_update: Optional[DatePropertyType] = field(
        default=None,
        metadata={
            "name": "dateOfNextUpdate",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    user_defined_maintenance_frequency: Optional[TmPeriodDurationPropertyType] = field(
        default=None,
        metadata={
            "name": "userDefinedMaintenanceFrequency",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    update_scope: List[MdScopeCodePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "updateScope",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    update_scope_description: List[MdScopeDescriptionPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "updateScopeDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    maintenance_note: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "maintenanceNote",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    contact: List[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
