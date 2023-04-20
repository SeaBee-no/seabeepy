from dataclasses import dataclass
from seabeepy.metadata.gmd.multi_point_type import MultiPointType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiPoint(MultiPointType):
    """A gml:MultiPoint consists of one or more gml:Points.

    The members of the geometric aggregate may be specified either using
    the "standard" property (gml:pointMember) or the array property
    (gml:pointMembers). It is also valid to use both the "standard" and
    the array properties in the same collection.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
