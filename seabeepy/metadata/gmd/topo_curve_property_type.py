from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.topo_curve import TopoCurve

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoCurvePropertyType:
    topo_curve: Optional[TopoCurve] = field(
        default=None,
        metadata={
            "name": "TopoCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
