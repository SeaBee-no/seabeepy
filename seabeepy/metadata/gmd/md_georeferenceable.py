from dataclasses import dataclass
from seabeepy.metadata.gmd.md_georeferenceable_type import MdGeoreferenceableType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdGeoreferenceable(MdGeoreferenceableType):
    class Meta:
        name = "MD_Georeferenceable"
        namespace = "http://www.isotc211.org/2005/gmd"
