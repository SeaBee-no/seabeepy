from dataclasses import dataclass, field
from typing import List
from seabeepy.metadata.gmd.point import Point

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PointArrayPropertyType:
    """gml:PointArrayPropertyType is a container for an array of points.

    The elements are always contained inline in the array property,
    referencing geometry elements or arrays of geometry elements via
    XLinks is not supported.
    """
    point: List[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
