from dataclasses import dataclass, field
from typing import List
from seabeepy.metadata.gmd.abstract_object_type import AbstractObjectType
from seabeepy.metadata.gmd.md_digital_transfer_options_property_type import MdDigitalTransferOptionsPropertyType
from seabeepy.metadata.gmd.md_distributor_property_type import (
    MdDistributorPropertyType,
    MdFormatPropertyType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDistributionType(AbstractObjectType):
    """
    Information about the distributor of and options for obtaining the dataset.
    """
    class Meta:
        name = "MD_Distribution_Type"

    distribution_format: List[MdFormatPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "distributionFormat",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    distributor: List[MdDistributorPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    transfer_options: List[MdDigitalTransferOptionsPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "transferOptions",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
