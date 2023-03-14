from dataclasses import dataclass
from seabeepy.metadata.gmd.generic_meta_data_type import GenericMetaDataType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GenericMetaData(GenericMetaDataType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
