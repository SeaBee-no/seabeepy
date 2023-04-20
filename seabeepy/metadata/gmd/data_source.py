from dataclasses import dataclass
from seabeepy.metadata.gmd.string_or_ref_type import StringOrRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DataSource(StringOrRefType):
    """Evidence is represented by a simple gml:dataSource or
    gml:dataSourceReference property that indicates the source of the temporal
    data.

    The remote link attributes of the gml:dataSource element have been
    deprecated along with its current type.
    """
    class Meta:
        name = "dataSource"
        namespace = "http://www.opengis.net/gml"
