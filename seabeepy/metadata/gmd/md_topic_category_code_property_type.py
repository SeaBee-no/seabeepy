from dataclasses import dataclass, field
from typing import Optional, Union
from seabeepy.metadata.gmd.md_topic_category_code_type import MdTopicCategoryCodeType
from seabeepy.metadata.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdTopicCategoryCodePropertyType:
    class Meta:
        name = "MD_TopicCategoryCode_PropertyType"

    md_topic_category_code: Optional[MdTopicCategoryCodeType] = field(
        default=None,
        metadata={
            "name": "MD_TopicCategoryCode",
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
