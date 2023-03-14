from dataclasses import dataclass
from seabeepy.metadata.gmd.string_or_ref_type import StringOrRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Status(StringOrRefType):
    """
    The remote link attributes of the gml:status element have been deprecated
    along with its current type.
    """
    class Meta:
        name = "status"
        namespace = "http://www.opengis.net/gml"
