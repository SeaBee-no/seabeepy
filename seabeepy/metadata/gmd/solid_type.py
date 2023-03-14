from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.abstract_solid_type import AbstractSolidType
from seabeepy.metadata.gmd.shell_property_type import ShellPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SolidType(AbstractSolidType):
    exterior: Optional[ShellPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    interior: List[ShellPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
