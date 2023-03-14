from seabeepy.metadata.gmd.abstract_continuous_coverage_type import AbstractContinuousCoverageType
from seabeepy.metadata.gmd.abstract_coordinate_system_type import AbstractCoordinateSystemType
from seabeepy.metadata.gmd.abstract_coverage_type import AbstractCoverageType
from seabeepy.metadata.gmd.abstract_crstype import (
    AbstractCrstype,
    AbstractCoordinateOperationType,
    AbstractDatumType,
    AbstractGeneralConversionType,
    AbstractGeneralDerivedCrstype,
    CrspropertyType,
    CompoundCrs,
    CompoundCrstype,
    ConversionType,
    Conversion1,
    DerivedCrs,
    DerivedCrstype1,
    ExExtent,
    ExExtentType,
    ExVerticalExtent,
    ExVerticalExtentPropertyType,
    ExVerticalExtentType,
    EngineeringCrs,
    EngineeringCrstype,
    EngineeringDatumPropertyType,
    EngineeringDatumType,
    EngineeringDatum1,
    GeneralConversionPropertyType,
    GeocentricCrs,
    GeocentricCrstype,
    GeodeticCrs,
    GeodeticCrspropertyType,
    GeodeticCrstype,
    GeodeticDatumPropertyType,
    GeodeticDatumType,
    GeodeticDatum1,
    GeographicCrs,
    GeographicCrspropertyType,
    GeographicCrstype,
    ImageCrs,
    ImageCrstype,
    ImageDatumPropertyType,
    ImageDatumType,
    ImageDatum1,
    ProjectedCrs,
    ProjectedCrstype,
    ScCrsPropertyType,
    SingleCrspropertyType,
    TemporalCrs,
    TemporalCrstype,
    TemporalDatumBaseType,
    TemporalDatumPropertyType,
    TemporalDatumType,
    TemporalDatum1,
    VerticalCrs,
    VerticalCrstype,
    VerticalDatumPropertyType,
    VerticalDatumType,
    VerticalDatum1,
    BaseCrs,
    BaseGeodeticCrs,
    BaseGeographicCrs,
    ComponentReferenceSystem,
    Conversion2,
    DefinedByConversion,
    DomainOfValidity,
    EngineeringDatum2,
    GeodeticDatum2,
    ImageDatum2,
    IncludesSingleCrs,
    SourceCrs,
    TargetCrs,
    TemporalDatum2,
    UsesEngineeringDatum,
    UsesGeodeticDatum,
    UsesImageDatum,
    UsesTemporalDatum,
    UsesVerticalDatum,
    VerticalDatum2,
)
from seabeepy.metadata.gmd.abstract_curve_segment_type import AbstractCurveSegmentType
from seabeepy.metadata.gmd.abstract_curve_type import AbstractCurveType
from seabeepy.metadata.gmd.abstract_discrete_coverage_type import AbstractDiscreteCoverageType
from seabeepy.metadata.gmd.abstract_dq_completeness_type import AbstractDqCompletenessType
from seabeepy.metadata.gmd.abstract_dq_element_type import AbstractDqElementType
from seabeepy.metadata.gmd.abstract_dq_logical_consistency_type import AbstractDqLogicalConsistencyType
from seabeepy.metadata.gmd.abstract_dq_positional_accuracy_type import AbstractDqPositionalAccuracyType
from seabeepy.metadata.gmd.abstract_dq_result_type import AbstractDqResultType
from seabeepy.metadata.gmd.abstract_dq_temporal_accuracy_type import AbstractDqTemporalAccuracyType
from seabeepy.metadata.gmd.abstract_dq_thematic_accuracy_type import AbstractDqThematicAccuracyType
from seabeepy.metadata.gmd.abstract_ex_geographic_extent_type import AbstractExGeographicExtentType
from seabeepy.metadata.gmd.abstract_feature_member_type import AbstractFeatureMemberType
from seabeepy.metadata.gmd.abstract_feature_type import AbstractFeatureType
from seabeepy.metadata.gmd.abstract_general_operation_parameter_property_type import (
    AbstractGeneralOperationParameterPropertyType,
    OperationParameterGroup,
    OperationParameterGroupType,
    GeneralOperationParameter,
    UsesParameter,
)
from seabeepy.metadata.gmd.abstract_general_operation_parameter_ref import AbstractGeneralOperationParameterRef
from seabeepy.metadata.gmd.abstract_general_operation_parameter_type import AbstractGeneralOperationParameterType
from seabeepy.metadata.gmd.abstract_general_parameter_value_property_type import (
    AbstractGeneralParameterValuePropertyType,
    ParameterValueGroup,
    ParameterValueGroupType,
    IncludesValue,
    ParameterValue2,
    UsesValue,
)
from seabeepy.metadata.gmd.abstract_general_parameter_value_type import AbstractGeneralParameterValueType
from seabeepy.metadata.gmd.abstract_general_transformation_type import AbstractGeneralTransformationType
from seabeepy.metadata.gmd.abstract_geometric_aggregate_type import AbstractGeometricAggregateType
from seabeepy.metadata.gmd.abstract_geometric_primitive_type import AbstractGeometricPrimitiveType
from seabeepy.metadata.gmd.abstract_geometry_type import AbstractGeometryType
from seabeepy.metadata.gmd.abstract_gmltype import AbstractGmltype
from seabeepy.metadata.gmd.abstract_gridded_surface_type import AbstractGriddedSurfaceType
from seabeepy.metadata.gmd.abstract_md_content_information_type import AbstractMdContentInformationType
from seabeepy.metadata.gmd.abstract_md_identification_type import AbstractMdIdentificationType
from seabeepy.metadata.gmd.abstract_md_spatial_representation_type import AbstractMdSpatialRepresentationType
from seabeepy.metadata.gmd.abstract_member_type import AbstractMemberType
from seabeepy.metadata.gmd.abstract_meta_data_type import AbstractMetaDataType
from seabeepy.metadata.gmd.abstract_metadata_property_type import AbstractMetadataPropertyType
from seabeepy.metadata.gmd.abstract_object_type import AbstractObjectType
from seabeepy.metadata.gmd.abstract_parametric_curve_surface_type import AbstractParametricCurveSurfaceType
from seabeepy.metadata.gmd.abstract_ring_property_type import AbstractRingPropertyType
from seabeepy.metadata.gmd.abstract_ring_type import AbstractRingType
from seabeepy.metadata.gmd.abstract_rs_reference_system_type import AbstractRsReferenceSystemType
from seabeepy.metadata.gmd.abstract_solid_type import AbstractSolidType
from seabeepy.metadata.gmd.abstract_surface_patch_type import AbstractSurfacePatchType
from seabeepy.metadata.gmd.abstract_surface_type import AbstractSurfaceType
from seabeepy.metadata.gmd.abstract_time_complex_type import AbstractTimeComplexType
from seabeepy.metadata.gmd.abstract_time_object_type import AbstractTimeObjectType
from seabeepy.metadata.gmd.abstract_time_slice_type import AbstractTimeSliceType
from seabeepy.metadata.gmd.abstract_topology_type import AbstractTopologyType
from seabeepy.metadata.gmd.actuate_value import ActuateValue
from seabeepy.metadata.gmd.affine_cs_1 import AffineCs1
from seabeepy.metadata.gmd.affine_cs_2 import AffineCs2
from seabeepy.metadata.gmd.affine_csproperty_type import AffineCspropertyType
from seabeepy.metadata.gmd.affine_cstype import AffineCstype
from seabeepy.metadata.gmd.affine_placement import AffinePlacement
from seabeepy.metadata.gmd.affine_placement_type import AffinePlacementType
from seabeepy.metadata.gmd.aggregation_type import AggregationType
from seabeepy.metadata.gmd.anchor_definition import AnchorDefinition
from seabeepy.metadata.gmd.anchor_point import AnchorPoint
from seabeepy.metadata.gmd.angle_1 import Angle1
from seabeepy.metadata.gmd.angle_2 import Angle2
from seabeepy.metadata.gmd.angle_choice_type import AngleChoiceType
from seabeepy.metadata.gmd.angle_property_type import AnglePropertyType
from seabeepy.metadata.gmd.angle_type import AngleType
from seabeepy.metadata.gmd.arc import Arc
from seabeepy.metadata.gmd.arc_by_bulge import ArcByBulge
from seabeepy.metadata.gmd.arc_by_bulge_type import ArcByBulgeType
from seabeepy.metadata.gmd.arc_by_center_point import ArcByCenterPoint
from seabeepy.metadata.gmd.arc_by_center_point_type import ArcByCenterPointType
from seabeepy.metadata.gmd.arc_string import ArcString
from seabeepy.metadata.gmd.arc_string_by_bulge import ArcStringByBulge
from seabeepy.metadata.gmd.arc_string_by_bulge_type import ArcStringByBulgeType
from seabeepy.metadata.gmd.arc_string_type import ArcStringType
from seabeepy.metadata.gmd.arc_type import ArcType
from seabeepy.metadata.gmd.area_type import AreaType
from seabeepy.metadata.gmd.association_name import AssociationName
from seabeepy.metadata.gmd.axis import Axis
from seabeepy.metadata.gmd.axis_abbrev import AxisAbbrev
from seabeepy.metadata.gmd.axis_direction import AxisDirection
from seabeepy.metadata.gmd.bag_type import (
    AbstractFeatureCollectionType,
    Array,
    ArrayAssociationType,
    ArrayType,
    AssociationRoleType,
    Bag,
    BagType,
    DirectedObservation,
    DirectedObservationAtDistance,
    DirectedObservationAtDistanceType,
    DirectedObservationType,
    FeatureArrayPropertyType,
    FeatureCollection,
    FeatureCollectionType,
    FeaturePropertyType,
    Observation,
    ObservationType,
    ProcedurePropertyType,
    ResultType,
    TargetPropertyType,
    FeatureMember,
    FeatureMembers,
    Member,
    Members,
    ResultOf,
    Subject,
    Target,
    Using,
)
from seabeepy.metadata.gmd.base_unit import BaseUnit
from seabeepy.metadata.gmd.base_unit_type import BaseUnitType
from seabeepy.metadata.gmd.bezier import Bezier
from seabeepy.metadata.gmd.bezier_type import BezierType
from seabeepy.metadata.gmd.binary import Binary
from seabeepy.metadata.gmd.binary_property_type import BinaryPropertyType
from seabeepy.metadata.gmd.binary_type import BinaryType
from seabeepy.metadata.gmd.boolean_1 import Boolean1
from seabeepy.metadata.gmd.boolean_2 import Boolean2
from seabeepy.metadata.gmd.boolean_list import BooleanList
from seabeepy.metadata.gmd.boolean_property_type_1 import BooleanPropertyType1
from seabeepy.metadata.gmd.boolean_property_type_2 import BooleanPropertyType2
from seabeepy.metadata.gmd.boolean_value import BooleanValue
from seabeepy.metadata.gmd.bounded_by import BoundedBy
from seabeepy.metadata.gmd.bounded_feature_type import BoundedFeatureType
from seabeepy.metadata.gmd.bounding_shape_type import BoundingShapeType
from seabeepy.metadata.gmd.bspline import Bspline
from seabeepy.metadata.gmd.bspline_type import BsplineType
from seabeepy.metadata.gmd.cartesian_cs_1 import CartesianCs1
from seabeepy.metadata.gmd.cartesian_cs_2 import CartesianCs2
from seabeepy.metadata.gmd.cartesian_csproperty_type import CartesianCspropertyType
from seabeepy.metadata.gmd.cartesian_csref import CartesianCsref
from seabeepy.metadata.gmd.cartesian_cstype import CartesianCstype
from seabeepy.metadata.gmd.catalog_symbol import CatalogSymbol
from seabeepy.metadata.gmd.category import Category
from seabeepy.metadata.gmd.category_extent import CategoryExtent
from seabeepy.metadata.gmd.category_extent_type import CategoryExtentType
from seabeepy.metadata.gmd.category_list import CategoryList
from seabeepy.metadata.gmd.category_property_type import CategoryPropertyType
from seabeepy.metadata.gmd.center_line_of import CenterLineOf
from seabeepy.metadata.gmd.center_of import CenterOf
from seabeepy.metadata.gmd.character_string import CharacterString
from seabeepy.metadata.gmd.character_string_property_type import CharacterStringPropertyType
from seabeepy.metadata.gmd.ci_address import CiAddress
from seabeepy.metadata.gmd.ci_address_property_type import CiAddressPropertyType
from seabeepy.metadata.gmd.ci_address_type import CiAddressType
from seabeepy.metadata.gmd.ci_citation_type import (
    CiCitation,
    CiCitationPropertyType,
    CiCitationType,
    MdIdentifier,
    MdIdentifierPropertyType,
    MdIdentifierType,
    RsIdentifier,
    RsIdentifierType,
)
from seabeepy.metadata.gmd.ci_contact import CiContact
from seabeepy.metadata.gmd.ci_contact_property_type import CiContactPropertyType
from seabeepy.metadata.gmd.ci_contact_type import CiContactType
from seabeepy.metadata.gmd.ci_date import CiDate
from seabeepy.metadata.gmd.ci_date_property_type import CiDatePropertyType
from seabeepy.metadata.gmd.ci_date_type import CiDateType
from seabeepy.metadata.gmd.ci_date_type_code import CiDateTypeCode
from seabeepy.metadata.gmd.ci_date_type_code_property_type import CiDateTypeCodePropertyType
from seabeepy.metadata.gmd.ci_on_line_function_code import CiOnLineFunctionCode
from seabeepy.metadata.gmd.ci_on_line_function_code_property_type import CiOnLineFunctionCodePropertyType
from seabeepy.metadata.gmd.ci_online_resource import CiOnlineResource
from seabeepy.metadata.gmd.ci_online_resource_property_type import CiOnlineResourcePropertyType
from seabeepy.metadata.gmd.ci_online_resource_type import CiOnlineResourceType
from seabeepy.metadata.gmd.ci_presentation_form_code import CiPresentationFormCode
from seabeepy.metadata.gmd.ci_presentation_form_code_property_type import CiPresentationFormCodePropertyType
from seabeepy.metadata.gmd.ci_responsible_party import CiResponsibleParty
from seabeepy.metadata.gmd.ci_responsible_party_property_type import CiResponsiblePartyPropertyType
from seabeepy.metadata.gmd.ci_responsible_party_type import CiResponsiblePartyType
from seabeepy.metadata.gmd.ci_role_code import CiRoleCode
from seabeepy.metadata.gmd.ci_role_code_property_type import CiRoleCodePropertyType
from seabeepy.metadata.gmd.ci_series import CiSeries
from seabeepy.metadata.gmd.ci_series_property_type import CiSeriesPropertyType
from seabeepy.metadata.gmd.ci_series_type import CiSeriesType
from seabeepy.metadata.gmd.ci_telephone import CiTelephone
from seabeepy.metadata.gmd.ci_telephone_property_type import CiTelephonePropertyType
from seabeepy.metadata.gmd.ci_telephone_type import CiTelephoneType
from seabeepy.metadata.gmd.circle import Circle
from seabeepy.metadata.gmd.circle_by_center_point import CircleByCenterPoint
from seabeepy.metadata.gmd.circle_by_center_point_type import CircleByCenterPointType
from seabeepy.metadata.gmd.circle_type import CircleType
from seabeepy.metadata.gmd.clothoid import Clothoid
from seabeepy.metadata.gmd.clothoid_type import ClothoidType
from seabeepy.metadata.gmd.code_list_type import CodeListType
from seabeepy.metadata.gmd.code_list_value_type import CodeListValueType
from seabeepy.metadata.gmd.code_or_nil_reason_list_type import CodeOrNilReasonListType
from seabeepy.metadata.gmd.code_type import CodeType
from seabeepy.metadata.gmd.code_with_authority_type import CodeWithAuthorityType
from seabeepy.metadata.gmd.compass_point_enumeration import CompassPointEnumeration
from seabeepy.metadata.gmd.composite_curve_type import (
    CompositeCurve,
    CompositeCurveType,
    Curve,
    CurvePropertyType,
    CurveSegmentArrayPropertyType,
    CurveType,
    OffsetCurve,
    OffsetCurveType,
    OrientableCurve,
    OrientableCurveType,
    BaseCurve,
    CurveMember,
    Segments,
)
from seabeepy.metadata.gmd.composite_surface_type import (
    CompositeSurface,
    CompositeSurfaceType,
    OrientableSurface,
    OrientableSurfaceType,
    SurfacePropertyType,
    BaseSurface,
    SurfaceMember,
)
from seabeepy.metadata.gmd.compound_crsproperty_type import CompoundCrspropertyType
from seabeepy.metadata.gmd.compound_crsref import CompoundCrsref
from seabeepy.metadata.gmd.concatenated_operation_property_type import ConcatenatedOperationPropertyType
from seabeepy.metadata.gmd.concatenated_operation_ref import ConcatenatedOperationRef
from seabeepy.metadata.gmd.cone import Cone
from seabeepy.metadata.gmd.cone_type import ConeType
from seabeepy.metadata.gmd.container_property_type import (
    AbstractTopoPrimitiveType,
    ContainerPropertyType,
    DirectedEdgePropertyType,
    DirectedFacePropertyType,
    DirectedNodePropertyType,
    DirectedTopoSolidPropertyType,
    Edge,
    EdgeType,
    Face,
    FaceType,
    IsolatedPropertyType,
    Node,
    NodeType,
    TopoSolid,
    TopoSolidType,
    Container,
    DirectedEdge,
    DirectedFace,
    DirectedNode,
    DirectedTopoSolid,
    Isolated,
)
from seabeepy.metadata.gmd.conventional_unit import ConventionalUnit
from seabeepy.metadata.gmd.conventional_unit_type import ConventionalUnitType
from seabeepy.metadata.gmd.conversion_property_type import ConversionPropertyType
from seabeepy.metadata.gmd.conversion_ref import ConversionRef
from seabeepy.metadata.gmd.conversion_to_preferred_unit import ConversionToPreferredUnit
from seabeepy.metadata.gmd.conversion_to_preferred_unit_type import ConversionToPreferredUnitType
from seabeepy.metadata.gmd.coordinate_operation_accuracy import CoordinateOperationAccuracy
from seabeepy.metadata.gmd.coordinate_operation_ref import CoordinateOperationRef
from seabeepy.metadata.gmd.coordinate_system import CoordinateSystem
from seabeepy.metadata.gmd.coordinate_system_axis import CoordinateSystemAxis
from seabeepy.metadata.gmd.coordinate_system_axis_property_type import CoordinateSystemAxisPropertyType
from seabeepy.metadata.gmd.coordinate_system_axis_ref import CoordinateSystemAxisRef
from seabeepy.metadata.gmd.coordinate_system_axis_type import CoordinateSystemAxisType
from seabeepy.metadata.gmd.coordinate_system_property_type import CoordinateSystemPropertyType
from seabeepy.metadata.gmd.coordinate_system_ref import CoordinateSystemRef
from seabeepy.metadata.gmd.coordinates import Coordinates
from seabeepy.metadata.gmd.coordinates_type import CoordinatesType
from seabeepy.metadata.gmd.count import Count
from seabeepy.metadata.gmd.count_extent import CountExtent
from seabeepy.metadata.gmd.count_list import CountList
from seabeepy.metadata.gmd.count_property_type import CountPropertyType
from seabeepy.metadata.gmd.country import Country
from seabeepy.metadata.gmd.country_property_type import CountryPropertyType
from seabeepy.metadata.gmd.coverage_function import CoverageFunction
from seabeepy.metadata.gmd.coverage_function_type import CoverageFunctionType
from seabeepy.metadata.gmd.coverage_mapping_rule import CoverageMappingRule
from seabeepy.metadata.gmd.crs_ref import CrsRef
from seabeepy.metadata.gmd.cubic_spline import CubicSpline
from seabeepy.metadata.gmd.cubic_spline_type import CubicSplineType
from seabeepy.metadata.gmd.curve_array_property import CurveArrayProperty
from seabeepy.metadata.gmd.curve_array_property_type import CurveArrayPropertyType
from seabeepy.metadata.gmd.curve_interpolation_type import CurveInterpolationType
from seabeepy.metadata.gmd.curve_members import CurveMembers
from seabeepy.metadata.gmd.curve_property import CurveProperty
from seabeepy.metadata.gmd.cylinder import Cylinder
from seabeepy.metadata.gmd.cylinder_type import CylinderType
from seabeepy.metadata.gmd.cylindrical_cs import CylindricalCs
from seabeepy.metadata.gmd.cylindrical_csproperty_type import CylindricalCspropertyType
from seabeepy.metadata.gmd.cylindrical_csref import CylindricalCsref
from seabeepy.metadata.gmd.cylindrical_cstype import CylindricalCstype
from seabeepy.metadata.gmd.data_block import DataBlock
from seabeepy.metadata.gmd.data_block_type import DataBlockType
from seabeepy.metadata.gmd.data_source import DataSource
from seabeepy.metadata.gmd.data_source_reference import DataSourceReference
from seabeepy.metadata.gmd.date import Date
from seabeepy.metadata.gmd.date_property_type import DatePropertyType
from seabeepy.metadata.gmd.date_time import DateTime
from seabeepy.metadata.gmd.date_time_property_type import DateTimePropertyType
from seabeepy.metadata.gmd.datum_property_type import DatumPropertyType
from seabeepy.metadata.gmd.datum_ref import DatumRef
from seabeepy.metadata.gmd.decimal import DecimalType
from seabeepy.metadata.gmd.decimal_minutes import DecimalMinutes
from seabeepy.metadata.gmd.decimal_property_type import DecimalPropertyType
from seabeepy.metadata.gmd.default_code_space import DefaultCodeSpace
from seabeepy.metadata.gmd.definition import Definition
from seabeepy.metadata.gmd.definition_base_type import DefinitionBaseType
from seabeepy.metadata.gmd.definition_proxy import DefinitionProxy
from seabeepy.metadata.gmd.definition_proxy_type import DefinitionProxyType
from seabeepy.metadata.gmd.definition_ref import DefinitionRef
from seabeepy.metadata.gmd.definition_type import DefinitionType
from seabeepy.metadata.gmd.degrees import Degrees
from seabeepy.metadata.gmd.degrees_type import DegreesType
from seabeepy.metadata.gmd.degrees_type_direction import DegreesTypeDirection
from seabeepy.metadata.gmd.derivation_unit_term import DerivationUnitTerm
from seabeepy.metadata.gmd.derivation_unit_term_type import DerivationUnitTermType
from seabeepy.metadata.gmd.derived_crsproperty_type import DerivedCrspropertyType
from seabeepy.metadata.gmd.derived_crsref import DerivedCrsref
from seabeepy.metadata.gmd.derived_crstype import DerivedCrstype
from seabeepy.metadata.gmd.derived_unit import DerivedUnit
from seabeepy.metadata.gmd.derived_unit_type import DerivedUnitType
from seabeepy.metadata.gmd.description import Description
from seabeepy.metadata.gmd.description_reference import DescriptionReference
from seabeepy.metadata.gmd.dictionary_entry_type import (
    DefinitionCollection,
    Dictionary,
    DictionaryEntryType,
    DictionaryType,
    DefinitionMember,
    DictionaryEntry,
)
from seabeepy.metadata.gmd.direct_position_list_type import DirectPositionListType
from seabeepy.metadata.gmd.direct_position_type import DirectPositionType
from seabeepy.metadata.gmd.direction import Direction
from seabeepy.metadata.gmd.direction_description_type import DirectionDescriptionType
from seabeepy.metadata.gmd.direction_property_type import DirectionPropertyType
from seabeepy.metadata.gmd.direction_vector_type import DirectionVectorType
from seabeepy.metadata.gmd.distance import Distance
from seabeepy.metadata.gmd.distance_property_type import DistancePropertyType
from seabeepy.metadata.gmd.dms_angle import DmsAngle
from seabeepy.metadata.gmd.dms_angle_value import DmsAngleValue
from seabeepy.metadata.gmd.dmsangle_type import DmsangleType
from seabeepy.metadata.gmd.domain_set import DomainSet
from seabeepy.metadata.gmd.domain_set_type import DomainSetType
from seabeepy.metadata.gmd.double_or_nil_reason_tuple_list import DoubleOrNilReasonTupleList
from seabeepy.metadata.gmd.dq_absolute_external_positional_accuracy import DqAbsoluteExternalPositionalAccuracy
from seabeepy.metadata.gmd.dq_absolute_external_positional_accuracy_property_type import DqAbsoluteExternalPositionalAccuracyPropertyType
from seabeepy.metadata.gmd.dq_absolute_external_positional_accuracy_type import DqAbsoluteExternalPositionalAccuracyType
from seabeepy.metadata.gmd.dq_accuracy_of_atime_measurement import DqAccuracyOfAtimeMeasurement
from seabeepy.metadata.gmd.dq_accuracy_of_atime_measurement_property_type import DqAccuracyOfAtimeMeasurementPropertyType
from seabeepy.metadata.gmd.dq_accuracy_of_atime_measurement_type import DqAccuracyOfAtimeMeasurementType
from seabeepy.metadata.gmd.dq_completeness_commission import DqCompletenessCommission
from seabeepy.metadata.gmd.dq_completeness_commission_property_type import DqCompletenessCommissionPropertyType
from seabeepy.metadata.gmd.dq_completeness_commission_type import DqCompletenessCommissionType
from seabeepy.metadata.gmd.dq_completeness_omission import DqCompletenessOmission
from seabeepy.metadata.gmd.dq_completeness_omission_property_type import DqCompletenessOmissionPropertyType
from seabeepy.metadata.gmd.dq_completeness_omission_type import DqCompletenessOmissionType
from seabeepy.metadata.gmd.dq_completeness_property_type import DqCompletenessPropertyType
from seabeepy.metadata.gmd.dq_conceptual_consistency import DqConceptualConsistency
from seabeepy.metadata.gmd.dq_conceptual_consistency_property_type import DqConceptualConsistencyPropertyType
from seabeepy.metadata.gmd.dq_conceptual_consistency_type import DqConceptualConsistencyType
from seabeepy.metadata.gmd.dq_conformance_result import DqConformanceResult
from seabeepy.metadata.gmd.dq_conformance_result_property_type import DqConformanceResultPropertyType
from seabeepy.metadata.gmd.dq_conformance_result_type import DqConformanceResultType
from seabeepy.metadata.gmd.dq_data_quality import DqDataQuality
from seabeepy.metadata.gmd.dq_data_quality_property_type import DqDataQualityPropertyType
from seabeepy.metadata.gmd.dq_data_quality_type import DqDataQualityType
from seabeepy.metadata.gmd.dq_domain_consistency import DqDomainConsistency
from seabeepy.metadata.gmd.dq_domain_consistency_property_type import DqDomainConsistencyPropertyType
from seabeepy.metadata.gmd.dq_domain_consistency_type import DqDomainConsistencyType
from seabeepy.metadata.gmd.dq_element_property_type import DqElementPropertyType
from seabeepy.metadata.gmd.dq_evaluation_method_type_code import DqEvaluationMethodTypeCode
from seabeepy.metadata.gmd.dq_evaluation_method_type_code_property_type import DqEvaluationMethodTypeCodePropertyType
from seabeepy.metadata.gmd.dq_format_consistency import DqFormatConsistency
from seabeepy.metadata.gmd.dq_format_consistency_property_type import DqFormatConsistencyPropertyType
from seabeepy.metadata.gmd.dq_format_consistency_type import DqFormatConsistencyType
from seabeepy.metadata.gmd.dq_gridded_data_positional_accuracy import DqGriddedDataPositionalAccuracy
from seabeepy.metadata.gmd.dq_gridded_data_positional_accuracy_property_type import DqGriddedDataPositionalAccuracyPropertyType
from seabeepy.metadata.gmd.dq_gridded_data_positional_accuracy_type import DqGriddedDataPositionalAccuracyType
from seabeepy.metadata.gmd.dq_logical_consistency_property_type import DqLogicalConsistencyPropertyType
from seabeepy.metadata.gmd.dq_non_quantitative_attribute_accuracy import DqNonQuantitativeAttributeAccuracy
from seabeepy.metadata.gmd.dq_non_quantitative_attribute_accuracy_property_type import DqNonQuantitativeAttributeAccuracyPropertyType
from seabeepy.metadata.gmd.dq_non_quantitative_attribute_accuracy_type import DqNonQuantitativeAttributeAccuracyType
from seabeepy.metadata.gmd.dq_positional_accuracy_property_type import DqPositionalAccuracyPropertyType
from seabeepy.metadata.gmd.dq_quantitative_attribute_accuracy import DqQuantitativeAttributeAccuracy
from seabeepy.metadata.gmd.dq_quantitative_attribute_accuracy_property_type import DqQuantitativeAttributeAccuracyPropertyType
from seabeepy.metadata.gmd.dq_quantitative_attribute_accuracy_type import DqQuantitativeAttributeAccuracyType
from seabeepy.metadata.gmd.dq_quantitative_result import DqQuantitativeResult
from seabeepy.metadata.gmd.dq_quantitative_result_property_type import DqQuantitativeResultPropertyType
from seabeepy.metadata.gmd.dq_quantitative_result_type import DqQuantitativeResultType
from seabeepy.metadata.gmd.dq_relative_internal_positional_accuracy import DqRelativeInternalPositionalAccuracy
from seabeepy.metadata.gmd.dq_relative_internal_positional_accuracy_property_type import DqRelativeInternalPositionalAccuracyPropertyType
from seabeepy.metadata.gmd.dq_relative_internal_positional_accuracy_type import DqRelativeInternalPositionalAccuracyType
from seabeepy.metadata.gmd.dq_result_property_type import DqResultPropertyType
from seabeepy.metadata.gmd.dq_scope import DqScope
from seabeepy.metadata.gmd.dq_scope_property_type import DqScopePropertyType
from seabeepy.metadata.gmd.dq_scope_type import DqScopeType
from seabeepy.metadata.gmd.dq_temporal_accuracy_property_type import DqTemporalAccuracyPropertyType
from seabeepy.metadata.gmd.dq_temporal_consistency import DqTemporalConsistency
from seabeepy.metadata.gmd.dq_temporal_consistency_property_type import DqTemporalConsistencyPropertyType
from seabeepy.metadata.gmd.dq_temporal_consistency_type import DqTemporalConsistencyType
from seabeepy.metadata.gmd.dq_temporal_validity import DqTemporalValidity
from seabeepy.metadata.gmd.dq_temporal_validity_property_type import DqTemporalValidityPropertyType
from seabeepy.metadata.gmd.dq_temporal_validity_type import DqTemporalValidityType
from seabeepy.metadata.gmd.dq_thematic_accuracy_property_type import DqThematicAccuracyPropertyType
from seabeepy.metadata.gmd.dq_thematic_classification_correctness import DqThematicClassificationCorrectness
from seabeepy.metadata.gmd.dq_thematic_classification_correctness_property_type import DqThematicClassificationCorrectnessPropertyType
from seabeepy.metadata.gmd.dq_thematic_classification_correctness_type import DqThematicClassificationCorrectnessType
from seabeepy.metadata.gmd.dq_topological_consistency import DqTopologicalConsistency
from seabeepy.metadata.gmd.dq_topological_consistency_property_type import DqTopologicalConsistencyPropertyType
from seabeepy.metadata.gmd.dq_topological_consistency_type import DqTopologicalConsistencyType
from seabeepy.metadata.gmd.ds_association import DsAssociation
from seabeepy.metadata.gmd.ds_association_property_type import DsAssociationPropertyType
from seabeepy.metadata.gmd.ds_association_type import DsAssociationType
from seabeepy.metadata.gmd.ds_association_type_code import DsAssociationTypeCode
from seabeepy.metadata.gmd.ds_association_type_code_property_type import DsAssociationTypeCodePropertyType
from seabeepy.metadata.gmd.ds_initiative_property_type import DsInitiativePropertyType
from seabeepy.metadata.gmd.ds_initiative_type_code import DsInitiativeTypeCode
from seabeepy.metadata.gmd.ds_initiative_type_code_property_type import DsInitiativeTypeCodePropertyType
from seabeepy.metadata.gmd.ds_other_aggregate_property_type import DsOtherAggregatePropertyType
from seabeepy.metadata.gmd.ds_platform_property_type import DsPlatformPropertyType
from seabeepy.metadata.gmd.ds_production_series_property_type import DsProductionSeriesPropertyType
from seabeepy.metadata.gmd.ds_sensor_property_type import DsSensorPropertyType
from seabeepy.metadata.gmd.ds_series_property_type import DsSeriesPropertyType
from seabeepy.metadata.gmd.ds_stereo_mate_property_type import DsStereoMatePropertyType
from seabeepy.metadata.gmd.duration import Duration
from seabeepy.metadata.gmd.dynamic_feature import DynamicFeature
from seabeepy.metadata.gmd.dynamic_feature_member_type import (
    DynamicFeatureCollection,
    DynamicFeatureCollectionType,
    DynamicFeatureMemberType,
    DynamicMembers,
)
from seabeepy.metadata.gmd.dynamic_feature_type import DynamicFeatureType
from seabeepy.metadata.gmd.edge_of import EdgeOf
from seabeepy.metadata.gmd.ellipsoid_1 import Ellipsoid1
from seabeepy.metadata.gmd.ellipsoid_2 import Ellipsoid2
from seabeepy.metadata.gmd.ellipsoid_property_type import EllipsoidPropertyType
from seabeepy.metadata.gmd.ellipsoid_ref import EllipsoidRef
from seabeepy.metadata.gmd.ellipsoid_type import EllipsoidType
from seabeepy.metadata.gmd.ellipsoidal_cs_1 import EllipsoidalCs1
from seabeepy.metadata.gmd.ellipsoidal_cs_2 import EllipsoidalCs2
from seabeepy.metadata.gmd.ellipsoidal_csproperty_type import EllipsoidalCspropertyType
from seabeepy.metadata.gmd.ellipsoidal_csref import EllipsoidalCsref
from seabeepy.metadata.gmd.ellipsoidal_cstype import EllipsoidalCstype
from seabeepy.metadata.gmd.engineering_crsproperty_type import EngineeringCrspropertyType
from seabeepy.metadata.gmd.engineering_crsref import EngineeringCrsref
from seabeepy.metadata.gmd.engineering_datum_ref import EngineeringDatumRef
from seabeepy.metadata.gmd.envelope import Envelope
from seabeepy.metadata.gmd.envelope_type import EnvelopeType
from seabeepy.metadata.gmd.envelope_with_time_period import EnvelopeWithTimePeriod
from seabeepy.metadata.gmd.envelope_with_time_period_type import EnvelopeWithTimePeriodType
from seabeepy.metadata.gmd.ex_bounding_polygon import ExBoundingPolygon
from seabeepy.metadata.gmd.ex_bounding_polygon_property_type import ExBoundingPolygonPropertyType
from seabeepy.metadata.gmd.ex_bounding_polygon_type import ExBoundingPolygonType
from seabeepy.metadata.gmd.ex_extent_property_type import ExExtentPropertyType
from seabeepy.metadata.gmd.ex_geographic_bounding_box import ExGeographicBoundingBox
from seabeepy.metadata.gmd.ex_geographic_bounding_box_property_type import ExGeographicBoundingBoxPropertyType
from seabeepy.metadata.gmd.ex_geographic_bounding_box_type import ExGeographicBoundingBoxType
from seabeepy.metadata.gmd.ex_geographic_description import ExGeographicDescription
from seabeepy.metadata.gmd.ex_geographic_description_property_type import ExGeographicDescriptionPropertyType
from seabeepy.metadata.gmd.ex_geographic_description_type import ExGeographicDescriptionType
from seabeepy.metadata.gmd.ex_geographic_extent_property_type import ExGeographicExtentPropertyType
from seabeepy.metadata.gmd.ex_spatial_temporal_extent import ExSpatialTemporalExtent
from seabeepy.metadata.gmd.ex_spatial_temporal_extent_property_type import ExSpatialTemporalExtentPropertyType
from seabeepy.metadata.gmd.ex_spatial_temporal_extent_type import ExSpatialTemporalExtentType
from seabeepy.metadata.gmd.ex_temporal_extent import ExTemporalExtent
from seabeepy.metadata.gmd.ex_temporal_extent_property_type import ExTemporalExtentPropertyType
from seabeepy.metadata.gmd.ex_temporal_extent_type import ExTemporalExtentType
from seabeepy.metadata.gmd.extent_of import ExtentOf
from seabeepy.metadata.gmd.exterior import Exterior
from seabeepy.metadata.gmd.feature_property import FeatureProperty
from seabeepy.metadata.gmd.file import File
from seabeepy.metadata.gmd.file_type import FileType
from seabeepy.metadata.gmd.file_value_model_type import FileValueModelType
from seabeepy.metadata.gmd.formula import Formula
from seabeepy.metadata.gmd.formula_type import FormulaType
from seabeepy.metadata.gmd.general_conversion_ref import GeneralConversionRef
from seabeepy.metadata.gmd.general_transformation_property_type import GeneralTransformationPropertyType
from seabeepy.metadata.gmd.general_transformation_ref import GeneralTransformationRef
from seabeepy.metadata.gmd.generic_meta_data import GenericMetaData
from seabeepy.metadata.gmd.generic_meta_data_type import GenericMetaDataType
from seabeepy.metadata.gmd.generic_name_property_type import GenericNamePropertyType
from seabeepy.metadata.gmd.geocentric_crsproperty_type import GeocentricCrspropertyType
from seabeepy.metadata.gmd.geocentric_crsref import GeocentricCrsref
from seabeepy.metadata.gmd.geodesic import Geodesic
from seabeepy.metadata.gmd.geodesic_string import GeodesicString
from seabeepy.metadata.gmd.geodesic_string_type import GeodesicStringType
from seabeepy.metadata.gmd.geodesic_type import GeodesicType
from seabeepy.metadata.gmd.geodetic_datum_ref import GeodeticDatumRef
from seabeepy.metadata.gmd.geographic_crsref import GeographicCrsref
from seabeepy.metadata.gmd.geometric_complex import GeometricComplex
from seabeepy.metadata.gmd.geometric_complex_property_type import GeometricComplexPropertyType
from seabeepy.metadata.gmd.geometric_complex_type import GeometricComplexType
from seabeepy.metadata.gmd.geometric_primitive_property_type import GeometricPrimitivePropertyType
from seabeepy.metadata.gmd.geometry_array_property_type import (
    GeometryArrayPropertyType,
    GeometryPropertyType,
    MultiGeometry,
    MultiGeometryType,
    GeometryMember,
    GeometryMembers,
)
from seabeepy.metadata.gmd.gm_object_property_type import GmObjectPropertyType
from seabeepy.metadata.gmd.gm_point_property_type import GmPointPropertyType
from seabeepy.metadata.gmd.greenwich_longitude import GreenwichLongitude
from seabeepy.metadata.gmd.grid import Grid
from seabeepy.metadata.gmd.grid_coverage import GridCoverage
from seabeepy.metadata.gmd.grid_coverage_type import GridCoverageType
from seabeepy.metadata.gmd.grid_domain import GridDomain
from seabeepy.metadata.gmd.grid_domain_type import GridDomainType
from seabeepy.metadata.gmd.grid_envelope_type import GridEnvelopeType
from seabeepy.metadata.gmd.grid_function import GridFunction
from seabeepy.metadata.gmd.grid_function_type import GridFunctionType
from seabeepy.metadata.gmd.grid_length_type import GridLengthType
from seabeepy.metadata.gmd.grid_limits_type import GridLimitsType
from seabeepy.metadata.gmd.grid_type import GridType
from seabeepy.metadata.gmd.group import Group
from seabeepy.metadata.gmd.history import History
from seabeepy.metadata.gmd.history_property_type import HistoryPropertyType
from seabeepy.metadata.gmd.identified_object_type import IdentifiedObjectType
from seabeepy.metadata.gmd.identifier import Identifier
from seabeepy.metadata.gmd.image_crsproperty_type import ImageCrspropertyType
from seabeepy.metadata.gmd.image_crsref import ImageCrsref
from seabeepy.metadata.gmd.image_datum_ref import ImageDatumRef
from seabeepy.metadata.gmd.includes_parameter import IncludesParameter
from seabeepy.metadata.gmd.increment_order import IncrementOrder
from seabeepy.metadata.gmd.indirect_entry import IndirectEntry
from seabeepy.metadata.gmd.indirect_entry_type import IndirectEntryType
from seabeepy.metadata.gmd.inline_property_type import InlinePropertyType
from seabeepy.metadata.gmd.integer import Integer
from seabeepy.metadata.gmd.integer_property_type import IntegerPropertyType
from seabeepy.metadata.gmd.integer_value import IntegerValue
from seabeepy.metadata.gmd.integer_value_list import IntegerValueList
from seabeepy.metadata.gmd.interior import Interior
from seabeepy.metadata.gmd.knot_property_type import KnotPropertyType
from seabeepy.metadata.gmd.knot_type import KnotType
from seabeepy.metadata.gmd.knot_types_type import KnotTypesType
from seabeepy.metadata.gmd.language_code import LanguageCode
from seabeepy.metadata.gmd.language_code_property_type import LanguageCodePropertyType
from seabeepy.metadata.gmd.length import Length
from seabeepy.metadata.gmd.length_property_type import LengthPropertyType
from seabeepy.metadata.gmd.length_type import LengthType
from seabeepy.metadata.gmd.li_lineage import LiLineage
from seabeepy.metadata.gmd.li_lineage_property_type import LiLineagePropertyType
from seabeepy.metadata.gmd.li_lineage_type import LiLineageType
from seabeepy.metadata.gmd.li_process_step_property_type import (
    LiProcessStep,
    LiProcessStepPropertyType,
    LiProcessStepType,
    LiSource,
    LiSourcePropertyType,
    LiSourceType,
)
from seabeepy.metadata.gmd.line_string import LineString
from seabeepy.metadata.gmd.line_string_segment import LineStringSegment
from seabeepy.metadata.gmd.line_string_segment_array_property_type import LineStringSegmentArrayPropertyType
from seabeepy.metadata.gmd.line_string_segment_type import LineStringSegmentType
from seabeepy.metadata.gmd.line_string_type import LineStringType
from seabeepy.metadata.gmd.linear_cs import LinearCs
from seabeepy.metadata.gmd.linear_csproperty_type import LinearCspropertyType
from seabeepy.metadata.gmd.linear_csref import LinearCsref
from seabeepy.metadata.gmd.linear_cstype import LinearCstype
from seabeepy.metadata.gmd.linear_ring import LinearRing
from seabeepy.metadata.gmd.linear_ring_property_type import LinearRingPropertyType
from seabeepy.metadata.gmd.linear_ring_type import LinearRingType
from seabeepy.metadata.gmd.local_name import LocalName
from seabeepy.metadata.gmd.local_name_property_type import LocalNamePropertyType
from seabeepy.metadata.gmd.localised_character_string import LocalisedCharacterString
from seabeepy.metadata.gmd.localised_character_string_property_type import LocalisedCharacterStringPropertyType
from seabeepy.metadata.gmd.localised_character_string_type import LocalisedCharacterStringType
from seabeepy.metadata.gmd.location import Location
from seabeepy.metadata.gmd.location_key_word import LocationKeyWord
from seabeepy.metadata.gmd.location_name import LocationName
from seabeepy.metadata.gmd.location_property_type import LocationPropertyType
from seabeepy.metadata.gmd.location_reference import LocationReference
from seabeepy.metadata.gmd.location_string import LocationString
from seabeepy.metadata.gmd.mapping_rule import MappingRule
from seabeepy.metadata.gmd.mapping_rule_type import MappingRuleType
from seabeepy.metadata.gmd.maximum_occurs import MaximumOccurs
from seabeepy.metadata.gmd.maximum_value import MaximumValue
from seabeepy.metadata.gmd.md_aggregate_information import MdAggregateInformation
from seabeepy.metadata.gmd.md_aggregate_information_property_type import MdAggregateInformationPropertyType
from seabeepy.metadata.gmd.md_aggregate_information_type import MdAggregateInformationType
from seabeepy.metadata.gmd.md_application_schema_information import MdApplicationSchemaInformation
from seabeepy.metadata.gmd.md_application_schema_information_property_type import MdApplicationSchemaInformationPropertyType
from seabeepy.metadata.gmd.md_application_schema_information_type import MdApplicationSchemaInformationType
from seabeepy.metadata.gmd.md_band import MdBand
from seabeepy.metadata.gmd.md_band_property_type import MdBandPropertyType
from seabeepy.metadata.gmd.md_band_type import MdBandType
from seabeepy.metadata.gmd.md_browse_graphic import MdBrowseGraphic
from seabeepy.metadata.gmd.md_browse_graphic_property_type import MdBrowseGraphicPropertyType
from seabeepy.metadata.gmd.md_browse_graphic_type import MdBrowseGraphicType
from seabeepy.metadata.gmd.md_cell_geometry_code import MdCellGeometryCode
from seabeepy.metadata.gmd.md_cell_geometry_code_property_type import MdCellGeometryCodePropertyType
from seabeepy.metadata.gmd.md_character_set_code import MdCharacterSetCode
from seabeepy.metadata.gmd.md_character_set_code_property_type import MdCharacterSetCodePropertyType
from seabeepy.metadata.gmd.md_classification_code import MdClassificationCode
from seabeepy.metadata.gmd.md_classification_code_property_type import MdClassificationCodePropertyType
from seabeepy.metadata.gmd.md_constraints import MdConstraints
from seabeepy.metadata.gmd.md_constraints_property_type import MdConstraintsPropertyType
from seabeepy.metadata.gmd.md_constraints_type import MdConstraintsType
from seabeepy.metadata.gmd.md_content_information_property_type import MdContentInformationPropertyType
from seabeepy.metadata.gmd.md_coverage_content_type_code import MdCoverageContentTypeCode
from seabeepy.metadata.gmd.md_coverage_content_type_code_property_type import MdCoverageContentTypeCodePropertyType
from seabeepy.metadata.gmd.md_coverage_description import MdCoverageDescription
from seabeepy.metadata.gmd.md_coverage_description_property_type import MdCoverageDescriptionPropertyType
from seabeepy.metadata.gmd.md_coverage_description_type import MdCoverageDescriptionType
from seabeepy.metadata.gmd.md_data_identification import MdDataIdentification
from seabeepy.metadata.gmd.md_data_identification_property_type import MdDataIdentificationPropertyType
from seabeepy.metadata.gmd.md_data_identification_type import MdDataIdentificationType
from seabeepy.metadata.gmd.md_datatype_code import MdDatatypeCode
from seabeepy.metadata.gmd.md_datatype_code_property_type import MdDatatypeCodePropertyType
from seabeepy.metadata.gmd.md_digital_transfer_options import MdDigitalTransferOptions
from seabeepy.metadata.gmd.md_digital_transfer_options_property_type import MdDigitalTransferOptionsPropertyType
from seabeepy.metadata.gmd.md_digital_transfer_options_type import MdDigitalTransferOptionsType
from seabeepy.metadata.gmd.md_dimension import MdDimension
from seabeepy.metadata.gmd.md_dimension_name_type_code import MdDimensionNameTypeCode
from seabeepy.metadata.gmd.md_dimension_name_type_code_property_type import MdDimensionNameTypeCodePropertyType
from seabeepy.metadata.gmd.md_dimension_property_type import MdDimensionPropertyType
from seabeepy.metadata.gmd.md_dimension_type import MdDimensionType
from seabeepy.metadata.gmd.md_distribution import MdDistribution
from seabeepy.metadata.gmd.md_distribution_property_type import MdDistributionPropertyType
from seabeepy.metadata.gmd.md_distribution_type import MdDistributionType
from seabeepy.metadata.gmd.md_distribution_units import MdDistributionUnits
from seabeepy.metadata.gmd.md_distribution_units_property_type import MdDistributionUnitsPropertyType
from seabeepy.metadata.gmd.md_distributor_property_type import (
    MdDistributor,
    MdDistributorPropertyType,
    MdDistributorType,
    MdFormat,
    MdFormatPropertyType,
    MdFormatType,
)
from seabeepy.metadata.gmd.md_extended_element_information import MdExtendedElementInformation
from seabeepy.metadata.gmd.md_extended_element_information_property_type import MdExtendedElementInformationPropertyType
from seabeepy.metadata.gmd.md_extended_element_information_type import MdExtendedElementInformationType
from seabeepy.metadata.gmd.md_feature_catalogue_description import MdFeatureCatalogueDescription
from seabeepy.metadata.gmd.md_feature_catalogue_description_property_type import MdFeatureCatalogueDescriptionPropertyType
from seabeepy.metadata.gmd.md_feature_catalogue_description_type import MdFeatureCatalogueDescriptionType
from seabeepy.metadata.gmd.md_geometric_object_type_code import MdGeometricObjectTypeCode
from seabeepy.metadata.gmd.md_geometric_object_type_code_property_type import MdGeometricObjectTypeCodePropertyType
from seabeepy.metadata.gmd.md_geometric_objects import MdGeometricObjects
from seabeepy.metadata.gmd.md_geometric_objects_property_type import MdGeometricObjectsPropertyType
from seabeepy.metadata.gmd.md_geometric_objects_type import MdGeometricObjectsType
from seabeepy.metadata.gmd.md_georectified import MdGeorectified
from seabeepy.metadata.gmd.md_georectified_property_type import MdGeorectifiedPropertyType
from seabeepy.metadata.gmd.md_georectified_type import MdGeorectifiedType
from seabeepy.metadata.gmd.md_georeferenceable import MdGeoreferenceable
from seabeepy.metadata.gmd.md_georeferenceable_property_type import MdGeoreferenceablePropertyType
from seabeepy.metadata.gmd.md_georeferenceable_type import MdGeoreferenceableType
from seabeepy.metadata.gmd.md_grid_spatial_representation import MdGridSpatialRepresentation
from seabeepy.metadata.gmd.md_grid_spatial_representation_property_type import MdGridSpatialRepresentationPropertyType
from seabeepy.metadata.gmd.md_grid_spatial_representation_type import MdGridSpatialRepresentationType
from seabeepy.metadata.gmd.md_identification_property_type import MdIdentificationPropertyType
from seabeepy.metadata.gmd.md_image_description import MdImageDescription
from seabeepy.metadata.gmd.md_image_description_property_type import MdImageDescriptionPropertyType
from seabeepy.metadata.gmd.md_image_description_type import MdImageDescriptionType
from seabeepy.metadata.gmd.md_imaging_condition_code import MdImagingConditionCode
from seabeepy.metadata.gmd.md_imaging_condition_code_property_type import MdImagingConditionCodePropertyType
from seabeepy.metadata.gmd.md_keyword_type_code import MdKeywordTypeCode
from seabeepy.metadata.gmd.md_keyword_type_code_property_type import MdKeywordTypeCodePropertyType
from seabeepy.metadata.gmd.md_keywords import MdKeywords
from seabeepy.metadata.gmd.md_keywords_property_type import MdKeywordsPropertyType
from seabeepy.metadata.gmd.md_keywords_type import MdKeywordsType
from seabeepy.metadata.gmd.md_legal_constraints import MdLegalConstraints
from seabeepy.metadata.gmd.md_legal_constraints_property_type import MdLegalConstraintsPropertyType
from seabeepy.metadata.gmd.md_legal_constraints_type import MdLegalConstraintsType
from seabeepy.metadata.gmd.md_maintenance_frequency_code import MdMaintenanceFrequencyCode
from seabeepy.metadata.gmd.md_maintenance_frequency_code_property_type import MdMaintenanceFrequencyCodePropertyType
from seabeepy.metadata.gmd.md_maintenance_information import MdMaintenanceInformation
from seabeepy.metadata.gmd.md_maintenance_information_property_type import MdMaintenanceInformationPropertyType
from seabeepy.metadata.gmd.md_maintenance_information_type import MdMaintenanceInformationType
from seabeepy.metadata.gmd.md_medium import MdMedium
from seabeepy.metadata.gmd.md_medium_format_code import MdMediumFormatCode
from seabeepy.metadata.gmd.md_medium_format_code_property_type import MdMediumFormatCodePropertyType
from seabeepy.metadata.gmd.md_medium_name_code import MdMediumNameCode
from seabeepy.metadata.gmd.md_medium_name_code_property_type import MdMediumNameCodePropertyType
from seabeepy.metadata.gmd.md_medium_property_type import MdMediumPropertyType
from seabeepy.metadata.gmd.md_medium_type import MdMediumType
from seabeepy.metadata.gmd.md_metadata_extension_information import MdMetadataExtensionInformation
from seabeepy.metadata.gmd.md_metadata_extension_information_property_type import MdMetadataExtensionInformationPropertyType
from seabeepy.metadata.gmd.md_metadata_extension_information_type import MdMetadataExtensionInformationType
from seabeepy.metadata.gmd.md_metadata_property_type import (
    AbstractDsAggregateType,
    DsAggregatePropertyType,
    DsDataSet,
    DsDataSetPropertyType,
    DsDataSetType,
    DsInitiative,
    DsInitiativeType,
    DsOtherAggregate,
    DsOtherAggregateType,
    DsPlatform,
    DsPlatformType,
    DsProductionSeries,
    DsProductionSeriesType,
    DsSensor,
    DsSensorType,
    DsSeries,
    DsSeriesType,
    DsStereoMate,
    DsStereoMateType,
    MdMetadata,
    MdMetadataPropertyType,
    MdMetadataType,
)
from seabeepy.metadata.gmd.md_obligation_code import MdObligationCode
from seabeepy.metadata.gmd.md_obligation_code_property_type import MdObligationCodePropertyType
from seabeepy.metadata.gmd.md_obligation_code_type import MdObligationCodeType
from seabeepy.metadata.gmd.md_pixel_orientation_code import MdPixelOrientationCode
from seabeepy.metadata.gmd.md_pixel_orientation_code_property_type import MdPixelOrientationCodePropertyType
from seabeepy.metadata.gmd.md_pixel_orientation_code_type import MdPixelOrientationCodeType
from seabeepy.metadata.gmd.md_portrayal_catalogue_reference import MdPortrayalCatalogueReference
from seabeepy.metadata.gmd.md_portrayal_catalogue_reference_property_type import MdPortrayalCatalogueReferencePropertyType
from seabeepy.metadata.gmd.md_portrayal_catalogue_reference_type import MdPortrayalCatalogueReferenceType
from seabeepy.metadata.gmd.md_progress_code import MdProgressCode
from seabeepy.metadata.gmd.md_progress_code_property_type import MdProgressCodePropertyType
from seabeepy.metadata.gmd.md_range_dimension import MdRangeDimension
from seabeepy.metadata.gmd.md_range_dimension_property_type import MdRangeDimensionPropertyType
from seabeepy.metadata.gmd.md_range_dimension_type import MdRangeDimensionType
from seabeepy.metadata.gmd.md_reference_system import MdReferenceSystem
from seabeepy.metadata.gmd.md_reference_system_property_type import MdReferenceSystemPropertyType
from seabeepy.metadata.gmd.md_reference_system_type import MdReferenceSystemType
from seabeepy.metadata.gmd.md_representative_fraction import MdRepresentativeFraction
from seabeepy.metadata.gmd.md_representative_fraction_property_type import MdRepresentativeFractionPropertyType
from seabeepy.metadata.gmd.md_representative_fraction_type import MdRepresentativeFractionType
from seabeepy.metadata.gmd.md_resolution import MdResolution
from seabeepy.metadata.gmd.md_resolution_property_type import MdResolutionPropertyType
from seabeepy.metadata.gmd.md_resolution_type import MdResolutionType
from seabeepy.metadata.gmd.md_restriction_code import MdRestrictionCode
from seabeepy.metadata.gmd.md_restriction_code_property_type import MdRestrictionCodePropertyType
from seabeepy.metadata.gmd.md_scope_code import MdScopeCode
from seabeepy.metadata.gmd.md_scope_code_property_type import MdScopeCodePropertyType
from seabeepy.metadata.gmd.md_scope_description import MdScopeDescription
from seabeepy.metadata.gmd.md_scope_description_property_type import MdScopeDescriptionPropertyType
from seabeepy.metadata.gmd.md_scope_description_type import MdScopeDescriptionType
from seabeepy.metadata.gmd.md_security_constraints import MdSecurityConstraints
from seabeepy.metadata.gmd.md_security_constraints_property_type import MdSecurityConstraintsPropertyType
from seabeepy.metadata.gmd.md_security_constraints_type import MdSecurityConstraintsType
from seabeepy.metadata.gmd.md_service_identification import MdServiceIdentification
from seabeepy.metadata.gmd.md_service_identification_property_type import MdServiceIdentificationPropertyType
from seabeepy.metadata.gmd.md_service_identification_type import MdServiceIdentificationType
from seabeepy.metadata.gmd.md_spatial_representation_property_type import MdSpatialRepresentationPropertyType
from seabeepy.metadata.gmd.md_spatial_representation_type_code import MdSpatialRepresentationTypeCode
from seabeepy.metadata.gmd.md_spatial_representation_type_code_property_type import MdSpatialRepresentationTypeCodePropertyType
from seabeepy.metadata.gmd.md_standard_order_process import MdStandardOrderProcess
from seabeepy.metadata.gmd.md_standard_order_process_property_type import MdStandardOrderProcessPropertyType
from seabeepy.metadata.gmd.md_standard_order_process_type import MdStandardOrderProcessType
from seabeepy.metadata.gmd.md_topic_category_code import MdTopicCategoryCode
from seabeepy.metadata.gmd.md_topic_category_code_property_type import MdTopicCategoryCodePropertyType
from seabeepy.metadata.gmd.md_topic_category_code_type import MdTopicCategoryCodeType
from seabeepy.metadata.gmd.md_topology_level_code import MdTopologyLevelCode
from seabeepy.metadata.gmd.md_topology_level_code_property_type import MdTopologyLevelCodePropertyType
from seabeepy.metadata.gmd.md_usage import MdUsage
from seabeepy.metadata.gmd.md_usage_property_type import MdUsagePropertyType
from seabeepy.metadata.gmd.md_usage_type import MdUsageType
from seabeepy.metadata.gmd.md_vector_spatial_representation import MdVectorSpatialRepresentation
from seabeepy.metadata.gmd.md_vector_spatial_representation_property_type import MdVectorSpatialRepresentationPropertyType
from seabeepy.metadata.gmd.md_vector_spatial_representation_type import MdVectorSpatialRepresentationType
from seabeepy.metadata.gmd.measure_1 import Measure1
from seabeepy.metadata.gmd.measure_2 import Measure2
from seabeepy.metadata.gmd.measure_list_type import MeasureListType
from seabeepy.metadata.gmd.measure_or_nil_reason_list_type import MeasureOrNilReasonListType
from seabeepy.metadata.gmd.measure_property_type import MeasurePropertyType
from seabeepy.metadata.gmd.measure_type import MeasureType
from seabeepy.metadata.gmd.member_name import MemberName
from seabeepy.metadata.gmd.member_name_property_type import MemberNamePropertyType
from seabeepy.metadata.gmd.member_name_type import MemberNameType
from seabeepy.metadata.gmd.meta_data_property import MetaDataProperty
from seabeepy.metadata.gmd.meta_data_property_type import MetaDataPropertyType
from seabeepy.metadata.gmd.method import Method
from seabeepy.metadata.gmd.method_formula import MethodFormula
from seabeepy.metadata.gmd.minimum_occurs import MinimumOccurs
from seabeepy.metadata.gmd.minimum_value import MinimumValue
from seabeepy.metadata.gmd.minutes import Minutes
from seabeepy.metadata.gmd.modified_coordinate import ModifiedCoordinate
from seabeepy.metadata.gmd.moving_object_status import MovingObjectStatus
from seabeepy.metadata.gmd.moving_object_status_type import MovingObjectStatusType
from seabeepy.metadata.gmd.multi_center_line_of import MultiCenterLineOf
from seabeepy.metadata.gmd.multi_center_of import MultiCenterOf
from seabeepy.metadata.gmd.multi_coverage import MultiCoverage
from seabeepy.metadata.gmd.multi_curve import MultiCurve
from seabeepy.metadata.gmd.multi_curve_coverage import MultiCurveCoverage
from seabeepy.metadata.gmd.multi_curve_coverage_type import MultiCurveCoverageType
from seabeepy.metadata.gmd.multi_curve_domain import MultiCurveDomain
from seabeepy.metadata.gmd.multi_curve_domain_type import MultiCurveDomainType
from seabeepy.metadata.gmd.multi_curve_property import MultiCurveProperty
from seabeepy.metadata.gmd.multi_curve_property_type import MultiCurvePropertyType
from seabeepy.metadata.gmd.multi_curve_type import MultiCurveType
from seabeepy.metadata.gmd.multi_edge_of import MultiEdgeOf
from seabeepy.metadata.gmd.multi_extent_of import MultiExtentOf
from seabeepy.metadata.gmd.multi_geometry_property import MultiGeometryProperty
from seabeepy.metadata.gmd.multi_geometry_property_type import MultiGeometryPropertyType
from seabeepy.metadata.gmd.multi_location import MultiLocation
from seabeepy.metadata.gmd.multi_point import MultiPoint
from seabeepy.metadata.gmd.multi_point_coverage import MultiPointCoverage
from seabeepy.metadata.gmd.multi_point_coverage_type import MultiPointCoverageType
from seabeepy.metadata.gmd.multi_point_domain import MultiPointDomain
from seabeepy.metadata.gmd.multi_point_domain_type import MultiPointDomainType
from seabeepy.metadata.gmd.multi_point_property import MultiPointProperty
from seabeepy.metadata.gmd.multi_point_property_type import MultiPointPropertyType
from seabeepy.metadata.gmd.multi_point_type import MultiPointType
from seabeepy.metadata.gmd.multi_position import MultiPosition
from seabeepy.metadata.gmd.multi_solid import MultiSolid
from seabeepy.metadata.gmd.multi_solid_coverage import MultiSolidCoverage
from seabeepy.metadata.gmd.multi_solid_coverage_type import MultiSolidCoverageType
from seabeepy.metadata.gmd.multi_solid_domain import MultiSolidDomain
from seabeepy.metadata.gmd.multi_solid_domain_type import MultiSolidDomainType
from seabeepy.metadata.gmd.multi_solid_property import MultiSolidProperty
from seabeepy.metadata.gmd.multi_solid_property_type import MultiSolidPropertyType
from seabeepy.metadata.gmd.multi_solid_type import MultiSolidType
from seabeepy.metadata.gmd.multi_surface import MultiSurface
from seabeepy.metadata.gmd.multi_surface_coverage import MultiSurfaceCoverage
from seabeepy.metadata.gmd.multi_surface_coverage_type import MultiSurfaceCoverageType
from seabeepy.metadata.gmd.multi_surface_domain import MultiSurfaceDomain
from seabeepy.metadata.gmd.multi_surface_domain_type import MultiSurfaceDomainType
from seabeepy.metadata.gmd.multi_surface_property import MultiSurfaceProperty
from seabeepy.metadata.gmd.multi_surface_property_type import MultiSurfacePropertyType
from seabeepy.metadata.gmd.multi_surface_type import MultiSurfaceType
from seabeepy.metadata.gmd.multiplicity import Multiplicity
from seabeepy.metadata.gmd.multiplicity_property_type import MultiplicityPropertyType
from seabeepy.metadata.gmd.multiplicity_range import MultiplicityRange
from seabeepy.metadata.gmd.multiplicity_range_property_type import MultiplicityRangePropertyType
from seabeepy.metadata.gmd.multiplicity_range_type import MultiplicityRangeType
from seabeepy.metadata.gmd.multiplicity_type import MultiplicityType
from seabeepy.metadata.gmd.name import Name
from seabeepy.metadata.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue
from seabeepy.metadata.gmd.null import Null
from seabeepy.metadata.gmd.number_property_type import NumberPropertyType
from seabeepy.metadata.gmd.object_reference_property_type import ObjectReferencePropertyType
from seabeepy.metadata.gmd.oblique_cartesian_cs import ObliqueCartesianCs
from seabeepy.metadata.gmd.oblique_cartesian_csproperty_type import ObliqueCartesianCspropertyType
from seabeepy.metadata.gmd.oblique_cartesian_csref import ObliqueCartesianCsref
from seabeepy.metadata.gmd.oblique_cartesian_cstype import ObliqueCartesianCstype
from seabeepy.metadata.gmd.operation_method import OperationMethod
from seabeepy.metadata.gmd.operation_method_property_type import OperationMethodPropertyType
from seabeepy.metadata.gmd.operation_method_ref import OperationMethodRef
from seabeepy.metadata.gmd.operation_method_type import OperationMethodType
from seabeepy.metadata.gmd.operation_parameter_1 import OperationParameter1
from seabeepy.metadata.gmd.operation_parameter_2 import OperationParameter2
from seabeepy.metadata.gmd.operation_parameter_group_property_type import OperationParameterGroupPropertyType
from seabeepy.metadata.gmd.operation_parameter_group_ref import OperationParameterGroupRef
from seabeepy.metadata.gmd.operation_parameter_property_type import OperationParameterPropertyType
from seabeepy.metadata.gmd.operation_parameter_ref import OperationParameterRef
from seabeepy.metadata.gmd.operation_parameter_type import OperationParameterType
from seabeepy.metadata.gmd.operation_property_type import OperationPropertyType
from seabeepy.metadata.gmd.operation_ref import OperationRef
from seabeepy.metadata.gmd.operation_version import OperationVersion
from seabeepy.metadata.gmd.origin import Origin
from seabeepy.metadata.gmd.parameter_value_1 import ParameterValue1
from seabeepy.metadata.gmd.parameter_value_type import ParameterValueType
from seabeepy.metadata.gmd.pass_through_operation_property_type import PassThroughOperationPropertyType
from seabeepy.metadata.gmd.pass_through_operation_ref import PassThroughOperationRef
from seabeepy.metadata.gmd.pass_through_operation_type import (
    ConcatenatedOperation,
    ConcatenatedOperationType,
    CoordinateOperationPropertyType,
    PassThroughOperation,
    PassThroughOperationType,
    CoordOperation,
    UsesOperation,
    UsesSingleOperation,
)
from seabeepy.metadata.gmd.patches import Patches
from seabeepy.metadata.gmd.pixel_in_cell import PixelInCell
from seabeepy.metadata.gmd.point import Point
from seabeepy.metadata.gmd.point_array_property import PointArrayProperty
from seabeepy.metadata.gmd.point_array_property_type import PointArrayPropertyType
from seabeepy.metadata.gmd.point_member import PointMember
from seabeepy.metadata.gmd.point_members import PointMembers
from seabeepy.metadata.gmd.point_property import PointProperty
from seabeepy.metadata.gmd.point_property_type import PointPropertyType
from seabeepy.metadata.gmd.point_rep import PointRep
from seabeepy.metadata.gmd.point_type import PointType
from seabeepy.metadata.gmd.polar_cs import PolarCs
from seabeepy.metadata.gmd.polar_csproperty_type import PolarCspropertyType
from seabeepy.metadata.gmd.polar_csref import PolarCsref
from seabeepy.metadata.gmd.polar_cstype import PolarCstype
from seabeepy.metadata.gmd.polygon import Polygon
from seabeepy.metadata.gmd.polygon_patch import PolygonPatch
from seabeepy.metadata.gmd.polygon_patch_array_property_type import PolygonPatchArrayPropertyType
from seabeepy.metadata.gmd.polygon_patch_type import PolygonPatchType
from seabeepy.metadata.gmd.polygon_patches import PolygonPatches
from seabeepy.metadata.gmd.polygon_type import PolygonType
from seabeepy.metadata.gmd.polyhedral_surface import PolyhedralSurface
from seabeepy.metadata.gmd.polyhedral_surface_type import PolyhedralSurfaceType
from seabeepy.metadata.gmd.pos import Pos
from seabeepy.metadata.gmd.pos_list import PosList
from seabeepy.metadata.gmd.position import Position
from seabeepy.metadata.gmd.prime_meridian_1 import PrimeMeridian1
from seabeepy.metadata.gmd.prime_meridian_2 import PrimeMeridian2
from seabeepy.metadata.gmd.prime_meridian_property_type import PrimeMeridianPropertyType
from seabeepy.metadata.gmd.prime_meridian_ref import PrimeMeridianRef
from seabeepy.metadata.gmd.prime_meridian_type import PrimeMeridianType
from seabeepy.metadata.gmd.priority_location import PriorityLocation
from seabeepy.metadata.gmd.priority_location_property_type import PriorityLocationPropertyType
from seabeepy.metadata.gmd.projected_crsproperty_type import ProjectedCrspropertyType
from seabeepy.metadata.gmd.projected_crsref import ProjectedCrsref
from seabeepy.metadata.gmd.pt_free_text import PtFreeText
from seabeepy.metadata.gmd.pt_free_text_property_type import PtFreeTextPropertyType
from seabeepy.metadata.gmd.pt_free_text_type import PtFreeTextType
from seabeepy.metadata.gmd.pt_locale import PtLocale
from seabeepy.metadata.gmd.pt_locale_container import PtLocaleContainer
from seabeepy.metadata.gmd.pt_locale_container_property_type import PtLocaleContainerPropertyType
from seabeepy.metadata.gmd.pt_locale_container_type import PtLocaleContainerType
from seabeepy.metadata.gmd.pt_locale_property_type import PtLocalePropertyType
from seabeepy.metadata.gmd.pt_locale_type import PtLocaleType
from seabeepy.metadata.gmd.quantity import Quantity
from seabeepy.metadata.gmd.quantity_extent import QuantityExtent
from seabeepy.metadata.gmd.quantity_extent_type import QuantityExtentType
from seabeepy.metadata.gmd.quantity_list import QuantityList
from seabeepy.metadata.gmd.quantity_property_type import QuantityPropertyType
from seabeepy.metadata.gmd.quantity_type import QuantityType
from seabeepy.metadata.gmd.quantity_type_reference import QuantityTypeReference
from seabeepy.metadata.gmd.range_meaning import RangeMeaning
from seabeepy.metadata.gmd.range_parameters import RangeParameters
from seabeepy.metadata.gmd.range_parameters_type import RangeParametersType
from seabeepy.metadata.gmd.range_set import RangeSet
from seabeepy.metadata.gmd.range_set_type import RangeSetType
from seabeepy.metadata.gmd.real import Real
from seabeepy.metadata.gmd.real_property_type import RealPropertyType
from seabeepy.metadata.gmd.realization_epoch import RealizationEpoch
from seabeepy.metadata.gmd.record import Record
from seabeepy.metadata.gmd.record_property_type import RecordPropertyType
from seabeepy.metadata.gmd.record_type import RecordType
from seabeepy.metadata.gmd.record_type_property_type import RecordTypePropertyType
from seabeepy.metadata.gmd.record_type_type import RecordTypeType
from seabeepy.metadata.gmd.rectangle import Rectangle
from seabeepy.metadata.gmd.rectangle_type import RectangleType
from seabeepy.metadata.gmd.rectified_grid import RectifiedGrid
from seabeepy.metadata.gmd.rectified_grid_coverage import RectifiedGridCoverage
from seabeepy.metadata.gmd.rectified_grid_coverage_type import RectifiedGridCoverageType
from seabeepy.metadata.gmd.rectified_grid_domain import RectifiedGridDomain
from seabeepy.metadata.gmd.rectified_grid_domain_type import RectifiedGridDomainType
from seabeepy.metadata.gmd.rectified_grid_type import RectifiedGridType
from seabeepy.metadata.gmd.reference_type import ReferenceType
from seabeepy.metadata.gmd.related_time_type_relative_position import RelatedTimeTypeRelativePosition
from seabeepy.metadata.gmd.remarks import Remarks
from seabeepy.metadata.gmd.reverse_property_name import ReversePropertyName
from seabeepy.metadata.gmd.ring import Ring
from seabeepy.metadata.gmd.ring_property_type import RingPropertyType
from seabeepy.metadata.gmd.ring_type import RingType
from seabeepy.metadata.gmd.rough_conversion_to_preferred_unit import RoughConversionToPreferredUnit
from seabeepy.metadata.gmd.rs_identifier_property_type import RsIdentifierPropertyType
from seabeepy.metadata.gmd.rs_reference_system_property_type import RsReferenceSystemPropertyType
from seabeepy.metadata.gmd.scale import Scale
from seabeepy.metadata.gmd.scale_property_type import ScalePropertyType
from seabeepy.metadata.gmd.scale_type import ScaleType
from seabeepy.metadata.gmd.scope import Scope
from seabeepy.metadata.gmd.scoped_name import ScopedName
from seabeepy.metadata.gmd.scoped_name_property_type import ScopedNamePropertyType
from seabeepy.metadata.gmd.second_defining_parameter_1 import SecondDefiningParameter1
from seabeepy.metadata.gmd.second_defining_parameter_2 import SecondDefiningParameter2
from seabeepy.metadata.gmd.second_defining_parameter_is_sphere import SecondDefiningParameterIsSphere
from seabeepy.metadata.gmd.seconds import Seconds
from seabeepy.metadata.gmd.semi_major_axis import SemiMajorAxis
from seabeepy.metadata.gmd.sequence_rule_enumeration import SequenceRuleEnumeration
from seabeepy.metadata.gmd.sequence_rule_type import SequenceRuleType
from seabeepy.metadata.gmd.shell import Shell
from seabeepy.metadata.gmd.shell_property_type import ShellPropertyType
from seabeepy.metadata.gmd.shell_type import ShellType
from seabeepy.metadata.gmd.show_value import ShowValue
from seabeepy.metadata.gmd.sign_type import SignType
from seabeepy.metadata.gmd.single_crsref import SingleCrsref
from seabeepy.metadata.gmd.single_operation_property_type import SingleOperationPropertyType
from seabeepy.metadata.gmd.single_operation_ref import SingleOperationRef
from seabeepy.metadata.gmd.solid import Solid
from seabeepy.metadata.gmd.solid_array_property import SolidArrayProperty
from seabeepy.metadata.gmd.solid_array_property_type import SolidArrayPropertyType
from seabeepy.metadata.gmd.solid_members import SolidMembers
from seabeepy.metadata.gmd.solid_property import SolidProperty
from seabeepy.metadata.gmd.solid_property_type import (
    CompositeSolid,
    CompositeSolidType,
    SolidPropertyType,
    SolidMember,
)
from seabeepy.metadata.gmd.solid_type import SolidType
from seabeepy.metadata.gmd.source_dimensions import SourceDimensions
from seabeepy.metadata.gmd.speed_type import SpeedType
from seabeepy.metadata.gmd.sphere import Sphere
from seabeepy.metadata.gmd.sphere_type import SphereType
from seabeepy.metadata.gmd.spherical_cs_1 import SphericalCs1
from seabeepy.metadata.gmd.spherical_cs_2 import SphericalCs2
from seabeepy.metadata.gmd.spherical_csproperty_type import SphericalCspropertyType
from seabeepy.metadata.gmd.spherical_csref import SphericalCsref
from seabeepy.metadata.gmd.spherical_cstype import SphericalCstype
from seabeepy.metadata.gmd.status import Status
from seabeepy.metadata.gmd.status_reference import StatusReference
from seabeepy.metadata.gmd.string_or_ref_type import StringOrRefType
from seabeepy.metadata.gmd.string_value import StringValue
from seabeepy.metadata.gmd.surface import Surface
from seabeepy.metadata.gmd.surface_array_property import SurfaceArrayProperty
from seabeepy.metadata.gmd.surface_array_property_type import SurfaceArrayPropertyType
from seabeepy.metadata.gmd.surface_interpolation_type import SurfaceInterpolationType
from seabeepy.metadata.gmd.surface_members import SurfaceMembers
from seabeepy.metadata.gmd.surface_patch_array_property_type import SurfacePatchArrayPropertyType
from seabeepy.metadata.gmd.surface_property import SurfaceProperty
from seabeepy.metadata.gmd.surface_type import SurfaceType
from seabeepy.metadata.gmd.target_dimensions import TargetDimensions
from seabeepy.metadata.gmd.target_element import TargetElement
from seabeepy.metadata.gmd.temporal_crsproperty_type import TemporalCrspropertyType
from seabeepy.metadata.gmd.temporal_crsref import TemporalCrsref
from seabeepy.metadata.gmd.temporal_cs import TemporalCs
from seabeepy.metadata.gmd.temporal_csproperty_type import TemporalCspropertyType
from seabeepy.metadata.gmd.temporal_csref import TemporalCsref
from seabeepy.metadata.gmd.temporal_cstype import TemporalCstype
from seabeepy.metadata.gmd.temporal_datum_ref import TemporalDatumRef
from seabeepy.metadata.gmd.time_calendar import TimeCalendar
from seabeepy.metadata.gmd.time_calendar_era import TimeCalendarEra
from seabeepy.metadata.gmd.time_calendar_era_property_type import TimeCalendarEraPropertyType
from seabeepy.metadata.gmd.time_calendar_era_type import TimeCalendarEraType
from seabeepy.metadata.gmd.time_calendar_property_type import TimeCalendarPropertyType
from seabeepy.metadata.gmd.time_calendar_type import TimeCalendarType
from seabeepy.metadata.gmd.time_clock import TimeClock
from seabeepy.metadata.gmd.time_clock_property_type import TimeClockPropertyType
from seabeepy.metadata.gmd.time_clock_type import TimeClockType
from seabeepy.metadata.gmd.time_coordinate_system import TimeCoordinateSystem
from seabeepy.metadata.gmd.time_coordinate_system_type import TimeCoordinateSystemType
from seabeepy.metadata.gmd.time_cs_1 import TimeCs1
from seabeepy.metadata.gmd.time_cs_2 import TimeCs2
from seabeepy.metadata.gmd.time_csproperty_type import TimeCspropertyType
from seabeepy.metadata.gmd.time_cstype import TimeCstype
from seabeepy.metadata.gmd.time_edge_property_type import (
    AbstractTimeGeometricPrimitiveType,
    AbstractTimePrimitiveType,
    AbstractTimeTopologyPrimitiveType,
    RelatedTimeType,
    TimeEdge,
    TimeEdgePropertyType,
    TimeEdgeType,
    TimeInstant,
    TimeInstantPropertyType,
    TimeInstantType,
    TimeNode,
    TimeNodePropertyType,
    TimeNodeType,
    TimePeriod,
    TimePeriodPropertyType,
    TimePeriodType,
    TimePrimitivePropertyType,
)
from seabeepy.metadata.gmd.time_indeterminate_value_type import TimeIndeterminateValueType
from seabeepy.metadata.gmd.time_interval import TimeInterval
from seabeepy.metadata.gmd.time_interval_length_type import TimeIntervalLengthType
from seabeepy.metadata.gmd.time_ordinal_era_type import (
    TimeOrdinalEra,
    TimeOrdinalEraPropertyType,
    TimeOrdinalEraType,
)
from seabeepy.metadata.gmd.time_ordinal_reference_system import TimeOrdinalReferenceSystem
from seabeepy.metadata.gmd.time_ordinal_reference_system_type import TimeOrdinalReferenceSystemType
from seabeepy.metadata.gmd.time_position import TimePosition
from seabeepy.metadata.gmd.time_position_type import TimePositionType
from seabeepy.metadata.gmd.time_reference_system import TimeReferenceSystem
from seabeepy.metadata.gmd.time_reference_system_type import TimeReferenceSystemType
from seabeepy.metadata.gmd.time_topology_complex import TimeTopologyComplex
from seabeepy.metadata.gmd.time_topology_complex_property_type import TimeTopologyComplexPropertyType
from seabeepy.metadata.gmd.time_topology_complex_type import TimeTopologyComplexType
from seabeepy.metadata.gmd.time_topology_primitive_property_type import TimeTopologyPrimitivePropertyType
from seabeepy.metadata.gmd.time_type import TimeType
from seabeepy.metadata.gmd.time_unit_type_value import TimeUnitTypeValue
from seabeepy.metadata.gmd.tin import Tin
from seabeepy.metadata.gmd.tin_type import TinType
from seabeepy.metadata.gmd.tm_period_duration import TmPeriodDuration
from seabeepy.metadata.gmd.tm_period_duration_property_type import TmPeriodDurationPropertyType
from seabeepy.metadata.gmd.tm_primitive_property_type import TmPrimitivePropertyType
from seabeepy.metadata.gmd.topo_complex_member_type import (
    TopoComplex,
    TopoComplexMemberType,
    TopoComplexType,
    MaximalComplex,
    SubComplex,
    SuperComplex,
)
from seabeepy.metadata.gmd.topo_complex_property import TopoComplexProperty
from seabeepy.metadata.gmd.topo_curve import TopoCurve
from seabeepy.metadata.gmd.topo_curve_property import TopoCurveProperty
from seabeepy.metadata.gmd.topo_curve_property_type import TopoCurvePropertyType
from seabeepy.metadata.gmd.topo_curve_type import TopoCurveType
from seabeepy.metadata.gmd.topo_point import TopoPoint
from seabeepy.metadata.gmd.topo_point_property import TopoPointProperty
from seabeepy.metadata.gmd.topo_point_property_type import TopoPointPropertyType
from seabeepy.metadata.gmd.topo_point_type import TopoPointType
from seabeepy.metadata.gmd.topo_primitive_array_association_type import TopoPrimitiveArrayAssociationType
from seabeepy.metadata.gmd.topo_primitive_member import TopoPrimitiveMember
from seabeepy.metadata.gmd.topo_primitive_member_type import TopoPrimitiveMemberType
from seabeepy.metadata.gmd.topo_primitive_members import TopoPrimitiveMembers
from seabeepy.metadata.gmd.topo_surface import TopoSurface
from seabeepy.metadata.gmd.topo_surface_property import TopoSurfaceProperty
from seabeepy.metadata.gmd.topo_surface_property_type import TopoSurfacePropertyType
from seabeepy.metadata.gmd.topo_surface_type import TopoSurfaceType
from seabeepy.metadata.gmd.topo_volume import TopoVolume
from seabeepy.metadata.gmd.topo_volume_property import TopoVolumeProperty
from seabeepy.metadata.gmd.topo_volume_property_type import TopoVolumePropertyType
from seabeepy.metadata.gmd.topo_volume_type import TopoVolumeType
from seabeepy.metadata.gmd.track import Track
from seabeepy.metadata.gmd.transformation import Transformation
from seabeepy.metadata.gmd.transformation_property_type import TransformationPropertyType
from seabeepy.metadata.gmd.transformation_ref import TransformationRef
from seabeepy.metadata.gmd.transformation_type import TransformationType
from seabeepy.metadata.gmd.triangle import Triangle
from seabeepy.metadata.gmd.triangle_patch_array_property_type import TrianglePatchArrayPropertyType
from seabeepy.metadata.gmd.triangle_patches import TrianglePatches
from seabeepy.metadata.gmd.triangle_type import TriangleType
from seabeepy.metadata.gmd.triangulated_surface import TriangulatedSurface
from seabeepy.metadata.gmd.triangulated_surface_type import TriangulatedSurfaceType
from seabeepy.metadata.gmd.tuple_list import TupleList
from seabeepy.metadata.gmd.type_name import TypeName
from seabeepy.metadata.gmd.type_name_property_type import TypeNamePropertyType
from seabeepy.metadata.gmd.type_name_type import TypeNameType
from seabeepy.metadata.gmd.unit_definition import UnitDefinition
from seabeepy.metadata.gmd.unit_definition_type import UnitDefinitionType
from seabeepy.metadata.gmd.unit_of_measure import UnitOfMeasure
from seabeepy.metadata.gmd.unit_of_measure_property_type import UnitOfMeasurePropertyType
from seabeepy.metadata.gmd.unit_of_measure_type import UnitOfMeasureType
from seabeepy.metadata.gmd.unlimited_integer import UnlimitedInteger
from seabeepy.metadata.gmd.unlimited_integer_property_type import UnlimitedIntegerPropertyType
from seabeepy.metadata.gmd.unlimited_integer_type import UnlimitedIntegerType
from seabeepy.metadata.gmd.uom_angle_property_type import UomAnglePropertyType
from seabeepy.metadata.gmd.uom_area_property_type import UomAreaPropertyType
from seabeepy.metadata.gmd.uom_length_property_type import UomLengthPropertyType
from seabeepy.metadata.gmd.uom_scale_property_type import UomScalePropertyType
from seabeepy.metadata.gmd.uom_time_property_type import UomTimePropertyType
from seabeepy.metadata.gmd.uom_velocity_property_type import UomVelocityPropertyType
from seabeepy.metadata.gmd.uom_volume_property_type import UomVolumePropertyType
from seabeepy.metadata.gmd.url import Url
from seabeepy.metadata.gmd.url_property_type import UrlPropertyType
from seabeepy.metadata.gmd.user_defined_cs import UserDefinedCs
from seabeepy.metadata.gmd.user_defined_csproperty_type import UserDefinedCspropertyType
from seabeepy.metadata.gmd.user_defined_csref import UserDefinedCsref
from seabeepy.metadata.gmd.user_defined_cstype import UserDefinedCstype
from seabeepy.metadata.gmd.uses_affine_cs import UsesAffineCs
from seabeepy.metadata.gmd.uses_axis import UsesAxis
from seabeepy.metadata.gmd.uses_cartesian_cs import UsesCartesianCs
from seabeepy.metadata.gmd.uses_cs import UsesCs
from seabeepy.metadata.gmd.uses_ellipsoid import UsesEllipsoid
from seabeepy.metadata.gmd.uses_ellipsoidal_cs import UsesEllipsoidalCs
from seabeepy.metadata.gmd.uses_method import UsesMethod
from seabeepy.metadata.gmd.uses_oblique_cartesian_cs import UsesObliqueCartesianCs
from seabeepy.metadata.gmd.uses_prime_meridian import UsesPrimeMeridian
from seabeepy.metadata.gmd.uses_spherical_cs import UsesSphericalCs
from seabeepy.metadata.gmd.uses_temporal_cs import UsesTemporalCs
from seabeepy.metadata.gmd.uses_time_cs import UsesTimeCs
from seabeepy.metadata.gmd.uses_vertical_cs import UsesVerticalCs
from seabeepy.metadata.gmd.valid_time import ValidTime
from seabeepy.metadata.gmd.value import Value
from seabeepy.metadata.gmd.value_array_property_type import (
    CompositeValue,
    CompositeValueType,
    ValueArray,
    ValueArrayPropertyType,
    ValueArrayType,
    ValuePropertyType,
    ValueComponent,
    ValueComponents,
)
from seabeepy.metadata.gmd.value_file import ValueFile
from seabeepy.metadata.gmd.value_list import ValueList
from seabeepy.metadata.gmd.value_of_parameter import ValueOfParameter
from seabeepy.metadata.gmd.value_property import ValueProperty
from seabeepy.metadata.gmd.values_of_group import ValuesOfGroup
from seabeepy.metadata.gmd.vector import Vector
from seabeepy.metadata.gmd.vector_type import VectorType
from seabeepy.metadata.gmd.vertical_crsproperty_type import VerticalCrspropertyType
from seabeepy.metadata.gmd.vertical_crsref import VerticalCrsref
from seabeepy.metadata.gmd.vertical_cs_1 import VerticalCs1
from seabeepy.metadata.gmd.vertical_cs_2 import VerticalCs2
from seabeepy.metadata.gmd.vertical_csproperty_type import VerticalCspropertyType
from seabeepy.metadata.gmd.vertical_csref import VerticalCsref
from seabeepy.metadata.gmd.vertical_cstype import VerticalCstype
from seabeepy.metadata.gmd.vertical_datum_ref import VerticalDatumRef
from seabeepy.metadata.gmd.volume_type import VolumeType

__all__ = [
    "AbstractContinuousCoverageType",
    "AbstractCoordinateSystemType",
    "AbstractCoverageType",
    "AbstractCrstype",
    "AbstractCoordinateOperationType",
    "AbstractDatumType",
    "AbstractGeneralConversionType",
    "AbstractGeneralDerivedCrstype",
    "CrspropertyType",
    "CompoundCrs",
    "CompoundCrstype",
    "ConversionType",
    "Conversion1",
    "DerivedCrs",
    "DerivedCrstype1",
    "ExExtent",
    "ExExtentType",
    "ExVerticalExtent",
    "ExVerticalExtentPropertyType",
    "ExVerticalExtentType",
    "EngineeringCrs",
    "EngineeringCrstype",
    "EngineeringDatumPropertyType",
    "EngineeringDatumType",
    "EngineeringDatum1",
    "GeneralConversionPropertyType",
    "GeocentricCrs",
    "GeocentricCrstype",
    "GeodeticCrs",
    "GeodeticCrspropertyType",
    "GeodeticCrstype",
    "GeodeticDatumPropertyType",
    "GeodeticDatumType",
    "GeodeticDatum1",
    "GeographicCrs",
    "GeographicCrspropertyType",
    "GeographicCrstype",
    "ImageCrs",
    "ImageCrstype",
    "ImageDatumPropertyType",
    "ImageDatumType",
    "ImageDatum1",
    "ProjectedCrs",
    "ProjectedCrstype",
    "ScCrsPropertyType",
    "SingleCrspropertyType",
    "TemporalCrs",
    "TemporalCrstype",
    "TemporalDatumBaseType",
    "TemporalDatumPropertyType",
    "TemporalDatumType",
    "TemporalDatum1",
    "VerticalCrs",
    "VerticalCrstype",
    "VerticalDatumPropertyType",
    "VerticalDatumType",
    "VerticalDatum1",
    "BaseCrs",
    "BaseGeodeticCrs",
    "BaseGeographicCrs",
    "ComponentReferenceSystem",
    "Conversion2",
    "DefinedByConversion",
    "DomainOfValidity",
    "EngineeringDatum2",
    "GeodeticDatum2",
    "ImageDatum2",
    "IncludesSingleCrs",
    "SourceCrs",
    "TargetCrs",
    "TemporalDatum2",
    "UsesEngineeringDatum",
    "UsesGeodeticDatum",
    "UsesImageDatum",
    "UsesTemporalDatum",
    "UsesVerticalDatum",
    "VerticalDatum2",
    "AbstractCurveSegmentType",
    "AbstractCurveType",
    "AbstractDiscreteCoverageType",
    "AbstractDqCompletenessType",
    "AbstractDqElementType",
    "AbstractDqLogicalConsistencyType",
    "AbstractDqPositionalAccuracyType",
    "AbstractDqResultType",
    "AbstractDqTemporalAccuracyType",
    "AbstractDqThematicAccuracyType",
    "AbstractExGeographicExtentType",
    "AbstractFeatureMemberType",
    "AbstractFeatureType",
    "AbstractGeneralOperationParameterPropertyType",
    "OperationParameterGroup",
    "OperationParameterGroupType",
    "GeneralOperationParameter",
    "UsesParameter",
    "AbstractGeneralOperationParameterRef",
    "AbstractGeneralOperationParameterType",
    "AbstractGeneralParameterValuePropertyType",
    "ParameterValueGroup",
    "ParameterValueGroupType",
    "IncludesValue",
    "ParameterValue2",
    "UsesValue",
    "AbstractGeneralParameterValueType",
    "AbstractGeneralTransformationType",
    "AbstractGeometricAggregateType",
    "AbstractGeometricPrimitiveType",
    "AbstractGeometryType",
    "AbstractGmltype",
    "AbstractGriddedSurfaceType",
    "AbstractMdContentInformationType",
    "AbstractMdIdentificationType",
    "AbstractMdSpatialRepresentationType",
    "AbstractMemberType",
    "AbstractMetaDataType",
    "AbstractMetadataPropertyType",
    "AbstractObjectType",
    "AbstractParametricCurveSurfaceType",
    "AbstractRingPropertyType",
    "AbstractRingType",
    "AbstractRsReferenceSystemType",
    "AbstractSolidType",
    "AbstractSurfacePatchType",
    "AbstractSurfaceType",
    "AbstractTimeComplexType",
    "AbstractTimeObjectType",
    "AbstractTimeSliceType",
    "AbstractTopologyType",
    "ActuateValue",
    "AffineCs1",
    "AffineCs2",
    "AffineCspropertyType",
    "AffineCstype",
    "AffinePlacement",
    "AffinePlacementType",
    "AggregationType",
    "AnchorDefinition",
    "AnchorPoint",
    "Angle1",
    "Angle2",
    "AngleChoiceType",
    "AnglePropertyType",
    "AngleType",
    "Arc",
    "ArcByBulge",
    "ArcByBulgeType",
    "ArcByCenterPoint",
    "ArcByCenterPointType",
    "ArcString",
    "ArcStringByBulge",
    "ArcStringByBulgeType",
    "ArcStringType",
    "ArcType",
    "AreaType",
    "AssociationName",
    "Axis",
    "AxisAbbrev",
    "AxisDirection",
    "AbstractFeatureCollectionType",
    "Array",
    "ArrayAssociationType",
    "ArrayType",
    "AssociationRoleType",
    "Bag",
    "BagType",
    "DirectedObservation",
    "DirectedObservationAtDistance",
    "DirectedObservationAtDistanceType",
    "DirectedObservationType",
    "FeatureArrayPropertyType",
    "FeatureCollection",
    "FeatureCollectionType",
    "FeaturePropertyType",
    "Observation",
    "ObservationType",
    "ProcedurePropertyType",
    "ResultType",
    "TargetPropertyType",
    "FeatureMember",
    "FeatureMembers",
    "Member",
    "Members",
    "ResultOf",
    "Subject",
    "Target",
    "Using",
    "BaseUnit",
    "BaseUnitType",
    "Bezier",
    "BezierType",
    "Binary",
    "BinaryPropertyType",
    "BinaryType",
    "Boolean1",
    "Boolean2",
    "BooleanList",
    "BooleanPropertyType1",
    "BooleanPropertyType2",
    "BooleanValue",
    "BoundedBy",
    "BoundedFeatureType",
    "BoundingShapeType",
    "Bspline",
    "BsplineType",
    "CartesianCs1",
    "CartesianCs2",
    "CartesianCspropertyType",
    "CartesianCsref",
    "CartesianCstype",
    "CatalogSymbol",
    "Category",
    "CategoryExtent",
    "CategoryExtentType",
    "CategoryList",
    "CategoryPropertyType",
    "CenterLineOf",
    "CenterOf",
    "CharacterString",
    "CharacterStringPropertyType",
    "CiAddress",
    "CiAddressPropertyType",
    "CiAddressType",
    "CiCitation",
    "CiCitationPropertyType",
    "CiCitationType",
    "MdIdentifier",
    "MdIdentifierPropertyType",
    "MdIdentifierType",
    "RsIdentifier",
    "RsIdentifierType",
    "CiContact",
    "CiContactPropertyType",
    "CiContactType",
    "CiDate",
    "CiDatePropertyType",
    "CiDateType",
    "CiDateTypeCode",
    "CiDateTypeCodePropertyType",
    "CiOnLineFunctionCode",
    "CiOnLineFunctionCodePropertyType",
    "CiOnlineResource",
    "CiOnlineResourcePropertyType",
    "CiOnlineResourceType",
    "CiPresentationFormCode",
    "CiPresentationFormCodePropertyType",
    "CiResponsibleParty",
    "CiResponsiblePartyPropertyType",
    "CiResponsiblePartyType",
    "CiRoleCode",
    "CiRoleCodePropertyType",
    "CiSeries",
    "CiSeriesPropertyType",
    "CiSeriesType",
    "CiTelephone",
    "CiTelephonePropertyType",
    "CiTelephoneType",
    "Circle",
    "CircleByCenterPoint",
    "CircleByCenterPointType",
    "CircleType",
    "Clothoid",
    "ClothoidType",
    "CodeListType",
    "CodeListValueType",
    "CodeOrNilReasonListType",
    "CodeType",
    "CodeWithAuthorityType",
    "CompassPointEnumeration",
    "CompositeCurve",
    "CompositeCurveType",
    "Curve",
    "CurvePropertyType",
    "CurveSegmentArrayPropertyType",
    "CurveType",
    "OffsetCurve",
    "OffsetCurveType",
    "OrientableCurve",
    "OrientableCurveType",
    "BaseCurve",
    "CurveMember",
    "Segments",
    "CompositeSurface",
    "CompositeSurfaceType",
    "OrientableSurface",
    "OrientableSurfaceType",
    "SurfacePropertyType",
    "BaseSurface",
    "SurfaceMember",
    "CompoundCrspropertyType",
    "CompoundCrsref",
    "ConcatenatedOperationPropertyType",
    "ConcatenatedOperationRef",
    "Cone",
    "ConeType",
    "AbstractTopoPrimitiveType",
    "ContainerPropertyType",
    "DirectedEdgePropertyType",
    "DirectedFacePropertyType",
    "DirectedNodePropertyType",
    "DirectedTopoSolidPropertyType",
    "Edge",
    "EdgeType",
    "Face",
    "FaceType",
    "IsolatedPropertyType",
    "Node",
    "NodeType",
    "TopoSolid",
    "TopoSolidType",
    "Container",
    "DirectedEdge",
    "DirectedFace",
    "DirectedNode",
    "DirectedTopoSolid",
    "Isolated",
    "ConventionalUnit",
    "ConventionalUnitType",
    "ConversionPropertyType",
    "ConversionRef",
    "ConversionToPreferredUnit",
    "ConversionToPreferredUnitType",
    "CoordinateOperationAccuracy",
    "CoordinateOperationRef",
    "CoordinateSystem",
    "CoordinateSystemAxis",
    "CoordinateSystemAxisPropertyType",
    "CoordinateSystemAxisRef",
    "CoordinateSystemAxisType",
    "CoordinateSystemPropertyType",
    "CoordinateSystemRef",
    "Coordinates",
    "CoordinatesType",
    "Count",
    "CountExtent",
    "CountList",
    "CountPropertyType",
    "Country",
    "CountryPropertyType",
    "CoverageFunction",
    "CoverageFunctionType",
    "CoverageMappingRule",
    "CrsRef",
    "CubicSpline",
    "CubicSplineType",
    "CurveArrayProperty",
    "CurveArrayPropertyType",
    "CurveInterpolationType",
    "CurveMembers",
    "CurveProperty",
    "Cylinder",
    "CylinderType",
    "CylindricalCs",
    "CylindricalCspropertyType",
    "CylindricalCsref",
    "CylindricalCstype",
    "DataBlock",
    "DataBlockType",
    "DataSource",
    "DataSourceReference",
    "Date",
    "DatePropertyType",
    "DateTime",
    "DateTimePropertyType",
    "DatumPropertyType",
    "DatumRef",
    "DecimalType",
    "DecimalMinutes",
    "DecimalPropertyType",
    "DefaultCodeSpace",
    "Definition",
    "DefinitionBaseType",
    "DefinitionProxy",
    "DefinitionProxyType",
    "DefinitionRef",
    "DefinitionType",
    "Degrees",
    "DegreesType",
    "DegreesTypeDirection",
    "DerivationUnitTerm",
    "DerivationUnitTermType",
    "DerivedCrspropertyType",
    "DerivedCrsref",
    "DerivedCrstype",
    "DerivedUnit",
    "DerivedUnitType",
    "Description",
    "DescriptionReference",
    "DefinitionCollection",
    "Dictionary",
    "DictionaryEntryType",
    "DictionaryType",
    "DefinitionMember",
    "DictionaryEntry",
    "DirectPositionListType",
    "DirectPositionType",
    "Direction",
    "DirectionDescriptionType",
    "DirectionPropertyType",
    "DirectionVectorType",
    "Distance",
    "DistancePropertyType",
    "DmsAngle",
    "DmsAngleValue",
    "DmsangleType",
    "DomainSet",
    "DomainSetType",
    "DoubleOrNilReasonTupleList",
    "DqAbsoluteExternalPositionalAccuracy",
    "DqAbsoluteExternalPositionalAccuracyPropertyType",
    "DqAbsoluteExternalPositionalAccuracyType",
    "DqAccuracyOfAtimeMeasurement",
    "DqAccuracyOfAtimeMeasurementPropertyType",
    "DqAccuracyOfAtimeMeasurementType",
    "DqCompletenessCommission",
    "DqCompletenessCommissionPropertyType",
    "DqCompletenessCommissionType",
    "DqCompletenessOmission",
    "DqCompletenessOmissionPropertyType",
    "DqCompletenessOmissionType",
    "DqCompletenessPropertyType",
    "DqConceptualConsistency",
    "DqConceptualConsistencyPropertyType",
    "DqConceptualConsistencyType",
    "DqConformanceResult",
    "DqConformanceResultPropertyType",
    "DqConformanceResultType",
    "DqDataQuality",
    "DqDataQualityPropertyType",
    "DqDataQualityType",
    "DqDomainConsistency",
    "DqDomainConsistencyPropertyType",
    "DqDomainConsistencyType",
    "DqElementPropertyType",
    "DqEvaluationMethodTypeCode",
    "DqEvaluationMethodTypeCodePropertyType",
    "DqFormatConsistency",
    "DqFormatConsistencyPropertyType",
    "DqFormatConsistencyType",
    "DqGriddedDataPositionalAccuracy",
    "DqGriddedDataPositionalAccuracyPropertyType",
    "DqGriddedDataPositionalAccuracyType",
    "DqLogicalConsistencyPropertyType",
    "DqNonQuantitativeAttributeAccuracy",
    "DqNonQuantitativeAttributeAccuracyPropertyType",
    "DqNonQuantitativeAttributeAccuracyType",
    "DqPositionalAccuracyPropertyType",
    "DqQuantitativeAttributeAccuracy",
    "DqQuantitativeAttributeAccuracyPropertyType",
    "DqQuantitativeAttributeAccuracyType",
    "DqQuantitativeResult",
    "DqQuantitativeResultPropertyType",
    "DqQuantitativeResultType",
    "DqRelativeInternalPositionalAccuracy",
    "DqRelativeInternalPositionalAccuracyPropertyType",
    "DqRelativeInternalPositionalAccuracyType",
    "DqResultPropertyType",
    "DqScope",
    "DqScopePropertyType",
    "DqScopeType",
    "DqTemporalAccuracyPropertyType",
    "DqTemporalConsistency",
    "DqTemporalConsistencyPropertyType",
    "DqTemporalConsistencyType",
    "DqTemporalValidity",
    "DqTemporalValidityPropertyType",
    "DqTemporalValidityType",
    "DqThematicAccuracyPropertyType",
    "DqThematicClassificationCorrectness",
    "DqThematicClassificationCorrectnessPropertyType",
    "DqThematicClassificationCorrectnessType",
    "DqTopologicalConsistency",
    "DqTopologicalConsistencyPropertyType",
    "DqTopologicalConsistencyType",
    "DsAssociation",
    "DsAssociationPropertyType",
    "DsAssociationType",
    "DsAssociationTypeCode",
    "DsAssociationTypeCodePropertyType",
    "DsInitiativePropertyType",
    "DsInitiativeTypeCode",
    "DsInitiativeTypeCodePropertyType",
    "DsOtherAggregatePropertyType",
    "DsPlatformPropertyType",
    "DsProductionSeriesPropertyType",
    "DsSensorPropertyType",
    "DsSeriesPropertyType",
    "DsStereoMatePropertyType",
    "Duration",
    "DynamicFeature",
    "DynamicFeatureCollection",
    "DynamicFeatureCollectionType",
    "DynamicFeatureMemberType",
    "DynamicMembers",
    "DynamicFeatureType",
    "EdgeOf",
    "Ellipsoid1",
    "Ellipsoid2",
    "EllipsoidPropertyType",
    "EllipsoidRef",
    "EllipsoidType",
    "EllipsoidalCs1",
    "EllipsoidalCs2",
    "EllipsoidalCspropertyType",
    "EllipsoidalCsref",
    "EllipsoidalCstype",
    "EngineeringCrspropertyType",
    "EngineeringCrsref",
    "EngineeringDatumRef",
    "Envelope",
    "EnvelopeType",
    "EnvelopeWithTimePeriod",
    "EnvelopeWithTimePeriodType",
    "ExBoundingPolygon",
    "ExBoundingPolygonPropertyType",
    "ExBoundingPolygonType",
    "ExExtentPropertyType",
    "ExGeographicBoundingBox",
    "ExGeographicBoundingBoxPropertyType",
    "ExGeographicBoundingBoxType",
    "ExGeographicDescription",
    "ExGeographicDescriptionPropertyType",
    "ExGeographicDescriptionType",
    "ExGeographicExtentPropertyType",
    "ExSpatialTemporalExtent",
    "ExSpatialTemporalExtentPropertyType",
    "ExSpatialTemporalExtentType",
    "ExTemporalExtent",
    "ExTemporalExtentPropertyType",
    "ExTemporalExtentType",
    "ExtentOf",
    "Exterior",
    "FeatureProperty",
    "File",
    "FileType",
    "FileValueModelType",
    "Formula",
    "FormulaType",
    "GeneralConversionRef",
    "GeneralTransformationPropertyType",
    "GeneralTransformationRef",
    "GenericMetaData",
    "GenericMetaDataType",
    "GenericNamePropertyType",
    "GeocentricCrspropertyType",
    "GeocentricCrsref",
    "Geodesic",
    "GeodesicString",
    "GeodesicStringType",
    "GeodesicType",
    "GeodeticDatumRef",
    "GeographicCrsref",
    "GeometricComplex",
    "GeometricComplexPropertyType",
    "GeometricComplexType",
    "GeometricPrimitivePropertyType",
    "GeometryArrayPropertyType",
    "GeometryPropertyType",
    "MultiGeometry",
    "MultiGeometryType",
    "GeometryMember",
    "GeometryMembers",
    "GmObjectPropertyType",
    "GmPointPropertyType",
    "GreenwichLongitude",
    "Grid",
    "GridCoverage",
    "GridCoverageType",
    "GridDomain",
    "GridDomainType",
    "GridEnvelopeType",
    "GridFunction",
    "GridFunctionType",
    "GridLengthType",
    "GridLimitsType",
    "GridType",
    "Group",
    "History",
    "HistoryPropertyType",
    "IdentifiedObjectType",
    "Identifier",
    "ImageCrspropertyType",
    "ImageCrsref",
    "ImageDatumRef",
    "IncludesParameter",
    "IncrementOrder",
    "IndirectEntry",
    "IndirectEntryType",
    "InlinePropertyType",
    "Integer",
    "IntegerPropertyType",
    "IntegerValue",
    "IntegerValueList",
    "Interior",
    "KnotPropertyType",
    "KnotType",
    "KnotTypesType",
    "LanguageCode",
    "LanguageCodePropertyType",
    "Length",
    "LengthPropertyType",
    "LengthType",
    "LiLineage",
    "LiLineagePropertyType",
    "LiLineageType",
    "LiProcessStep",
    "LiProcessStepPropertyType",
    "LiProcessStepType",
    "LiSource",
    "LiSourcePropertyType",
    "LiSourceType",
    "LineString",
    "LineStringSegment",
    "LineStringSegmentArrayPropertyType",
    "LineStringSegmentType",
    "LineStringType",
    "LinearCs",
    "LinearCspropertyType",
    "LinearCsref",
    "LinearCstype",
    "LinearRing",
    "LinearRingPropertyType",
    "LinearRingType",
    "LocalName",
    "LocalNamePropertyType",
    "LocalisedCharacterString",
    "LocalisedCharacterStringPropertyType",
    "LocalisedCharacterStringType",
    "Location",
    "LocationKeyWord",
    "LocationName",
    "LocationPropertyType",
    "LocationReference",
    "LocationString",
    "MappingRule",
    "MappingRuleType",
    "MaximumOccurs",
    "MaximumValue",
    "MdAggregateInformation",
    "MdAggregateInformationPropertyType",
    "MdAggregateInformationType",
    "MdApplicationSchemaInformation",
    "MdApplicationSchemaInformationPropertyType",
    "MdApplicationSchemaInformationType",
    "MdBand",
    "MdBandPropertyType",
    "MdBandType",
    "MdBrowseGraphic",
    "MdBrowseGraphicPropertyType",
    "MdBrowseGraphicType",
    "MdCellGeometryCode",
    "MdCellGeometryCodePropertyType",
    "MdCharacterSetCode",
    "MdCharacterSetCodePropertyType",
    "MdClassificationCode",
    "MdClassificationCodePropertyType",
    "MdConstraints",
    "MdConstraintsPropertyType",
    "MdConstraintsType",
    "MdContentInformationPropertyType",
    "MdCoverageContentTypeCode",
    "MdCoverageContentTypeCodePropertyType",
    "MdCoverageDescription",
    "MdCoverageDescriptionPropertyType",
    "MdCoverageDescriptionType",
    "MdDataIdentification",
    "MdDataIdentificationPropertyType",
    "MdDataIdentificationType",
    "MdDatatypeCode",
    "MdDatatypeCodePropertyType",
    "MdDigitalTransferOptions",
    "MdDigitalTransferOptionsPropertyType",
    "MdDigitalTransferOptionsType",
    "MdDimension",
    "MdDimensionNameTypeCode",
    "MdDimensionNameTypeCodePropertyType",
    "MdDimensionPropertyType",
    "MdDimensionType",
    "MdDistribution",
    "MdDistributionPropertyType",
    "MdDistributionType",
    "MdDistributionUnits",
    "MdDistributionUnitsPropertyType",
    "MdDistributor",
    "MdDistributorPropertyType",
    "MdDistributorType",
    "MdFormat",
    "MdFormatPropertyType",
    "MdFormatType",
    "MdExtendedElementInformation",
    "MdExtendedElementInformationPropertyType",
    "MdExtendedElementInformationType",
    "MdFeatureCatalogueDescription",
    "MdFeatureCatalogueDescriptionPropertyType",
    "MdFeatureCatalogueDescriptionType",
    "MdGeometricObjectTypeCode",
    "MdGeometricObjectTypeCodePropertyType",
    "MdGeometricObjects",
    "MdGeometricObjectsPropertyType",
    "MdGeometricObjectsType",
    "MdGeorectified",
    "MdGeorectifiedPropertyType",
    "MdGeorectifiedType",
    "MdGeoreferenceable",
    "MdGeoreferenceablePropertyType",
    "MdGeoreferenceableType",
    "MdGridSpatialRepresentation",
    "MdGridSpatialRepresentationPropertyType",
    "MdGridSpatialRepresentationType",
    "MdIdentificationPropertyType",
    "MdImageDescription",
    "MdImageDescriptionPropertyType",
    "MdImageDescriptionType",
    "MdImagingConditionCode",
    "MdImagingConditionCodePropertyType",
    "MdKeywordTypeCode",
    "MdKeywordTypeCodePropertyType",
    "MdKeywords",
    "MdKeywordsPropertyType",
    "MdKeywordsType",
    "MdLegalConstraints",
    "MdLegalConstraintsPropertyType",
    "MdLegalConstraintsType",
    "MdMaintenanceFrequencyCode",
    "MdMaintenanceFrequencyCodePropertyType",
    "MdMaintenanceInformation",
    "MdMaintenanceInformationPropertyType",
    "MdMaintenanceInformationType",
    "MdMedium",
    "MdMediumFormatCode",
    "MdMediumFormatCodePropertyType",
    "MdMediumNameCode",
    "MdMediumNameCodePropertyType",
    "MdMediumPropertyType",
    "MdMediumType",
    "MdMetadataExtensionInformation",
    "MdMetadataExtensionInformationPropertyType",
    "MdMetadataExtensionInformationType",
    "AbstractDsAggregateType",
    "DsAggregatePropertyType",
    "DsDataSet",
    "DsDataSetPropertyType",
    "DsDataSetType",
    "DsInitiative",
    "DsInitiativeType",
    "DsOtherAggregate",
    "DsOtherAggregateType",
    "DsPlatform",
    "DsPlatformType",
    "DsProductionSeries",
    "DsProductionSeriesType",
    "DsSensor",
    "DsSensorType",
    "DsSeries",
    "DsSeriesType",
    "DsStereoMate",
    "DsStereoMateType",
    "MdMetadata",
    "MdMetadataPropertyType",
    "MdMetadataType",
    "MdObligationCode",
    "MdObligationCodePropertyType",
    "MdObligationCodeType",
    "MdPixelOrientationCode",
    "MdPixelOrientationCodePropertyType",
    "MdPixelOrientationCodeType",
    "MdPortrayalCatalogueReference",
    "MdPortrayalCatalogueReferencePropertyType",
    "MdPortrayalCatalogueReferenceType",
    "MdProgressCode",
    "MdProgressCodePropertyType",
    "MdRangeDimension",
    "MdRangeDimensionPropertyType",
    "MdRangeDimensionType",
    "MdReferenceSystem",
    "MdReferenceSystemPropertyType",
    "MdReferenceSystemType",
    "MdRepresentativeFraction",
    "MdRepresentativeFractionPropertyType",
    "MdRepresentativeFractionType",
    "MdResolution",
    "MdResolutionPropertyType",
    "MdResolutionType",
    "MdRestrictionCode",
    "MdRestrictionCodePropertyType",
    "MdScopeCode",
    "MdScopeCodePropertyType",
    "MdScopeDescription",
    "MdScopeDescriptionPropertyType",
    "MdScopeDescriptionType",
    "MdSecurityConstraints",
    "MdSecurityConstraintsPropertyType",
    "MdSecurityConstraintsType",
    "MdServiceIdentification",
    "MdServiceIdentificationPropertyType",
    "MdServiceIdentificationType",
    "MdSpatialRepresentationPropertyType",
    "MdSpatialRepresentationTypeCode",
    "MdSpatialRepresentationTypeCodePropertyType",
    "MdStandardOrderProcess",
    "MdStandardOrderProcessPropertyType",
    "MdStandardOrderProcessType",
    "MdTopicCategoryCode",
    "MdTopicCategoryCodePropertyType",
    "MdTopicCategoryCodeType",
    "MdTopologyLevelCode",
    "MdTopologyLevelCodePropertyType",
    "MdUsage",
    "MdUsagePropertyType",
    "MdUsageType",
    "MdVectorSpatialRepresentation",
    "MdVectorSpatialRepresentationPropertyType",
    "MdVectorSpatialRepresentationType",
    "Measure1",
    "Measure2",
    "MeasureListType",
    "MeasureOrNilReasonListType",
    "MeasurePropertyType",
    "MeasureType",
    "MemberName",
    "MemberNamePropertyType",
    "MemberNameType",
    "MetaDataProperty",
    "MetaDataPropertyType",
    "Method",
    "MethodFormula",
    "MinimumOccurs",
    "MinimumValue",
    "Minutes",
    "ModifiedCoordinate",
    "MovingObjectStatus",
    "MovingObjectStatusType",
    "MultiCenterLineOf",
    "MultiCenterOf",
    "MultiCoverage",
    "MultiCurve",
    "MultiCurveCoverage",
    "MultiCurveCoverageType",
    "MultiCurveDomain",
    "MultiCurveDomainType",
    "MultiCurveProperty",
    "MultiCurvePropertyType",
    "MultiCurveType",
    "MultiEdgeOf",
    "MultiExtentOf",
    "MultiGeometryProperty",
    "MultiGeometryPropertyType",
    "MultiLocation",
    "MultiPoint",
    "MultiPointCoverage",
    "MultiPointCoverageType",
    "MultiPointDomain",
    "MultiPointDomainType",
    "MultiPointProperty",
    "MultiPointPropertyType",
    "MultiPointType",
    "MultiPosition",
    "MultiSolid",
    "MultiSolidCoverage",
    "MultiSolidCoverageType",
    "MultiSolidDomain",
    "MultiSolidDomainType",
    "MultiSolidProperty",
    "MultiSolidPropertyType",
    "MultiSolidType",
    "MultiSurface",
    "MultiSurfaceCoverage",
    "MultiSurfaceCoverageType",
    "MultiSurfaceDomain",
    "MultiSurfaceDomainType",
    "MultiSurfaceProperty",
    "MultiSurfacePropertyType",
    "MultiSurfaceType",
    "Multiplicity",
    "MultiplicityPropertyType",
    "MultiplicityRange",
    "MultiplicityRangePropertyType",
    "MultiplicityRangeType",
    "MultiplicityType",
    "Name",
    "NilReasonEnumerationValue",
    "Null",
    "NumberPropertyType",
    "ObjectReferencePropertyType",
    "ObliqueCartesianCs",
    "ObliqueCartesianCspropertyType",
    "ObliqueCartesianCsref",
    "ObliqueCartesianCstype",
    "OperationMethod",
    "OperationMethodPropertyType",
    "OperationMethodRef",
    "OperationMethodType",
    "OperationParameter1",
    "OperationParameter2",
    "OperationParameterGroupPropertyType",
    "OperationParameterGroupRef",
    "OperationParameterPropertyType",
    "OperationParameterRef",
    "OperationParameterType",
    "OperationPropertyType",
    "OperationRef",
    "OperationVersion",
    "Origin",
    "ParameterValue1",
    "ParameterValueType",
    "PassThroughOperationPropertyType",
    "PassThroughOperationRef",
    "ConcatenatedOperation",
    "ConcatenatedOperationType",
    "CoordinateOperationPropertyType",
    "PassThroughOperation",
    "PassThroughOperationType",
    "CoordOperation",
    "UsesOperation",
    "UsesSingleOperation",
    "Patches",
    "PixelInCell",
    "Point",
    "PointArrayProperty",
    "PointArrayPropertyType",
    "PointMember",
    "PointMembers",
    "PointProperty",
    "PointPropertyType",
    "PointRep",
    "PointType",
    "PolarCs",
    "PolarCspropertyType",
    "PolarCsref",
    "PolarCstype",
    "Polygon",
    "PolygonPatch",
    "PolygonPatchArrayPropertyType",
    "PolygonPatchType",
    "PolygonPatches",
    "PolygonType",
    "PolyhedralSurface",
    "PolyhedralSurfaceType",
    "Pos",
    "PosList",
    "Position",
    "PrimeMeridian1",
    "PrimeMeridian2",
    "PrimeMeridianPropertyType",
    "PrimeMeridianRef",
    "PrimeMeridianType",
    "PriorityLocation",
    "PriorityLocationPropertyType",
    "ProjectedCrspropertyType",
    "ProjectedCrsref",
    "PtFreeText",
    "PtFreeTextPropertyType",
    "PtFreeTextType",
    "PtLocale",
    "PtLocaleContainer",
    "PtLocaleContainerPropertyType",
    "PtLocaleContainerType",
    "PtLocalePropertyType",
    "PtLocaleType",
    "Quantity",
    "QuantityExtent",
    "QuantityExtentType",
    "QuantityList",
    "QuantityPropertyType",
    "QuantityType",
    "QuantityTypeReference",
    "RangeMeaning",
    "RangeParameters",
    "RangeParametersType",
    "RangeSet",
    "RangeSetType",
    "Real",
    "RealPropertyType",
    "RealizationEpoch",
    "Record",
    "RecordPropertyType",
    "RecordType",
    "RecordTypePropertyType",
    "RecordTypeType",
    "Rectangle",
    "RectangleType",
    "RectifiedGrid",
    "RectifiedGridCoverage",
    "RectifiedGridCoverageType",
    "RectifiedGridDomain",
    "RectifiedGridDomainType",
    "RectifiedGridType",
    "ReferenceType",
    "RelatedTimeTypeRelativePosition",
    "Remarks",
    "ReversePropertyName",
    "Ring",
    "RingPropertyType",
    "RingType",
    "RoughConversionToPreferredUnit",
    "RsIdentifierPropertyType",
    "RsReferenceSystemPropertyType",
    "Scale",
    "ScalePropertyType",
    "ScaleType",
    "Scope",
    "ScopedName",
    "ScopedNamePropertyType",
    "SecondDefiningParameter1",
    "SecondDefiningParameter2",
    "SecondDefiningParameterIsSphere",
    "Seconds",
    "SemiMajorAxis",
    "SequenceRuleEnumeration",
    "SequenceRuleType",
    "Shell",
    "ShellPropertyType",
    "ShellType",
    "ShowValue",
    "SignType",
    "SingleCrsref",
    "SingleOperationPropertyType",
    "SingleOperationRef",
    "Solid",
    "SolidArrayProperty",
    "SolidArrayPropertyType",
    "SolidMembers",
    "SolidProperty",
    "CompositeSolid",
    "CompositeSolidType",
    "SolidPropertyType",
    "SolidMember",
    "SolidType",
    "SourceDimensions",
    "SpeedType",
    "Sphere",
    "SphereType",
    "SphericalCs1",
    "SphericalCs2",
    "SphericalCspropertyType",
    "SphericalCsref",
    "SphericalCstype",
    "Status",
    "StatusReference",
    "StringOrRefType",
    "StringValue",
    "Surface",
    "SurfaceArrayProperty",
    "SurfaceArrayPropertyType",
    "SurfaceInterpolationType",
    "SurfaceMembers",
    "SurfacePatchArrayPropertyType",
    "SurfaceProperty",
    "SurfaceType",
    "TargetDimensions",
    "TargetElement",
    "TemporalCrspropertyType",
    "TemporalCrsref",
    "TemporalCs",
    "TemporalCspropertyType",
    "TemporalCsref",
    "TemporalCstype",
    "TemporalDatumRef",
    "TimeCalendar",
    "TimeCalendarEra",
    "TimeCalendarEraPropertyType",
    "TimeCalendarEraType",
    "TimeCalendarPropertyType",
    "TimeCalendarType",
    "TimeClock",
    "TimeClockPropertyType",
    "TimeClockType",
    "TimeCoordinateSystem",
    "TimeCoordinateSystemType",
    "TimeCs1",
    "TimeCs2",
    "TimeCspropertyType",
    "TimeCstype",
    "AbstractTimeGeometricPrimitiveType",
    "AbstractTimePrimitiveType",
    "AbstractTimeTopologyPrimitiveType",
    "RelatedTimeType",
    "TimeEdge",
    "TimeEdgePropertyType",
    "TimeEdgeType",
    "TimeInstant",
    "TimeInstantPropertyType",
    "TimeInstantType",
    "TimeNode",
    "TimeNodePropertyType",
    "TimeNodeType",
    "TimePeriod",
    "TimePeriodPropertyType",
    "TimePeriodType",
    "TimePrimitivePropertyType",
    "TimeIndeterminateValueType",
    "TimeInterval",
    "TimeIntervalLengthType",
    "TimeOrdinalEra",
    "TimeOrdinalEraPropertyType",
    "TimeOrdinalEraType",
    "TimeOrdinalReferenceSystem",
    "TimeOrdinalReferenceSystemType",
    "TimePosition",
    "TimePositionType",
    "TimeReferenceSystem",
    "TimeReferenceSystemType",
    "TimeTopologyComplex",
    "TimeTopologyComplexPropertyType",
    "TimeTopologyComplexType",
    "TimeTopologyPrimitivePropertyType",
    "TimeType",
    "TimeUnitTypeValue",
    "Tin",
    "TinType",
    "TmPeriodDuration",
    "TmPeriodDurationPropertyType",
    "TmPrimitivePropertyType",
    "TopoComplex",
    "TopoComplexMemberType",
    "TopoComplexType",
    "MaximalComplex",
    "SubComplex",
    "SuperComplex",
    "TopoComplexProperty",
    "TopoCurve",
    "TopoCurveProperty",
    "TopoCurvePropertyType",
    "TopoCurveType",
    "TopoPoint",
    "TopoPointProperty",
    "TopoPointPropertyType",
    "TopoPointType",
    "TopoPrimitiveArrayAssociationType",
    "TopoPrimitiveMember",
    "TopoPrimitiveMemberType",
    "TopoPrimitiveMembers",
    "TopoSurface",
    "TopoSurfaceProperty",
    "TopoSurfacePropertyType",
    "TopoSurfaceType",
    "TopoVolume",
    "TopoVolumeProperty",
    "TopoVolumePropertyType",
    "TopoVolumeType",
    "Track",
    "Transformation",
    "TransformationPropertyType",
    "TransformationRef",
    "TransformationType",
    "Triangle",
    "TrianglePatchArrayPropertyType",
    "TrianglePatches",
    "TriangleType",
    "TriangulatedSurface",
    "TriangulatedSurfaceType",
    "TupleList",
    "TypeName",
    "TypeNamePropertyType",
    "TypeNameType",
    "UnitDefinition",
    "UnitDefinitionType",
    "UnitOfMeasure",
    "UnitOfMeasurePropertyType",
    "UnitOfMeasureType",
    "UnlimitedInteger",
    "UnlimitedIntegerPropertyType",
    "UnlimitedIntegerType",
    "UomAnglePropertyType",
    "UomAreaPropertyType",
    "UomLengthPropertyType",
    "UomScalePropertyType",
    "UomTimePropertyType",
    "UomVelocityPropertyType",
    "UomVolumePropertyType",
    "Url",
    "UrlPropertyType",
    "UserDefinedCs",
    "UserDefinedCspropertyType",
    "UserDefinedCsref",
    "UserDefinedCstype",
    "UsesAffineCs",
    "UsesAxis",
    "UsesCartesianCs",
    "UsesCs",
    "UsesEllipsoid",
    "UsesEllipsoidalCs",
    "UsesMethod",
    "UsesObliqueCartesianCs",
    "UsesPrimeMeridian",
    "UsesSphericalCs",
    "UsesTemporalCs",
    "UsesTimeCs",
    "UsesVerticalCs",
    "ValidTime",
    "Value",
    "CompositeValue",
    "CompositeValueType",
    "ValueArray",
    "ValueArrayPropertyType",
    "ValueArrayType",
    "ValuePropertyType",
    "ValueComponent",
    "ValueComponents",
    "ValueFile",
    "ValueList",
    "ValueOfParameter",
    "ValueProperty",
    "ValuesOfGroup",
    "Vector",
    "VectorType",
    "VerticalCrspropertyType",
    "VerticalCrsref",
    "VerticalCs1",
    "VerticalCs2",
    "VerticalCspropertyType",
    "VerticalCsref",
    "VerticalCstype",
    "VerticalDatumRef",
    "VolumeType",
]
