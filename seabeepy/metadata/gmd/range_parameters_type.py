from dataclasses import dataclass, field
from typing import List, Optional, Union
from seabeepy.metadata.gmd.actuate_value import ActuateValue
from seabeepy.metadata.gmd.boolean_1 import Boolean1
from seabeepy.metadata.gmd.category import Category
from seabeepy.metadata.gmd.category_extent import CategoryExtent
from seabeepy.metadata.gmd.category_list import CategoryList
from seabeepy.metadata.gmd.count import Count
from seabeepy.metadata.gmd.nil_reason_enumeration_value import NilReasonEnumerationValue
from seabeepy.metadata.gmd.quantity import Quantity
from seabeepy.metadata.gmd.quantity_extent import QuantityExtent
from seabeepy.metadata.gmd.quantity_list import QuantityList
from seabeepy.metadata.gmd.show_value import ShowValue
from seabeepy.metadata.gmd.value_array_property_type import (
    CompositeValue,
    ValueArray,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RangeParametersType:
    """gml:RangeParameterType is a framework for the description of the range
    parameters each of which is a gml:AbstractValue.

    Specific range parameters are defined through the creation of a GML
    Application Schema that provides elements that are substitutable for
    gml:AbstractValue.
    """
    quantity_extent: Optional[QuantityExtent] = field(
        default=None,
        metadata={
            "name": "QuantityExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    count_extent: List[Union[str, NilReasonEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "name": "CountExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "length": 2,
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
    category_extent: Optional[CategoryExtent] = field(
        default=None,
        metadata={
            "name": "CategoryExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    value_array: Optional[ValueArray] = field(
        default=None,
        metadata={
            "name": "ValueArray",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    composite_value: Optional[CompositeValue] = field(
        default=None,
        metadata={
            "name": "CompositeValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    quantity_list: Optional[QuantityList] = field(
        default=None,
        metadata={
            "name": "QuantityList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    count_list: List[Union[str, NilReasonEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "name": "CountList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
    category_list: Optional[CategoryList] = field(
        default=None,
        metadata={
            "name": "CategoryList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        }
    )
    boolean_list: List[Union[str, NilReasonEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "name": "BooleanList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        }
    )
    count: Optional[Count] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        }
    )
    category: Optional[Category] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        }
    )
    boolean: Optional[Boolean1] = field(
        default=None,
        metadata={
            "name": "Boolean",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        }
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    type: str = field(
        init=False,
        default="simple",
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        }
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        }
    )
