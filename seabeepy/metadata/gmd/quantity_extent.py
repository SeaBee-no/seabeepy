from dataclasses import dataclass
from seabeepy.metadata.gmd.quantity_extent_type import QuantityExtentType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class QuantityExtent(QuantityExtentType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
