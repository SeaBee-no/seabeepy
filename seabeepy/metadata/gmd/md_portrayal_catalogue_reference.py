from dataclasses import dataclass
from seabeepy.metadata.gmd.md_portrayal_catalogue_reference_type import MdPortrayalCatalogueReferenceType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdPortrayalCatalogueReference(MdPortrayalCatalogueReferenceType):
    class Meta:
        name = "MD_PortrayalCatalogueReference"
        namespace = "http://www.isotc211.org/2005/gmd"
