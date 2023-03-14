from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MappingRuleType:
    rule_definition: Optional[str] = field(
        default=None,
        metadata={
            "name": "ruleDefinition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    rule_reference: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "ruleReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
