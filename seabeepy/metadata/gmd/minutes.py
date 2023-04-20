from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Minutes:
    class Meta:
        name = "minutes"
        namespace = "http://www.opengis.net/gml"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
            "max_inclusive": 59,
        }
    )
