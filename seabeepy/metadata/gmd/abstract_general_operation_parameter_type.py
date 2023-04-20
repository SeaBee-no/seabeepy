from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.identified_object_type import IdentifiedObjectType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeneralOperationParameterType(IdentifiedObjectType):
    minimum_occurs: Optional[int] = field(
        default=None,
        metadata={
            "name": "minimumOccurs",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
