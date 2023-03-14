from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.definition_base_type import DefinitionBaseType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DefinitionType(DefinitionBaseType):
    remarks: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
