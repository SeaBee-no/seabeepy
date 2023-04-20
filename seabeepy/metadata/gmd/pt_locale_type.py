from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.abstract_object_type import AbstractObjectType
from seabeepy.metadata.gmd.country_property_type import CountryPropertyType
from seabeepy.metadata.gmd.language_code_property_type import LanguageCodePropertyType
from seabeepy.metadata.gmd.md_character_set_code_property_type import MdCharacterSetCodePropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class PtLocaleType(AbstractObjectType):
    class Meta:
        name = "PT_Locale_Type"

    language_code: Optional[LanguageCodePropertyType] = field(
        default=None,
        metadata={
            "name": "languageCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    country: Optional[CountryPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    character_encoding: Optional[MdCharacterSetCodePropertyType] = field(
        default=None,
        metadata={
            "name": "characterEncoding",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
