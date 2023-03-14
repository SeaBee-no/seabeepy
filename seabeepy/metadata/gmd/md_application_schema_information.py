from dataclasses import dataclass
from seabeepy.metadata.gmd.md_application_schema_information_type import MdApplicationSchemaInformationType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdApplicationSchemaInformation(MdApplicationSchemaInformationType):
    class Meta:
        name = "MD_ApplicationSchemaInformation"
        namespace = "http://www.isotc211.org/2005/gmd"
