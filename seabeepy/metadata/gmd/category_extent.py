from dataclasses import dataclass
from seabeepy.metadata.gmd.category_extent_type import CategoryExtentType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CategoryExtent(CategoryExtentType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
