from dataclasses import dataclass
from seabeepy.metadata.gmd.abstract_crstype import EngineeringDatumPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EngineeringDatumRef(EngineeringDatumPropertyType):
    class Meta:
        name = "engineeringDatumRef"
        namespace = "http://www.opengis.net/gml"
