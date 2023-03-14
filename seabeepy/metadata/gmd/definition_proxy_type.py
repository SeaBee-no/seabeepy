from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.definition_ref import DefinitionRef
from seabeepy.metadata.gmd.definition_type import DefinitionType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DefinitionProxyType(DefinitionType):
    definition_ref: Optional[DefinitionRef] = field(
        default=None,
        metadata={
            "name": "definitionRef",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
