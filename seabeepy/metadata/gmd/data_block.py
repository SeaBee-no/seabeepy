from dataclasses import dataclass
from seabeepy.metadata.gmd.data_block_type import DataBlockType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DataBlock(DataBlockType):
    """gml:DataBlock describes the Range as a block of text encoded values
    similar to a Common Separated Value (CSV) representation.

    The range set parameterization is described by the property
    gml:rangeParameters.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
