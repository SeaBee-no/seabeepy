from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.abstract_object_type import AbstractObjectType
from seabeepy.metadata.gmd.character_string_property_type import CharacterStringPropertyType
from seabeepy.metadata.gmd.ci_citation_type import (
    CiCitationPropertyType,
    MdIdentifierPropertyType,
)
from seabeepy.metadata.gmd.date_time_property_type import DateTimePropertyType
from seabeepy.metadata.gmd.dq_evaluation_method_type_code_property_type import DqEvaluationMethodTypeCodePropertyType
from seabeepy.metadata.gmd.dq_result_property_type import DqResultPropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractDqElementType(AbstractObjectType):
    class Meta:
        name = "AbstractDQ_Element_Type"

    name_of_measure: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "nameOfMeasure",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    measure_identification: Optional[MdIdentifierPropertyType] = field(
        default=None,
        metadata={
            "name": "measureIdentification",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    measure_description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "measureDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    evaluation_method_type: Optional[DqEvaluationMethodTypeCodePropertyType] = field(
        default=None,
        metadata={
            "name": "evaluationMethodType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    evaluation_method_description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "evaluationMethodDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    evaluation_procedure: Optional[CiCitationPropertyType] = field(
        default=None,
        metadata={
            "name": "evaluationProcedure",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    date_time: List[DateTimePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "dateTime",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    result: List[DqResultPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
            "max_occurs": 2,
        }
    )
