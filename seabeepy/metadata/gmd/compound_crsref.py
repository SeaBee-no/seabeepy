from dataclasses import dataclass
from seabeepy.metadata.gmd.compound_crsproperty_type import CompoundCrspropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CompoundCrsref(CompoundCrspropertyType):
    class Meta:
        name = "compoundCRSRef"
        namespace = "http://www.opengis.net/gml"
