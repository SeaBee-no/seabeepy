from dataclasses import dataclass
from seabeepy.metadata.gmd.binary_type import BinaryType

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class Binary(BinaryType):
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"
