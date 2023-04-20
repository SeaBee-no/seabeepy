from dataclasses import dataclass, field
from typing import List
from seabeepy.metadata.gmd.abstract_time_complex_type import AbstractTimeComplexType
from seabeepy.metadata.gmd.time_topology_primitive_property_type import TimeTopologyPrimitivePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeTopologyComplexType(AbstractTimeComplexType):
    primitive: List[TimeTopologyPrimitivePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
