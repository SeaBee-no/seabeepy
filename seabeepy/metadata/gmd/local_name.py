from dataclasses import dataclass
from seabeepy.metadata.gmd.code_type import CodeType

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class LocalName(CodeType):
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"
