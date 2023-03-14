from dataclasses import dataclass
from seabeepy.metadata.gmd.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AnchorDefinition(CodeType):
    """gml:anchorDefinition is a description, possibly including coordinates,
    of the definition used to anchor the datum to the Earth. Also known as the
    "origin", especially for engineering and image datums. The codeSpace
    attribute may be used to reference a source of more detailed on this point
    or surface, or on a set of such descriptions.

    -       For a geodetic datum, this point is also known as the fundamental point, which is traditionally the point where the relationship between geoid and ellipsoid is defined. In some cases, the "fundamental point" may consist of a number of points. In those cases, the parameters defining the geoid/ellipsoid relationship have been averaged for these points, and the averages adopted as the datum definition.
    -       For an engineering datum, the anchor definition may be a physical point, or it may be a point with defined coordinates in another CRS.may
    -       For an image datum, the anchor definition is usually either the centre of the image or the corner of the image.
    -       For a temporal datum, this attribute is not defined. Instead of the anchor definition, a temporal datum carries a separate time origin of type DateTime.
    """
    class Meta:
        name = "anchorDefinition"
        namespace = "http://www.opengis.net/gml"
