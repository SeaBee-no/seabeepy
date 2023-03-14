from dataclasses import dataclass
from seabeepy.metadata.gmd.md_keywords_type import MdKeywordsType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdKeywords(MdKeywordsType):
    class Meta:
        name = "MD_Keywords"
        namespace = "http://www.isotc211.org/2005/gmd"
