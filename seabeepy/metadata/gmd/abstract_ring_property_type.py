from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.linear_ring import LinearRing
from seabeepy.metadata.gmd.ring import Ring

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractRingPropertyType:
    """
    A property with the content model of gml:AbstractRingPropertyType
    encapsulates a ring to represent the surface boundary property of a
    surface.
    """
    ring: Optional[Ring] = field(
        default=None,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    linear_ring: Optional[LinearRing] = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
