from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.boolean_property_type_2 import BooleanPropertyType2
from seabeepy.metadata.gmd.ci_citation_type import MdIdentifierPropertyType
from seabeepy.metadata.gmd.integer_property_type import IntegerPropertyType
from seabeepy.metadata.gmd.md_coverage_description_type import MdCoverageDescriptionType
from seabeepy.metadata.gmd.md_imaging_condition_code_property_type import MdImagingConditionCodePropertyType
from seabeepy.metadata.gmd.real_property_type import RealPropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdImageDescriptionType(MdCoverageDescriptionType):
    """
    Information about an image's suitability for use.
    """
    class Meta:
        name = "MD_ImageDescription_Type"

    illumination_elevation_angle: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "illuminationElevationAngle",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    illumination_azimuth_angle: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "illuminationAzimuthAngle",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    imaging_condition: Optional[MdImagingConditionCodePropertyType] = field(
        default=None,
        metadata={
            "name": "imagingCondition",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    image_quality_code: Optional[MdIdentifierPropertyType] = field(
        default=None,
        metadata={
            "name": "imageQualityCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    cloud_cover_percentage: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "cloudCoverPercentage",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    processing_level_code: Optional[MdIdentifierPropertyType] = field(
        default=None,
        metadata={
            "name": "processingLevelCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    compression_generation_quantity: Optional[IntegerPropertyType] = field(
        default=None,
        metadata={
            "name": "compressionGenerationQuantity",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    triangulation_indicator: Optional[BooleanPropertyType2] = field(
        default=None,
        metadata={
            "name": "triangulationIndicator",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    radiometric_calibration_data_availability: Optional[BooleanPropertyType2] = field(
        default=None,
        metadata={
            "name": "radiometricCalibrationDataAvailability",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    camera_calibration_information_availability: Optional[BooleanPropertyType2] = field(
        default=None,
        metadata={
            "name": "cameraCalibrationInformationAvailability",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    film_distortion_information_availability: Optional[BooleanPropertyType2] = field(
        default=None,
        metadata={
            "name": "filmDistortionInformationAvailability",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    lens_distortion_information_availability: Optional[BooleanPropertyType2] = field(
        default=None,
        metadata={
            "name": "lensDistortionInformationAvailability",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
