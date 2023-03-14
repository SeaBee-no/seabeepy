from dataclasses import dataclass
from seabeepy.metadata.gmd.abstract_crstype import GeodeticDatumPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeodeticDatumRef(GeodeticDatumPropertyType):
    class Meta:
        name = "geodeticDatumRef"
        namespace = "http://www.opengis.net/gml"
