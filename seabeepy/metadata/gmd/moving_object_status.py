from dataclasses import dataclass
from seabeepy.metadata.gmd.moving_object_status_type import MovingObjectStatusType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MovingObjectStatus(MovingObjectStatusType):
    """gml:MovingObjectStatus is one example of how gml:AbstractTimeSlice may
    be extended.

    This element provides a standard method to capture a record of the
    status of a moving object. A gml:MovingObjectStatus element allows
    the user to describe the present location, along with the speed,
    bearing, acceleration and elevation of an object in a particular
    time slice. Additional information about the current status of the
    object may be recorded in the gml:status or gml:statusReference
    property elements.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
