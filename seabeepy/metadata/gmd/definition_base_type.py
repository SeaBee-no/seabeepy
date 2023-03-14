from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.description import Description
from seabeepy.metadata.gmd.description_reference import DescriptionReference
from seabeepy.metadata.gmd.identifier import Identifier
from seabeepy.metadata.gmd.meta_data_property import MetaDataProperty
from seabeepy.metadata.gmd.name import Name

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DefinitionBaseType:
    meta_data_property: List[MetaDataProperty] = field(
        default_factory=list,
        metadata={
            "name": "metaDataProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    description_reference: Optional[DescriptionReference] = field(
        default=None,
        metadata={
            "name": "descriptionReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    name: List[Name] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
