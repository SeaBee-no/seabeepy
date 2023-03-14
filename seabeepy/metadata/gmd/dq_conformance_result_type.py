from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.abstract_dq_result_type import AbstractDqResultType
from seabeepy.metadata.gmd.boolean_property_type_2 import BooleanPropertyType2
from seabeepy.metadata.gmd.character_string_property_type import CharacterStringPropertyType
from seabeepy.metadata.gmd.ci_citation_type import CiCitationPropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqConformanceResultType(AbstractDqResultType):
    """quantitative_result from Quality Procedures -  - renamed to remove implied use limitiation."""
    class Meta:
        name = "DQ_ConformanceResult_Type"

    specification: Optional[CiCitationPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    explanation: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    pass_value: Optional[BooleanPropertyType2] = field(
        default=None,
        metadata={
            "name": "pass",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
