from dataclasses import dataclass
from seabeepy.metadata.gmd.string_or_ref_type import StringOrRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MappingRule(StringOrRefType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
