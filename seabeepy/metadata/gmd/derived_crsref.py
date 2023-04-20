from dataclasses import dataclass
from seabeepy.metadata.gmd.derived_crsproperty_type import DerivedCrspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DerivedCrsref(DerivedCrspropertyType):
    class Meta:
        name = "derivedCRSRef"
        namespace = "http://www.opengis.net/gml"
