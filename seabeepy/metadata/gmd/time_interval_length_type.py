from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union
from seabeepy.metadata.gmd.time_unit_type_value import TimeUnitTypeValue

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeIntervalLengthType:
    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        }
    )
    unit: Optional[Union[str, TimeUnitTypeValue]] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"other:\w{2,}",
        }
    )
    radix: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    factor: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
