from dataclasses import dataclass
from seabeepy.metadata.gmd.cylindrical_cstype import CylindricalCstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CylindricalCs(CylindricalCstype):
    """gml:CylindricalCS is a three-dimensional coordinate system consisting of
    a polar coordinate system extended by a straight coordinate axis
    perpendicular to the plane spanned by the polar coordinate system.

    A CylindricalCS shall have three gml:axis property elements.
    """
    class Meta:
        name = "CylindricalCS"
        namespace = "http://www.opengis.net/gml"
