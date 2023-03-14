from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.catalog_symbol import CatalogSymbol
from seabeepy.metadata.gmd.definition_type import DefinitionType
from seabeepy.metadata.gmd.quantity_type import QuantityType
from seabeepy.metadata.gmd.quantity_type_reference import QuantityTypeReference

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UnitDefinitionType(DefinitionType):
    quantity_type: Optional[QuantityType] = field(
        default=None,
        metadata={
            "name": "quantityType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    quantity_type_reference: Optional[QuantityTypeReference] = field(
        default=None,
        metadata={
            "name": "quantityTypeReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    catalog_symbol: Optional[CatalogSymbol] = field(
        default=None,
        metadata={
            "name": "catalogSymbol",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
