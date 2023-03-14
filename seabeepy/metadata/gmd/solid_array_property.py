from dataclasses import dataclass
from seabeepy.metadata.gmd.solid_array_property_type import SolidArrayPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SolidArrayProperty(SolidArrayPropertyType):
    """This property element contains a list of solid elements.

    solidArrayProperty is the predefined property which may be used by
    GML Application Schemas whenever a GML feature has a property with a
    value that is substitutable for a list of AbstractSolid.
    """
    class Meta:
        name = "solidArrayProperty"
        namespace = "http://www.opengis.net/gml"
