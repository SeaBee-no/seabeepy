from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.abstract_md_content_information_type import AbstractMdContentInformationType
from seabeepy.metadata.gmd.md_coverage_content_type_code_property_type import MdCoverageContentTypeCodePropertyType
from seabeepy.metadata.gmd.md_range_dimension_property_type import MdRangeDimensionPropertyType
from seabeepy.metadata.gmd.record_type_property_type import RecordTypePropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdCoverageDescriptionType(AbstractMdContentInformationType):
    """
    Information about the domain of the raster cell.
    """
    class Meta:
        name = "MD_CoverageDescription_Type"

    attribute_description: Optional[RecordTypePropertyType] = field(
        default=None,
        metadata={
            "name": "attributeDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    content_type: Optional[MdCoverageContentTypeCodePropertyType] = field(
        default=None,
        metadata={
            "name": "contentType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    dimension: List[MdRangeDimensionPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
