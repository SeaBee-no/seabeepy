from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.abstract_parametric_curve_surface_type import AbstractParametricCurveSurfaceType
from seabeepy.metadata.gmd.point_property import PointProperty
from seabeepy.metadata.gmd.pos import Pos
from seabeepy.metadata.gmd.pos_list import PosList

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGriddedSurfaceType(AbstractParametricCurveSurfaceType):
    rows: Optional["AbstractGriddedSurfaceType.Rows"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    rows_attribute: Optional[int] = field(
        default=None,
        metadata={
            "name": "rows",
            "type": "Attribute",
        }
    )
    columns: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )

    @dataclass
    class Rows:
        row: List["AbstractGriddedSurfaceType.Rows.Row"] = field(
            default_factory=list,
            metadata={
                "name": "Row",
                "type": "Element",
                "namespace": "http://www.opengis.net/gml",
                "min_occurs": 1,
            }
        )

        @dataclass
        class Row:
            pos_list: Optional[PosList] = field(
                default=None,
                metadata={
                    "name": "posList",
                    "type": "Element",
                    "namespace": "http://www.opengis.net/gml",
                }
            )
            pos: List[Pos] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "namespace": "http://www.opengis.net/gml",
                }
            )
            point_property: List[PointProperty] = field(
                default_factory=list,
                metadata={
                    "name": "pointProperty",
                    "type": "Element",
                    "namespace": "http://www.opengis.net/gml",
                }
            )
