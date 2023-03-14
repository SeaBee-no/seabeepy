from dataclasses import dataclass, field
from typing import List
from seabeepy.metadata.gmd.abstract_object_type import AbstractObjectType
from seabeepy.metadata.gmd.character_string_property_type import CharacterStringPropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdConstraintsType(AbstractObjectType):
    """
    Restrictions on the access and use of a dataset or metadata.
    """
    class Meta:
        name = "MD_Constraints_Type"

    use_limitation: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "useLimitation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
