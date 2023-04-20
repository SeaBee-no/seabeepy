from dataclasses import dataclass
from seabeepy.metadata.gmd.abstract_time_object_type import AbstractTimeObjectType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractTimeComplexType(AbstractTimeObjectType):
    pass
