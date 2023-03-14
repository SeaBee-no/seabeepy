from dataclasses import dataclass, field
from typing import List
from seabeepy.metadata.gmd.abstract_object_type import AbstractObjectType
from seabeepy.metadata.gmd.ci_citation_type import CiCitationPropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdPortrayalCatalogueReferenceType(AbstractObjectType):
    """
    Information identifing the portrayal catalogue used.
    """
    class Meta:
        name = "MD_PortrayalCatalogueReference_Type"

    portrayal_catalogue_citation: List[CiCitationPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "portrayalCatalogueCitation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "min_occurs": 1,
        }
    )
