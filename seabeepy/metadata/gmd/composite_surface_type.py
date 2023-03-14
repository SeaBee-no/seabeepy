from dataclasses import dataclass, field
from typing import List, Optional, Union
from seabeepy.metadata.gmd.abstract_surface_type import AbstractSurfaceType
from seabeepy.metadata.gmd.actuate_value import ActuateValue
from seabeepy.metadata.gmd.aggregation_type import AggregationType
from seabeepy.metadata.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue
from seabeepy.metadata.gmd.polygon import Polygon
from seabeepy.metadata.gmd.polyhedral_surface import PolyhedralSurface
from seabeepy.metadata.gmd.show_value import ShowValue
from seabeepy.metadata.gmd.sign_type import SignType
from seabeepy.metadata.gmd.surface import Surface
from seabeepy.metadata.gmd.tin import Tin
from seabeepy.metadata.gmd.triangulated_surface import TriangulatedSurface

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CompositeSurfaceType(AbstractSurfaceType):
    surface_member: List["SurfaceMember"] = field(
        default_factory=list,
        metadata={
            "name": "surfaceMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        }
    )


@dataclass
class OrientableSurfaceType(AbstractSurfaceType):
    base_surface: Optional["BaseSurface"] = field(
        default=None,
        metadata={
            "name": "baseSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    orientation: SignType = field(
        default=SignType.VALUE,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class CompositeSurface(CompositeSurfaceType):
    """A gml:CompositeSurface is represented by a set of orientable surfaces.

    It is geometry type with all the geometric properties of a
    (primitive) surface. Essentially, a composite surface is a
    collection of surfaces that join in pairs on common boundary curves
    and which, when considered as a whole, form a single surface.
    surfaceMember references or contains inline one surface in the
    composite surface. The surfaces are contiguous.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class OrientableSurface(OrientableSurfaceType):
    """OrientableSurface consists of a surface and an orientation.

    If the orientation is "+", then the OrientableSurface is identical
    to the baseSurface. If the orientation is "-", then the
    OrientableSurface is a reference to a gml:AbstractSurface with an
    up-normal that reverses the direction for this OrientableSurface,
    the sense of "the top of the surface".
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class SurfacePropertyType:
    """A property that has a surface as its value domain may either be an
    appropriate geometry element encapsulated in an element of this type or an
    XLink reference to a remote geometry element (where remote includes
    geometry elements located elsewhere in the same document).

    Either the reference or the contained element shall be given, but
    neither both nor none.
    """
    composite_surface: Optional[CompositeSurface] = field(
        default=None,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    orientable_surface: Optional[OrientableSurface] = field(
        default=None,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    tin: Optional[Tin] = field(
        default=None,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    triangulated_surface: Optional[TriangulatedSurface] = field(
        default=None,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    polyhedral_surface: Optional[PolyhedralSurface] = field(
        default=None,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    surface: Optional[Surface] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    type: str = field(
        init=False,
        default="simple",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        }
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class BaseSurface(SurfacePropertyType):
    """The property baseSurface references or contains the base surface.

    The property baseSurface either references the base surface via the
    XLink-attributes or contains the surface element. A surface element
    is any element which is substitutable for gml:AbstractSurface. The
    base surface has positive orientation.
    """
    class Meta:
        name = "baseSurface"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SurfaceMember(SurfacePropertyType):
    """This property element either references a surface via the XLink-
    attributes or contains the surface element.

    A surface element is any element, which is substitutable for
    gml:AbstractSurface.
    """
    class Meta:
        name = "surfaceMember"
        namespace = "http://www.opengis.net/gml"
