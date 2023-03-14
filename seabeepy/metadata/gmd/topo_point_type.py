from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.abstract_topology_type import AbstractTopologyType
from seabeepy.metadata.gmd.container_property_type import DirectedNode

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoPointType(AbstractTopologyType):
    directed_node: Optional[DirectedNode] = field(
        default=None,
        metadata={
            "name": "directedNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
