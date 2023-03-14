from seabeepy.metadata.gmd import *
from typing import List

ADDRESSER = CharacterStringPropertyType(character_string="Adresser")
ORTOFOTO = CharacterStringPropertyType(character_string="Ortofoto")


def norwegian_md_keywords(tkeywords: List[str] = []) -> MdKeywordsPropertyType:
    """Template MdKeywordsPropertyType

    Add norwegian inspire tkeywords from https://register.geonorge.no/metadata-kodelister/inspiretema
    to a MdKeywordsPropertyType with a norwegian thesarus.
    """
    return MdKeywordsPropertyType(
        md_keywords=MdKeywords(
            keyword=[
                CharacterStringPropertyType(character_string=k) for k in tkeywords
            ],
            type=None,
            thesaurus_name=CiCitationPropertyType(
                ci_citation=CiCitation(
                    id=None,
                    uuid=None,
                    title=CharacterStringPropertyType(
                        character_string="Nasjonal tematisk inndeling (DOK-kategori)",
                    ),
                    alternate_title=[],
                    date=[
                        CiDatePropertyType(
                            ci_date=CiDate(
                                id=None,
                                uuid=None,
                                date=DatePropertyType(
                                    date=None, date_time=None, nil_reason=None
                                ),
                                date_type=CiDateTypeCodePropertyType(
                                    ci_date_type_code=CiDateTypeCode(
                                        value="pubblicazione",
                                        code_list="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI_DateTypeCode",
                                        code_list_value="publication",
                                        code_space=None,
                                    ),
                                    nil_reason=None,
                                ),
                            ),
                        )
                    ],
                ),
            ),
        ),
    )


def custom_keywords(keywords: List[str]) -> MdKeywordsPropertyType:
    return MdKeywordsPropertyType(
        md_keywords=MdKeywords(
            keyword=[
                CharacterStringPropertyType(
                    character_string=k,
                ) for k in keywords
            ],
            type=MdKeywordTypeCodePropertyType(
                md_keyword_type_code=MdKeywordTypeCode(
                    value="theme",
                    code_list="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#MD_KeywordTypeCode",
                    code_list_value="theme",
                    code_space="ISOTC211/19115",
                ),
            ),
            thesaurus_name=None,
        ),
    )
