from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.abstract_object_type import AbstractObjectType
from seabeepy.metadata.gmd.ci_date_type_code_property_type import CiDateTypeCodePropertyType
from seabeepy.metadata.gmd.date_property_type import DatePropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiDateType(AbstractObjectType):
    class Meta:
        name = "CI_Date_Type"

    date: Optional[DatePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    date_type: Optional[CiDateTypeCodePropertyType] = field(
        default=None,
        metadata={
            "name": "dateType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
