from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.abstract_object_type import AbstractObjectType
from seabeepy.metadata.gmd.binary_property_type import BinaryPropertyType
from seabeepy.metadata.gmd.character_string_property_type import CharacterStringPropertyType
from seabeepy.metadata.gmd.ci_citation_type import CiCitationPropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdApplicationSchemaInformationType(AbstractObjectType):
    """
    Information about the application schema used to build the dataset.
    """
    class Meta:
        name = "MD_ApplicationSchemaInformation_Type"

    name: Optional[CiCitationPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    schema_language: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "schemaLanguage",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    constraint_language: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "constraintLanguage",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    schema_ascii: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "schemaAscii",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    graphics_file: Optional[BinaryPropertyType] = field(
        default=None,
        metadata={
            "name": "graphicsFile",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    software_development_file: Optional[BinaryPropertyType] = field(
        default=None,
        metadata={
            "name": "softwareDevelopmentFile",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    software_development_file_format: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "softwareDevelopmentFileFormat",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
