from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.definition_type import DefinitionType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeReferenceSystemType(DefinitionType):
    domain_of_validity: Optional[str] = field(
        default=None,
        metadata={
            "name": "domainOfValidity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
