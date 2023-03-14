from dataclasses import dataclass, field
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDate, XmlDateTime
from seabeepy.metadata.gmd.abstract_general_parameter_value_property_type import (
    IncludesValue,
    ParameterValue2,
    UsesValue,
)
from seabeepy.metadata.gmd.abstract_object_type import AbstractObjectType
from seabeepy.metadata.gmd.actuate_value import ActuateValue
from seabeepy.metadata.gmd.affine_cs_2 import AffineCs2
from seabeepy.metadata.gmd.aggregation_type import AggregationType
from seabeepy.metadata.gmd.anchor_definition import AnchorDefinition
from seabeepy.metadata.gmd.anchor_point import AnchorPoint
from seabeepy.metadata.gmd.cartesian_cs_2 import CartesianCs2
from seabeepy.metadata.gmd.character_string_property_type import CharacterStringPropertyType
from seabeepy.metadata.gmd.coordinate_operation_accuracy import CoordinateOperationAccuracy
from seabeepy.metadata.gmd.coordinate_system import CoordinateSystem
from seabeepy.metadata.gmd.derived_crstype import DerivedCrstype
from seabeepy.metadata.gmd.ellipsoid_2 import Ellipsoid2
from seabeepy.metadata.gmd.ellipsoidal_cs_2 import EllipsoidalCs2
from seabeepy.metadata.gmd.ex_geographic_extent_property_type import ExGeographicExtentPropertyType
from seabeepy.metadata.gmd.ex_temporal_extent_property_type import ExTemporalExtentPropertyType
from seabeepy.metadata.gmd.identified_object_type import IdentifiedObjectType
from seabeepy.metadata.gmd.method import Method
from seabeepy.metadata.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue
from seabeepy.metadata.gmd.pixel_in_cell import PixelInCell
from seabeepy.metadata.gmd.prime_meridian_2 import PrimeMeridian2
from seabeepy.metadata.gmd.real_property_type import RealPropertyType
from seabeepy.metadata.gmd.show_value import ShowValue
from seabeepy.metadata.gmd.spherical_cs_2 import SphericalCs2
from seabeepy.metadata.gmd.time_cs_2 import TimeCs2
from seabeepy.metadata.gmd.uses_affine_cs import UsesAffineCs
from seabeepy.metadata.gmd.uses_cartesian_cs import UsesCartesianCs
from seabeepy.metadata.gmd.uses_cs import UsesCs
from seabeepy.metadata.gmd.uses_ellipsoid import UsesEllipsoid
from seabeepy.metadata.gmd.uses_ellipsoidal_cs import UsesEllipsoidalCs
from seabeepy.metadata.gmd.uses_method import UsesMethod
from seabeepy.metadata.gmd.uses_oblique_cartesian_cs import UsesObliqueCartesianCs
from seabeepy.metadata.gmd.uses_prime_meridian import UsesPrimeMeridian
from seabeepy.metadata.gmd.uses_spherical_cs import UsesSphericalCs
from seabeepy.metadata.gmd.uses_temporal_cs import UsesTemporalCs
from seabeepy.metadata.gmd.uses_time_cs import UsesTimeCs
from seabeepy.metadata.gmd.uses_vertical_cs import UsesVerticalCs
from seabeepy.metadata.gmd.vertical_cs_2 import VerticalCs2


@dataclass
class AbstractCrstype(IdentifiedObjectType):
    class Meta:
        name = "AbstractCRSType"
        target_namespace = "http://www.opengis.net/gml"

    domain_of_validity: List["DomainOfValidity"] = field(
        default_factory=list,
        metadata={
            "name": "domainOfValidity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    scope: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )


@dataclass
class AbstractDatumType(IdentifiedObjectType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml"

    domain_of_validity: Optional["DomainOfValidity"] = field(
        default=None,
        metadata={
            "name": "domainOfValidity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    scope: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
    anchor_point: Optional[AnchorPoint] = field(
        default=None,
        metadata={
            "name": "anchorPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    anchor_definition: Optional[AnchorDefinition] = field(
        default=None,
        metadata={
            "name": "anchorDefinition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    realization_epoch: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "realizationEpoch",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class GeneralConversionPropertyType:
    """
    gml:GeneralConversionPropertyType is a property type for association roles
    to a general conversion, either referencing or containing the definition of
    that conversion.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml"

    conversion: Optional["Conversion1"] = field(
        default=None,
        metadata={
            "name": "Conversion",
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


@dataclass
class EngineeringDatumType(AbstractDatumType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml"


@dataclass
class GeodeticDatumType(AbstractDatumType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml"

    uses_prime_meridian: Optional[UsesPrimeMeridian] = field(
        default=None,
        metadata={
            "name": "usesPrimeMeridian",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    prime_meridian: Optional[PrimeMeridian2] = field(
        default=None,
        metadata={
            "name": "primeMeridian",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_ellipsoid: Optional[UsesEllipsoid] = field(
        default=None,
        metadata={
            "name": "usesEllipsoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    ellipsoid: Optional[Ellipsoid2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class ImageDatumType(AbstractDatumType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml"

    pixel_in_cell: Optional[PixelInCell] = field(
        default=None,
        metadata={
            "name": "pixelInCell",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class TemporalDatumBaseType(AbstractDatumType):
    """The TemporalDatumBaseType partially defines the origin of a temporal
    coordinate reference system.

    This type restricts the AbstractDatumType to remove the
    "anchorDefinition" and "realizationEpoch" elements.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml"


@dataclass
class VerticalDatumType(AbstractDatumType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml"


@dataclass
class Conversion2(GeneralConversionPropertyType):
    """
    gml:conversion is an association role to the coordinate conversion used to
    define the derived CRS.
    """
    class Meta:
        name = "conversion"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DefinedByConversion(GeneralConversionPropertyType):
    class Meta:
        name = "definedByConversion"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractGeneralDerivedCrstype(AbstractCrstype):
    class Meta:
        name = "AbstractGeneralDerivedCRSType"
        target_namespace = "http://www.opengis.net/gml"

    defined_by_conversion: Optional[DefinedByConversion] = field(
        default=None,
        metadata={
            "name": "definedByConversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    conversion: Optional[Conversion2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class EngineeringDatum1(EngineeringDatumType):
    """gml:EngineeringDatum defines the origin of an engineering coordinate
    reference system, and is used in a region around that origin.

    This origin may be fixed with respect to the earth (such as a
    defined point at a construction site), or be a defined point on a
    moving vehicle (such as on a ship or satellite).
    """
    class Meta:
        name = "EngineeringDatum"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeodeticDatum1(GeodeticDatumType):
    """
    gml:GeodeticDatum is a geodetic datum defines the precise location and
    orientation in 3-dimensional space of a defined ellipsoid (or sphere), or
    of a Cartesian coordinate system centered in this ellipsoid (or sphere).
    """
    class Meta:
        name = "GeodeticDatum"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ImageDatum1(ImageDatumType):
    """gml:ImageDatum defines the origin of an image coordinate reference
    system, and is used in a local context only.

    For an image datum, the anchor definition is usually either the
    centre of the image or the corner of the image. For more
    information, see ISO 19111 B.3.5.
    """
    class Meta:
        name = "ImageDatum"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TemporalDatumType(TemporalDatumBaseType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml"

    origin: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class VerticalDatum1(VerticalDatumType):
    """
    gml:VerticalDatum is a textual description and/or a set of parameters
    identifying a particular reference level surface used as a zero-height
    surface, including its position with respect to the Earth for any of the
    height types recognized by this International Standard.
    """
    class Meta:
        name = "VerticalDatum"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DerivedCrstype1(AbstractGeneralDerivedCrstype):
    class Meta:
        name = "DerivedCRSType"
        target_namespace = "http://www.opengis.net/gml"

    base_crs: Optional["BaseCrs"] = field(
        default=None,
        metadata={
            "name": "baseCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    derived_crstype: Optional[DerivedCrstype] = field(
        default=None,
        metadata={
            "name": "derivedCRSType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    uses_cs: Optional[UsesCs] = field(
        default=None,
        metadata={
            "name": "usesCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinate_system: Optional[CoordinateSystem] = field(
        default=None,
        metadata={
            "name": "coordinateSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class EngineeringDatumPropertyType:
    """
    gml:EngineeringDatumPropertyType is a property type for association roles
    to an engineering datum, either referencing or containing the definition of
    that datum.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml"

    engineering_datum: Optional[EngineeringDatum1] = field(
        default=None,
        metadata={
            "name": "EngineeringDatum",
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


@dataclass
class GeodeticDatumPropertyType:
    """
    gml:GeodeticDatumPropertyType is a property type for association roles to a
    geodetic datum, either referencing or containing the definition of that
    datum.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml"

    geodetic_datum: Optional[GeodeticDatum1] = field(
        default=None,
        metadata={
            "name": "GeodeticDatum",
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


@dataclass
class ImageDatumPropertyType:
    """
    gml:ImageDatumPropertyType is a property type for association roles to an
    image datum, either referencing or containing the definition of that datum.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml"

    image_datum: Optional[ImageDatum1] = field(
        default=None,
        metadata={
            "name": "ImageDatum",
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


@dataclass
class TemporalDatum1(TemporalDatumType):
    """A gml:TemporalDatum defines the origin of a Temporal Reference System.

    This type omits the "anchorDefinition" and "realizationEpoch"
    elements and adds the "origin" element with the dateTime type.
    """
    class Meta:
        name = "TemporalDatum"
        namespace = "http://www.opengis.net/gml"


@dataclass
class VerticalDatumPropertyType:
    """
    gml:VerticalDatumPropertyType is property type for association roles to a
    vertical datum, either referencing or containing the definition of that
    datum.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml"

    vertical_datum: Optional[VerticalDatum1] = field(
        default=None,
        metadata={
            "name": "VerticalDatum",
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


@dataclass
class DerivedCrs(DerivedCrstype1):
    """gml:DerivedCRS is a single coordinate reference system that is defined
    by its coordinate conversion from another single coordinate reference
    system known as the base CRS.

    The base CRS can be a projected coordinate reference system, if this
    DerivedCRS is used for a georectified grid coverage as described in
    ISO 19123, Clause 8.
    """
    class Meta:
        name = "DerivedCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TemporalDatumPropertyType:
    """
    gml:TemporalDatumPropertyType is a property type for association roles to a
    temporal datum, either referencing or containing the definition of that
    datum.
    """
    class Meta:
        target_namespace = "http://www.opengis.net/gml"

    temporal_datum: Optional[TemporalDatum1] = field(
        default=None,
        metadata={
            "name": "TemporalDatum",
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


@dataclass
class EngineeringDatum2(EngineeringDatumPropertyType):
    """
    gml:engineeringDatum is an association role to the engineering datum used
    by this CRS.
    """
    class Meta:
        name = "engineeringDatum"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeodeticDatum2(GeodeticDatumPropertyType):
    """
    gml:geodeticDatum is an association role to the geodetic datum used by this
    CRS.
    """
    class Meta:
        name = "geodeticDatum"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ImageDatum2(ImageDatumPropertyType):
    """
    gml:imageDatum is an association role to the image datum used by this CRS.
    """
    class Meta:
        name = "imageDatum"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesEngineeringDatum(EngineeringDatumPropertyType):
    class Meta:
        name = "usesEngineeringDatum"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesGeodeticDatum(GeodeticDatumPropertyType):
    class Meta:
        name = "usesGeodeticDatum"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesImageDatum(ImageDatumPropertyType):
    class Meta:
        name = "usesImageDatum"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesVerticalDatum(VerticalDatumPropertyType):
    class Meta:
        name = "usesVerticalDatum"
        namespace = "http://www.opengis.net/gml"


@dataclass
class VerticalDatum2(VerticalDatumPropertyType):
    """
    gml:verticalDatum is an association role to the vertical datum used by this
    CRS.
    """
    class Meta:
        name = "verticalDatum"
        namespace = "http://www.opengis.net/gml"


@dataclass
class EngineeringCrstype(AbstractCrstype):
    class Meta:
        name = "EngineeringCRSType"
        target_namespace = "http://www.opengis.net/gml"

    uses_cs: Optional[UsesCs] = field(
        default=None,
        metadata={
            "name": "usesCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinate_system: Optional[CoordinateSystem] = field(
        default=None,
        metadata={
            "name": "coordinateSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_engineering_datum: Optional[UsesEngineeringDatum] = field(
        default=None,
        metadata={
            "name": "usesEngineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    engineering_datum: Optional[EngineeringDatum2] = field(
        default=None,
        metadata={
            "name": "engineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class GeocentricCrstype(AbstractCrstype):
    class Meta:
        name = "GeocentricCRSType"
        target_namespace = "http://www.opengis.net/gml"

    uses_cartesian_cs: Optional[UsesCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_spherical_cs: Optional[UsesSphericalCs] = field(
        default=None,
        metadata={
            "name": "usesSphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_geodetic_datum: Optional[UsesGeodeticDatum] = field(
        default=None,
        metadata={
            "name": "usesGeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class GeodeticCrstype(AbstractCrstype):
    """
    gml:GeodeticCRS is a coordinate reference system based on a geodetic datum.
    """
    class Meta:
        name = "GeodeticCRSType"
        target_namespace = "http://www.opengis.net/gml"

    uses_ellipsoidal_cs: Optional[UsesEllipsoidalCs] = field(
        default=None,
        metadata={
            "name": "usesEllipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    ellipsoidal_cs: Optional[EllipsoidalCs2] = field(
        default=None,
        metadata={
            "name": "ellipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_cartesian_cs: Optional[UsesCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    cartesian_cs: Optional[CartesianCs2] = field(
        default=None,
        metadata={
            "name": "cartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_spherical_cs: Optional[UsesSphericalCs] = field(
        default=None,
        metadata={
            "name": "usesSphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    spherical_cs: Optional[SphericalCs2] = field(
        default=None,
        metadata={
            "name": "sphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_geodetic_datum: Optional[UsesGeodeticDatum] = field(
        default=None,
        metadata={
            "name": "usesGeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geodetic_datum: Optional[GeodeticDatum2] = field(
        default=None,
        metadata={
            "name": "geodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class GeographicCrstype(AbstractCrstype):
    class Meta:
        name = "GeographicCRSType"
        target_namespace = "http://www.opengis.net/gml"

    uses_ellipsoidal_cs: Optional[UsesEllipsoidalCs] = field(
        default=None,
        metadata={
            "name": "usesEllipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    uses_geodetic_datum: Optional[UsesGeodeticDatum] = field(
        default=None,
        metadata={
            "name": "usesGeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )


@dataclass
class ImageCrstype(AbstractCrstype):
    class Meta:
        name = "ImageCRSType"
        target_namespace = "http://www.opengis.net/gml"

    uses_cartesian_cs: Optional[UsesCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    cartesian_cs: Optional[CartesianCs2] = field(
        default=None,
        metadata={
            "name": "cartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_affine_cs: Optional[UsesAffineCs] = field(
        default=None,
        metadata={
            "name": "usesAffineCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    affine_cs: Optional[AffineCs2] = field(
        default=None,
        metadata={
            "name": "affineCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_oblique_cartesian_cs: Optional[UsesObliqueCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesObliqueCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_image_datum: Optional[UsesImageDatum] = field(
        default=None,
        metadata={
            "name": "usesImageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    image_datum: Optional[ImageDatum2] = field(
        default=None,
        metadata={
            "name": "imageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class VerticalCrstype(AbstractCrstype):
    class Meta:
        name = "VerticalCRSType"
        target_namespace = "http://www.opengis.net/gml"

    uses_vertical_cs: Optional[UsesVerticalCs] = field(
        default=None,
        metadata={
            "name": "usesVerticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    vertical_cs: Optional[VerticalCs2] = field(
        default=None,
        metadata={
            "name": "verticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_vertical_datum: Optional[UsesVerticalDatum] = field(
        default=None,
        metadata={
            "name": "usesVerticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    vertical_datum: Optional[VerticalDatum2] = field(
        default=None,
        metadata={
            "name": "verticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class TemporalDatum2(TemporalDatumPropertyType):
    """
    gml:temporalDatum is an association role to the temporal datum used by this
    CRS.
    """
    class Meta:
        name = "temporalDatum"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesTemporalDatum(TemporalDatumPropertyType):
    class Meta:
        name = "usesTemporalDatum"
        namespace = "http://www.opengis.net/gml"


@dataclass
class EngineeringCrs(EngineeringCrstype):
    """gml:EngineeringCRS is a contextually local coordinate reference system
    which can be divided into two broad categories:

    -       earth-fixed systems applied to engineering activities on or near the surface of the earth;
    -       CRSs on moving platforms such as road vehicles, vessels, aircraft, or spacecraft, see ISO 19111 8.3.
    """
    class Meta:
        name = "EngineeringCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeocentricCrs(GeocentricCrstype):
    class Meta:
        name = "GeocentricCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeodeticCrs(GeodeticCrstype):
    class Meta:
        name = "GeodeticCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeographicCrs(GeographicCrstype):
    class Meta:
        name = "GeographicCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ImageCrs(ImageCrstype):
    """gml:ImageCRS is an engineering coordinate reference system applied to
    locations in images.

    Image coordinate reference systems are treated as a separate sub-
    type because the definition of the associated image datum contains
    two attributes not relevant to other engineering datums.
    """
    class Meta:
        name = "ImageCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TemporalCrstype(AbstractCrstype):
    class Meta:
        name = "TemporalCRSType"
        target_namespace = "http://www.opengis.net/gml"

    uses_time_cs: Optional[UsesTimeCs] = field(
        default=None,
        metadata={
            "name": "usesTimeCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    time_cs: Optional[TimeCs2] = field(
        default=None,
        metadata={
            "name": "timeCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_temporal_cs: Optional[UsesTemporalCs] = field(
        default=None,
        metadata={
            "name": "usesTemporalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_temporal_datum: Optional[UsesTemporalDatum] = field(
        default=None,
        metadata={
            "name": "usesTemporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    temporal_datum: Optional[TemporalDatum2] = field(
        default=None,
        metadata={
            "name": "temporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class VerticalCrs(VerticalCrstype):
    """gml:VerticalCRS is a 1D coordinate reference system used for recording
    heights or depths.

    Vertical CRSs make use of the direction of gravity to define the
    concept of height or depth, but the relationship with gravity may
    not be straightforward. By implication, ellipsoidal heights (h)
    cannot be captured in a vertical coordinate reference system.
    Ellipsoidal heights cannot exist independently, but only as an
    inseparable part of a 3D coordinate tuple defined in a geographic 3D
    coordinate reference system.
    """
    class Meta:
        name = "VerticalCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeodeticCrspropertyType:
    """
    gml:GeodeticCRSPropertyType is a property type for association roles to a
    geodetic coordinate reference system, either referencing or containing the
    definition of that reference system.
    """
    class Meta:
        name = "GeodeticCRSPropertyType"
        target_namespace = "http://www.opengis.net/gml"

    geodetic_crs: Optional[GeodeticCrs] = field(
        default=None,
        metadata={
            "name": "GeodeticCRS",
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


@dataclass
class GeographicCrspropertyType:
    class Meta:
        name = "GeographicCRSPropertyType"
        target_namespace = "http://www.opengis.net/gml"

    geographic_crs: Optional[GeographicCrs] = field(
        default=None,
        metadata={
            "name": "GeographicCRS",
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


@dataclass
class TemporalCrs(TemporalCrstype):
    """
    gml:TemporalCRS is a 1D coordinate reference system used for the recording
    of time.
    """
    class Meta:
        name = "TemporalCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class BaseGeodeticCrs(GeodeticCrspropertyType):
    """
    gml:baseGeodeticCRS is an association role to the geodetic coordinate
    reference system used by this projected CRS.
    """
    class Meta:
        name = "baseGeodeticCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class BaseGeographicCrs(GeographicCrspropertyType):
    class Meta:
        name = "baseGeographicCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ProjectedCrstype(AbstractGeneralDerivedCrstype):
    class Meta:
        name = "ProjectedCRSType"
        target_namespace = "http://www.opengis.net/gml"

    base_geodetic_crs: Optional[BaseGeodeticCrs] = field(
        default=None,
        metadata={
            "name": "baseGeodeticCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    base_geographic_crs: Optional[BaseGeographicCrs] = field(
        default=None,
        metadata={
            "name": "baseGeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_cartesian_cs: Optional[UsesCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    cartesian_cs: Optional[CartesianCs2] = field(
        default=None,
        metadata={
            "name": "cartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class ProjectedCrs(ProjectedCrstype):
    """gml:ProjectedCRS is a 2D coordinate reference system used to approximate
    the shape of the earth on a planar surface, but in such a way that the
    distortion that is inherent to the approximation is carefully controlled
    and known.

    Distortion correction is commonly applied to calculated bearings and
    distances to produce values that are a close match to actual field
    values.
    """
    class Meta:
        name = "ProjectedCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SingleCrspropertyType:
    """
    gml:SingleCRSPropertyType is a property type for association roles to a
    single coordinate reference system, either referencing or containing the
    definition of that coordinate reference system.
    """
    class Meta:
        name = "SingleCRSPropertyType"
        target_namespace = "http://www.opengis.net/gml"

    geocentric_crs: Optional[GeocentricCrs] = field(
        default=None,
        metadata={
            "name": "GeocentricCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geographic_crs: Optional[GeographicCrs] = field(
        default=None,
        metadata={
            "name": "GeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    temporal_crs: Optional[TemporalCrs] = field(
        default=None,
        metadata={
            "name": "TemporalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    image_crs: Optional[ImageCrs] = field(
        default=None,
        metadata={
            "name": "ImageCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    engineering_crs: Optional[EngineeringCrs] = field(
        default=None,
        metadata={
            "name": "EngineeringCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    vertical_crs: Optional[VerticalCrs] = field(
        default=None,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geodetic_crs: Optional[GeodeticCrs] = field(
        default=None,
        metadata={
            "name": "GeodeticCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    derived_crs: Optional[DerivedCrs] = field(
        default=None,
        metadata={
            "name": "DerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    projected_crs: Optional[ProjectedCrs] = field(
        default=None,
        metadata={
            "name": "ProjectedCRS",
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


@dataclass
class BaseCrs(SingleCrspropertyType):
    """
    gml:baseCRS is an association role to the coordinate reference system used
    by this derived CRS.
    """
    class Meta:
        name = "baseCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ComponentReferenceSystem(SingleCrspropertyType):
    """The gml:componentReferenceSystem elements are an ordered sequence of
    associations to all the component coordinate reference systems included in
    this compound coordinate reference system.

    The gml:AggregationAttributeGroup should be used to specify that the
    gml:componentReferenceSystem properties are ordered.
    """
    class Meta:
        name = "componentReferenceSystem"
        namespace = "http://www.opengis.net/gml"


@dataclass
class IncludesSingleCrs(SingleCrspropertyType):
    class Meta:
        name = "includesSingleCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class CompoundCrstype(AbstractCrstype):
    class Meta:
        name = "CompoundCRSType"
        target_namespace = "http://www.opengis.net/gml"

    includes_single_crs: List[IncludesSingleCrs] = field(
        default_factory=list,
        metadata={
            "name": "includesSingleCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    component_reference_system: List[ComponentReferenceSystem] = field(
        default_factory=list,
        metadata={
            "name": "componentReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
class CompoundCrs(CompoundCrstype):
    """gml:CompundCRS is a coordinate reference system describing the position
    of points through two or more independent coordinate reference systems.

    It is associated with a non-repeating sequence of two or more
    instances of SingleCRS.
    """
    class Meta:
        name = "CompoundCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ScCrsPropertyType:
    class Meta:
        name = "SC_CRS_PropertyType"
        target_namespace = "http://www.isotc211.org/2005/gsr"

    compound_crs: Optional[CompoundCrs] = field(
        default=None,
        metadata={
            "name": "CompoundCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geocentric_crs: Optional[GeocentricCrs] = field(
        default=None,
        metadata={
            "name": "GeocentricCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geographic_crs: Optional[GeographicCrs] = field(
        default=None,
        metadata={
            "name": "GeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    temporal_crs: Optional[TemporalCrs] = field(
        default=None,
        metadata={
            "name": "TemporalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    image_crs: Optional[ImageCrs] = field(
        default=None,
        metadata={
            "name": "ImageCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    engineering_crs: Optional[EngineeringCrs] = field(
        default=None,
        metadata={
            "name": "EngineeringCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    vertical_crs: Optional[VerticalCrs] = field(
        default=None,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geodetic_crs: Optional[GeodeticCrs] = field(
        default=None,
        metadata={
            "name": "GeodeticCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    derived_crs: Optional[DerivedCrs] = field(
        default=None,
        metadata={
            "name": "DerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    projected_crs: Optional[ProjectedCrs] = field(
        default=None,
        metadata={
            "name": "ProjectedCRS",
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
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class CrspropertyType:
    """
    gml:CRSPropertyType is a property type for association roles to a CRS
    abstract coordinate reference system, either referencing or containing the
    definition of that CRS.
    """
    class Meta:
        name = "CRSPropertyType"
        target_namespace = "http://www.opengis.net/gml"

    compound_crs: Optional[CompoundCrs] = field(
        default=None,
        metadata={
            "name": "CompoundCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geocentric_crs: Optional[GeocentricCrs] = field(
        default=None,
        metadata={
            "name": "GeocentricCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geographic_crs: Optional[GeographicCrs] = field(
        default=None,
        metadata={
            "name": "GeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    temporal_crs: Optional[TemporalCrs] = field(
        default=None,
        metadata={
            "name": "TemporalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    image_crs: Optional[ImageCrs] = field(
        default=None,
        metadata={
            "name": "ImageCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    engineering_crs: Optional[EngineeringCrs] = field(
        default=None,
        metadata={
            "name": "EngineeringCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    vertical_crs: Optional[VerticalCrs] = field(
        default=None,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    geodetic_crs: Optional[GeodeticCrs] = field(
        default=None,
        metadata={
            "name": "GeodeticCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    derived_crs: Optional[DerivedCrs] = field(
        default=None,
        metadata={
            "name": "DerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    projected_crs: Optional[ProjectedCrs] = field(
        default=None,
        metadata={
            "name": "ProjectedCRS",
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


@dataclass
class ExVerticalExtentType(AbstractObjectType):
    """
    Vertical domain of dataset.
    """
    class Meta:
        name = "EX_VerticalExtent_Type"
        target_namespace = "http://www.isotc211.org/2005/gmd"

    minimum_value: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "minimumValue",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    maximum_value: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "maximumValue",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    vertical_crs: Optional[ScCrsPropertyType] = field(
        default=None,
        metadata={
            "name": "verticalCRS",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )


@dataclass
class SourceCrs(CrspropertyType):
    """
    gml:sourceCRS is an association role to the source CRS (coordinate
    reference system) of this coordinate operation.
    """
    class Meta:
        name = "sourceCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TargetCrs(CrspropertyType):
    """
    gml:targetCRS is an association role to the target CRS (coordinate
    reference system) of this coordinate operation.
    """
    class Meta:
        name = "targetCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ExVerticalExtent(ExVerticalExtentType):
    class Meta:
        name = "EX_VerticalExtent"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class ExVerticalExtentPropertyType:
    class Meta:
        name = "EX_VerticalExtent_PropertyType"
        target_namespace = "http://www.isotc211.org/2005/gmd"

    ex_vertical_extent: Optional[ExVerticalExtent] = field(
        default=None,
        metadata={
            "name": "EX_VerticalExtent",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
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
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )


@dataclass
class ExExtentType(AbstractObjectType):
    """
    Information about spatial, vertical, and temporal extent.
    """
    class Meta:
        name = "EX_Extent_Type"
        target_namespace = "http://www.isotc211.org/2005/gmd"

    description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    geographic_element: List[ExGeographicExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "geographicElement",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    temporal_element: List[ExTemporalExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "temporalElement",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    vertical_element: List[ExVerticalExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "verticalElement",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class ExExtent(ExExtentType):
    class Meta:
        name = "EX_Extent"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class DomainOfValidity:
    """
    The gml:domainOfValidity property implements an association role to an
    EX_Extent object as encoded in ISO/TS 19139, either referencing or
    containing the definition of that extent.
    """
    class Meta:
        name = "domainOfValidity"
        namespace = "http://www.opengis.net/gml"

    ex_extent: Optional[ExExtent] = field(
        default=None,
        metadata={
            "name": "EX_Extent",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
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


@dataclass
class AbstractCoordinateOperationType(IdentifiedObjectType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml"

    domain_of_validity: Optional[DomainOfValidity] = field(
        default=None,
        metadata={
            "name": "domainOfValidity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    scope: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        }
    )
    operation_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "operationVersion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    coordinate_operation_accuracy: List[CoordinateOperationAccuracy] = field(
        default_factory=list,
        metadata={
            "name": "coordinateOperationAccuracy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    source_crs: Optional[SourceCrs] = field(
        default=None,
        metadata={
            "name": "sourceCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    target_crs: Optional[TargetCrs] = field(
        default=None,
        metadata={
            "name": "targetCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class AbstractGeneralConversionType(AbstractCoordinateOperationType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml"


@dataclass
class ConversionType(AbstractGeneralConversionType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml"

    uses_method: Optional[UsesMethod] = field(
        default=None,
        metadata={
            "name": "usesMethod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    method: Optional[Method] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    includes_value: List[IncludesValue] = field(
        default_factory=list,
        metadata={
            "name": "includesValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    uses_value: List[UsesValue] = field(
        default_factory=list,
        metadata={
            "name": "usesValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    parameter_value: List[ParameterValue2] = field(
        default_factory=list,
        metadata={
            "name": "parameterValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )


@dataclass
class Conversion1(ConversionType):
    """gml:Conversion is a concrete operation on coordinates that does not
    include any change of Datum.

    The best-known example of a coordinate conversion is a map
    projection. The parameters describing coordinate conversions are
    defined rather than empirically derived. Note that some conversions
    have no parameters. This concrete complex type can be used without
    using a GML Application Schema that defines operation-method-
    specialized element names and contents, especially for methods with
    only one Conversion instance. The usesValue property elements are an
    unordered list of composition associations to the set of parameter
    values used by this conversion operation.
    """
    class Meta:
        name = "Conversion"
        namespace = "http://www.opengis.net/gml"
