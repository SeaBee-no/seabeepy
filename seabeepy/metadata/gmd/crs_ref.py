from dataclasses import dataclass
from seabeepy.metadata.gmd.abstract_crstype import CrspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CrsRef(CrspropertyType):
    """gml:crsRef is an association role either referencing or containing the
    definition of a CRS.

    This property element has been deprecated.
    """
    class Meta:
        name = "crsRef"
        namespace = "http://www.opengis.net/gml"
