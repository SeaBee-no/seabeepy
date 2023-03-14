from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.abstract_md_content_information_type import AbstractMdContentInformationType
from seabeepy.metadata.gmd.boolean_property_type_2 import BooleanPropertyType2
from seabeepy.metadata.gmd.character_string_property_type import CharacterStringPropertyType
from seabeepy.metadata.gmd.ci_citation_type import CiCitationPropertyType
from seabeepy.metadata.gmd.generic_name_property_type import GenericNamePropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdFeatureCatalogueDescriptionType(AbstractMdContentInformationType):
    """
    Information identifing the feature catalogue.
    """
    class Meta:
        name = "MD_FeatureCatalogueDescription_Type"

    compliance_code: Optional[BooleanPropertyType2] = field(
        default=None,
        metadata={
            "name": "complianceCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    language: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    included_with_dataset: Optional[BooleanPropertyType2] = field(
        default=None,
        metadata={
            "name": "includedWithDataset",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    feature_types: List[GenericNamePropertyType] = field(
        default_factory=list,
        metadata={
            "name": "featureTypes",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    feature_catalogue_citation: List[CiCitationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "featureCatalogueCitation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )
