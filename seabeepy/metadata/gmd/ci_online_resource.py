from dataclasses import dataclass
from seabeepy.metadata.gmd.ci_online_resource_type import CiOnlineResourceType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiOnlineResource(CiOnlineResourceType):
    class Meta:
        name = "CI_OnlineResource"
        namespace = "http://www.isotc211.org/2005/gmd"
