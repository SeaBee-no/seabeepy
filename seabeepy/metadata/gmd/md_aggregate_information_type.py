from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.abstract_object_type import AbstractObjectType
from seabeepy.metadata.gmd.ci_citation_type import (
    CiCitationPropertyType,
    MdIdentifierPropertyType,
)
from seabeepy.metadata.gmd.ds_association_type_code_property_type import DsAssociationTypeCodePropertyType
from seabeepy.metadata.gmd.ds_initiative_type_code_property_type import DsInitiativeTypeCodePropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdAggregateInformationType(AbstractObjectType):
    """
    Encapsulates the dataset aggregation information.
    """
    class Meta:
        name = "MD_AggregateInformation_Type"

    aggregate_data_set_name: Optional[CiCitationPropertyType] = field(
        default=None,
        metadata={
            "name": "aggregateDataSetName",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    aggregate_data_set_identifier: Optional[MdIdentifierPropertyType] = field(
        default=None,
        metadata={
            "name": "aggregateDataSetIdentifier",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    association_type: Optional[DsAssociationTypeCodePropertyType] = field(
        default=None,
        metadata={
            "name": "associationType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    initiative_type: Optional[DsInitiativeTypeCodePropertyType] = field(
        default=None,
        metadata={
            "name": "initiativeType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
