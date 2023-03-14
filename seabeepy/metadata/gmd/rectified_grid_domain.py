from dataclasses import dataclass
from seabeepy.metadata.gmd.rectified_grid_domain_type import RectifiedGridDomainType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RectifiedGridDomain(RectifiedGridDomainType):
    class Meta:
        name = "rectifiedGridDomain"
        namespace = "http://www.opengis.net/gml"
