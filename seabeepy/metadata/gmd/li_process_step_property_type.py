from dataclasses import dataclass, field
from typing import List, Optional, Union
from seabeepy.metadata.gmd.abstract_object_type import AbstractObjectType
from seabeepy.metadata.gmd.actuate_value import ActuateValue
from seabeepy.metadata.gmd.character_string_property_type import CharacterStringPropertyType
from seabeepy.metadata.gmd.ci_citation_type import CiCitationPropertyType
from seabeepy.metadata.gmd.ci_responsible_party_property_type import CiResponsiblePartyPropertyType
from seabeepy.metadata.gmd.date_time_property_type import DateTimePropertyType
from seabeepy.metadata.gmd.ex_extent_property_type import ExExtentPropertyType
from seabeepy.metadata.gmd.md_reference_system_property_type import MdReferenceSystemPropertyType
from seabeepy.metadata.gmd.md_representative_fraction_property_type import MdRepresentativeFractionPropertyType
from seabeepy.metadata.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue
from seabeepy.metadata.gmd.show_value import ShowValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class LiProcessStepPropertyType:
    class Meta:
        name = "LI_ProcessStep_PropertyType"

    li_process_step: Optional["LiProcessStep"] = field(
        default=None,
        metadata={
            "name": "LI_ProcessStep",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    type: str = field(
        init=False,
        default="simple",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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


@dataclass
class LiSourceType(AbstractObjectType):
    class Meta:
        name = "LI_Source_Type"

    description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    scale_denominator: Optional[MdRepresentativeFractionPropertyType] = field(
        default=None,
        metadata={
            "name": "scaleDenominator",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    source_reference_system: Optional[MdReferenceSystemPropertyType] = field(
        default=None,
        metadata={
            "name": "sourceReferenceSystem",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    source_citation: Optional[CiCitationPropertyType] = field(
        default=None,
        metadata={
            "name": "sourceCitation",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    source_extent: List[ExExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "sourceExtent",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    source_step: List[LiProcessStepPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "sourceStep",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class LiSource(LiSourceType):
    class Meta:
        name = "LI_Source"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class LiSourcePropertyType:
    class Meta:
        name = "LI_Source_PropertyType"

    li_source: Optional[LiSource] = field(
        default=None,
        metadata={
            "name": "LI_Source",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    type: str = field(
        init=False,
        default="simple",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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


@dataclass
class LiProcessStepType(AbstractObjectType):
    class Meta:
        name = "LI_ProcessStep_Type"

    description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    rationale: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    date_time: Optional[DateTimePropertyType] = field(
        default=None,
        metadata={
            "name": "dateTime",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    processor: List[CiResponsiblePartyPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    source: List[LiSourcePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )


@dataclass
class LiProcessStep(LiProcessStepType):
    class Meta:
        name = "LI_ProcessStep"
        namespace = "http://www.isotc211.org/2005/gmd"
