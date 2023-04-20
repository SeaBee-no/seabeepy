from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.character_string_property_type import CharacterStringPropertyType
from seabeepy.metadata.gmd.pt_free_text import PtFreeText

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class PtFreeTextPropertyType(CharacterStringPropertyType):
    class Meta:
        name = "PT_FreeText_PropertyType"

    pt_free_text: Optional[PtFreeText] = field(
        default=None,
        metadata={
            "name": "PT_FreeText",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
