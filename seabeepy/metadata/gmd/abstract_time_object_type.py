from dataclasses import dataclass
from seabeepy.metadata.gmd.abstract_gmltype import AbstractGmltype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractTimeObjectType(AbstractGmltype):
    pass
