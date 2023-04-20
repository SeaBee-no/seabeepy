from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from seabeepy.metadata.gmd.degrees import Degrees

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DmsangleType:
    class Meta:
        name = "DMSAngleType"

    degrees: Optional[Degrees] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        }
    )
    decimal_minutes: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "decimalMinutes",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_inclusive": Decimal("0.00"),
            "max_exclusive": Decimal("60.00"),
        }
    )
    minutes: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "max_inclusive": 59,
        }
    )
    seconds: Optional[Decimal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_inclusive": Decimal("0.00"),
            "max_exclusive": Decimal("60.00"),
        }
    )
