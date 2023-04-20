from dataclasses import dataclass, field
from typing import Optional, Union
from seabeepy.metadata.gmd.md_scope_description import MdScopeDescription
from seabeepy.metadata.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdScopeDescriptionPropertyType:
    class Meta:
        name = "MD_ScopeDescription_PropertyType"

    md_scope_description: Optional[MdScopeDescription] = field(
        default=None,
        metadata={
            "name": "MD_ScopeDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )
