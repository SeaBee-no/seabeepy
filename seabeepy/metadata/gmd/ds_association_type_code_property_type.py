from dataclasses import dataclass, field
from typing import Optional, Union
from seabeepy.metadata.gmd.ds_association_type_code import DsAssociationTypeCode
from seabeepy.metadata.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DsAssociationTypeCodePropertyType:
    class Meta:
        name = "DS_AssociationTypeCode_PropertyType"

    ds_association_type_code: Optional[DsAssociationTypeCode] = field(
        default=None,
        metadata={
            "name": "DS_AssociationTypeCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        }
    )
