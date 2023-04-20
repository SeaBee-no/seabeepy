from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.abstract_object_type import AbstractObjectType
from seabeepy.metadata.gmd.tm_primitive_property_type import TmPrimitivePropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class ExTemporalExtentType(AbstractObjectType):
    """
    Time period covered by the content of the dataset.
    """
    class Meta:
        name = "EX_TemporalExtent_Type"

    extent: Optional[TmPrimitivePropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
