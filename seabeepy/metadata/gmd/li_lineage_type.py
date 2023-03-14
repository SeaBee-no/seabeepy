from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.abstract_object_type import AbstractObjectType
from seabeepy.metadata.gmd.character_string_property_type import CharacterStringPropertyType
from seabeepy.metadata.gmd.li_process_step_property_type import (
    LiProcessStepPropertyType,
    LiSourcePropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class LiLineageType(AbstractObjectType):
    class Meta:
        name = "LI_Lineage_Type"

    statement: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    process_step: List[LiProcessStepPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "processStep",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    source: List[LiSourcePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
