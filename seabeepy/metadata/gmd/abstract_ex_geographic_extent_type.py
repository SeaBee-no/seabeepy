from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.abstract_object_type import AbstractObjectType
from seabeepy.metadata.gmd.boolean_property_type_2 import BooleanPropertyType2

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractExGeographicExtentType(AbstractObjectType):
    """
    Geographic area of the dataset.
    """
    class Meta:
        name = "AbstractEX_GeographicExtent_Type"

    extent_type_code: Optional[BooleanPropertyType2] = field(
        default=None,
        metadata={
            "name": "extentTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
