from dataclasses import dataclass, field
from typing import List, Optional
from seabeepy.metadata.gmd.boolean_property_type_2 import BooleanPropertyType2
from seabeepy.metadata.gmd.character_string_property_type import CharacterStringPropertyType
from seabeepy.metadata.gmd.gm_point_property_type import GmPointPropertyType
from seabeepy.metadata.gmd.md_grid_spatial_representation_type import MdGridSpatialRepresentationType
from seabeepy.metadata.gmd.md_pixel_orientation_code_property_type import MdPixelOrientationCodePropertyType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdGeorectifiedType(MdGridSpatialRepresentationType):
    class Meta:
        name = "MD_Georectified_Type"

    check_point_availability: Optional[BooleanPropertyType2] = field(
        default=None,
        metadata={
            "name": "checkPointAvailability",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    check_point_description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "checkPointDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    corner_points: List[GmPointPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "cornerPoints",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    center_point: Optional[GmPointPropertyType] = field(
        default=None,
        metadata={
            "name": "centerPoint",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    point_in_pixel: Optional[MdPixelOrientationCodePropertyType] = field(
        default=None,
        metadata={
            "name": "pointInPixel",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        }
    )
    transformation_dimension_description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "name": "transformationDimensionDescription",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        }
    )
    transformation_dimension_mapping: List[CharacterStringPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "transformationDimensionMapping",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "max_occurs": 2,
        }
    )
