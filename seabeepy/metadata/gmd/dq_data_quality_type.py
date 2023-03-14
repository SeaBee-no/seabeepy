from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.abstract_object_type import AbstractObjectType
from seabeepy.metadata.gmd.dq_element_property_type import DqElementPropertyType
from seabeepy.metadata.gmd.dq_scope_property_type import DqScopePropertyType
from seabeepy.metadata.gmd.li_lineage_property_type import LiLineagePropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqDataQualityType(AbstractObjectType):
    class Meta:
        name = "DQ_DataQuality_Type"

    scope: Optional[DqScopePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    report: List[DqElementPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    lineage: Optional[LiLineagePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
