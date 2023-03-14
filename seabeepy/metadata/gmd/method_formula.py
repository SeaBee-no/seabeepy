from dataclasses import dataclass
from seabeepy.metadata.gmd.code_type import CodeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MethodFormula(CodeType):
    class Meta:
        name = "methodFormula"
        namespace = "http://www.opengis.net/gml"
