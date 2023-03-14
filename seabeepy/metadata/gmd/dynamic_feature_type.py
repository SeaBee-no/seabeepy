from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.abstract_feature_type import AbstractFeatureType
from seabeepy.metadata.gmd.data_source import DataSource
from seabeepy.metadata.gmd.data_source_reference import DataSourceReference
from seabeepy.metadata.gmd.history import History
from seabeepy.metadata.gmd.track import Track
from seabeepy.metadata.gmd.valid_time import ValidTime

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DynamicFeatureType(AbstractFeatureType):
    valid_time: Optional[ValidTime] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    track: Optional[Track] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    history: Optional[History] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    data_source: Optional[DataSource] = field(
        default=None,
        metadata={
            "name": "dataSource",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    data_source_reference: Optional[DataSourceReference] = field(
        default=None,
        metadata={
            "name": "dataSourceReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
