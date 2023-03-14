from xsdata.formats.dataclass import parsers
from typing import List
from seabeepy.metadata import gmd
from seabeepy.metadata import templates
from owslib.csw import CatalogueServiceWeb

def fetch_dataset_iso(uuid: str, geonode_url: str) -> gmd.MdMetadata:
    """Fetch iso metadata from pycsw
    
    
    Returns a python representation of the iso xml using http://www.isotc211.org/2005/gmd.
    """

    # Should watch out for missing properties
    parser = parsers.XmlParser(config=parsers.config.ParserConfig(fail_on_unknown_properties=False))
    csw = CatalogueServiceWeb(f'{geonode_url}/catalogue/csw')
    csw.getrecordbyid(id=[uuid], outputschema="http://www.isotc211.org/2005/gmd")
    iso_record = csw.records[uuid]

    return parser.from_bytes(iso_record.xml, gmd.MdMetadata)

def add_norwegian_thesarus_keywords(ds_metadata: gmd.MdMetadata, tkeywords: List[str]) -> gmd.MdMetadata:
    """Add a list of norwegian keywords

    Adds descriptive keywords with a thesarus called Nasjonal tematisk inndeling (DOK-kategori),
    also see  https://register.geonorge.no/metadata-kodelister/inspiretema or seabee geonode.
    NOTE: The rdf file must be loaded in geonode first
    """
    des_keywords = ds_metadata.identification_info[0].md_data_identification.descriptive_keywords
    des_keywords.append(templates.norwegian_md_keywords(tkeywords))

    return ds_metadata

def remove_norwegian_thesarus(ds_metadata: gmd.MdMetadata) -> gmd.MdMetadata:
    """Remove norwegian thesarus

    Remove thesarus with name Nasjonal tematisk inndeling (DOK-kategori).
    """
    des_keywords = ds_metadata.identification_info[0].md_data_identification.descriptive_keywords

    thesarus_filtered = [dk for dk in  des_keywords if thesarus_name(dk) != "Nasjonal tematisk inndeling (DOK-kategori)"]

    ds_metadata.identification_info[0].md_data_identification.descriptive_keywords = thesarus_filtered

    return ds_metadata

def add_seabee_keywords(ds_metadata: gmd.MdMetadata, keywords: List[str]) -> gmd.MdMetadata:
    """Add a list of custom seabee keywords
    """
    des_keywords = ds_metadata.identification_info[0].md_data_identification.descriptive_keywords
    des_keywords.append(templates.custom_keywords(keywords))

    return ds_metadata

def remove_all_keywords(ds_metadata: gmd.MdMetadata) -> gmd.MdMetadata:
    """Remove all descriptive keywords
    """

    ds_metadata.identification_info[0].md_data_identification.descriptive_keywords = []

    return ds_metadata

def thesarus_name(keyword: gmd.MdKeywordsPropertyType) -> str:
    """Getter for thesarus name"""
    if keyword.md_keywords.thesaurus_name is None:
        return ""
    return keyword.md_keywords.thesaurus_name.ci_citation.title.character_string