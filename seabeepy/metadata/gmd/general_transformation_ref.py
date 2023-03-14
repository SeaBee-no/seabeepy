from dataclasses import dataclass
from seabeepy.metadata.gmd.general_transformation_property_type import GeneralTransformationPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeneralTransformationRef(GeneralTransformationPropertyType):
    class Meta:
        name = "generalTransformationRef"
        namespace = "http://www.opengis.net/gml"
