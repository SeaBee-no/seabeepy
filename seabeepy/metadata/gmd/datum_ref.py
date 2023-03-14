from dataclasses import dataclass
from seabeepy.metadata.gmd.datum_property_type import DatumPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DatumRef(DatumPropertyType):
    class Meta:
        name = "datumRef"
        namespace = "http://www.opengis.net/gml"
