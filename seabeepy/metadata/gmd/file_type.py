from dataclasses import dataclass, field
from typing import Optional
from seabeepy.metadata.gmd.file_value_model_type import FileValueModelType
from seabeepy.metadata.gmd.range_parameters import RangeParameters

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class FileType:
    range_parameters: Optional[RangeParameters] = field(
        default=None,
        metadata={
            "name": "rangeParameters",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    file_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    file_structure: Optional[FileValueModelType] = field(
        default=None,
        metadata={
            "name": "fileStructure",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    compression: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
