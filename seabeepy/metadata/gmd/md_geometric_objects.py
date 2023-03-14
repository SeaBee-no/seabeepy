from dataclasses import dataclass
from seabeepy.metadata.gmd.md_geometric_objects_type import MdGeometricObjectsType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdGeometricObjects(MdGeometricObjectsType):
    class Meta:
        name = "MD_GeometricObjects"
        namespace = "http://www.isotc211.org/2005/gmd"
