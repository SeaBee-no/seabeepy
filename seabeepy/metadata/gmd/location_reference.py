from dataclasses import dataclass
from seabeepy.metadata.gmd.reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LocationReference(ReferenceType):
    """
    The gml:locationReference property element is a convenience property where
    the text value referenced by the xlink:href attribute describes the
    location of the feature.
    """
    class Meta:
        name = "locationReference"
        namespace = "http://www.opengis.net/gml"
