from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.md_topic_category_code_type import MdTopicCategoryCodeType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdTopicCategoryCode:
    class Meta:
        name = "MD_TopicCategoryCode"
        namespace = "http://www.isotc211.org/2005/gmd"

    value: Optional[MdTopicCategoryCodeType] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
