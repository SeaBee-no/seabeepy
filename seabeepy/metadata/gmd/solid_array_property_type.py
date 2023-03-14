from dataclasses import dataclass, field
from typing import List
from seabeepy.metadata.gmd.solid import Solid
from seabeepy.metadata.gmd.solid_property_type import CompositeSolid

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SolidArrayPropertyType:
    """gml:SolidArrayPropertyType is a container for an array of solids.

    The elements are always contained in the array property, referencing
    geometry elements or arrays of geometry elements is not supported.
    """
    composite_solid: List[CompositeSolid] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    solid: List[Solid] = field(
        default_factory=list,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequential": True,
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
