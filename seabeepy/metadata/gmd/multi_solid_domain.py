from dataclasses import dataclass
from seabeepy.metadata.gmd.multi_solid_domain_type import MultiSolidDomainType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSolidDomain(MultiSolidDomainType):
    class Meta:
        name = "multiSolidDomain"
        namespace = "http://www.opengis.net/gml"
