from dataclasses import dataclass, field
from typing import List
from seabeepy.metadata.gmd.abstract_object_type import AbstractObjectType
from seabeepy.metadata.gmd.multiplicity_range_property_type import MultiplicityRangePropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class MultiplicityType(AbstractObjectType):
    """Use to represent the possible cardinality of a relation.

    Represented by a set of simple multiplicity ranges.
    """
    class Meta:
        name = "Multiplicity_Type"

    range: List[MultiplicityRangePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
            "min_occurs": 1,
        }
    )
