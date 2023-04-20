from dataclasses import dataclass, field
from typing import Optional, Union
from seabeepy.metadata.gmd.md_coverage_content_type_code import MdCoverageContentTypeCode
from seabeepy.metadata.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdCoverageContentTypeCodePropertyType:
    class Meta:
        name = "MD_CoverageContentTypeCode_PropertyType"

    md_coverage_content_type_code: Optional[MdCoverageContentTypeCode] = field(
        default=None,
        metadata={
            "name": "MD_CoverageContentTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )
