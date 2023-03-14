from dataclasses import dataclass
from seabeepy.metadata.gmd.reference_type import ReferenceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class StatusReference(ReferenceType):
    class Meta:
        name = "statusReference"
        namespace = "http://www.opengis.net/gml"
