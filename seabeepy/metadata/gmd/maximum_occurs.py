from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MaximumOccurs:
    """gml:maximumOccurs is the maximum number of times that values for this
    parameter group may be included.

    If this attribute is omitted, the maximum number shall be one.
    """
    class Meta:
        name = "maximumOccurs"
        namespace = "http://www.opengis.net/gml"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
