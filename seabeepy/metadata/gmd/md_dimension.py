from dataclasses import dataclass
from seabeepy.metadata.gmd.md_dimension_type import MdDimensionType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDimension(MdDimensionType):
    class Meta:
        name = "MD_Dimension"
        namespace = "http://www.isotc211.org/2005/gmd"
