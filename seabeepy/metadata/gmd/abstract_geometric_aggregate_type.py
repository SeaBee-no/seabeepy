from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.abstract_geometry_type import AbstractGeometryType
from seabeepy.metadata.gmd.aggregation_type import AggregationType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeometricAggregateType(AbstractGeometryType):
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        }
    )
