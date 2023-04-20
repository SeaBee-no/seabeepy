from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class StringValue:
    """gml:stringValue is a character string value of an operation parameter.

    A string value does not have an associated unit of measure.
    """
    class Meta:
        name = "stringValue"
        namespace = "http://www.opengis.net/gml"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
