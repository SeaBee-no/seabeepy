from dataclasses import dataclass
from seabeepy.metadata.gmd.md_scope_description_type import MdScopeDescriptionType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdScopeDescription(MdScopeDescriptionType):
    class Meta:
        name = "MD_ScopeDescription"
        namespace = "http://www.isotc211.org/2005/gmd"
