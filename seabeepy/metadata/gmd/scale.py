from dataclasses import dataclass
from seabeepy.metadata.gmd.scale_type import ScaleType

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class Scale(ScaleType):
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"
