from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.abstract_dq_result_type import AbstractDqResultType
from seabeepy.metadata.gmd.character_string_property_type import CharacterStringPropertyType
from seabeepy.metadata.gmd.record_property_type import RecordPropertyType
from seabeepy.metadata.gmd.record_type_property_type import RecordTypePropertyType
from seabeepy.metadata.gmd.unit_of_measure_property_type import UnitOfMeasurePropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqQuantitativeResultType(AbstractDqResultType):
    """Quantitative_conformance_measure from Quality Procedures.

    -  - Renamed to remove implied use limitation -  - OCL - -- result is type specified by valueDomain - result.tupleType = valueDomain
    """
    class Meta:
        name = "DQ_QuantitativeResult_Type"

    value_type: Optional[RecordTypePropertyType] = field(
        default=None,
        metadata={
            "name": "valueType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    value_unit: Optional[UnitOfMeasurePropertyType] = field(
        default=None,
        metadata={
            "name": "valueUnit",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    error_statistic: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "errorStatistic",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    value: List[RecordPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )
