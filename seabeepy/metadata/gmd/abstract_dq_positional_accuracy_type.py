from dataclasses import dataclass
from seabeepy.metadata.gmd.abstract_dq_element_type import AbstractDqElementType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractDqPositionalAccuracyType(AbstractDqElementType):
    class Meta:
        name = "AbstractDQ_PositionalAccuracy_Type"
