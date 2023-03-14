from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.linear_ring import LinearRing

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LinearRingPropertyType:
    """
    A property with the content model of gml:LinearRingPropertyType
    encapsulates a linear ring to represent a component of a surface boundary.
    """
    linear_ring: Optional[LinearRing] = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
