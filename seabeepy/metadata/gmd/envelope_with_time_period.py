from dataclasses import dataclass
from seabeepy.metadata.gmd.envelope_with_time_period_type import EnvelopeWithTimePeriodType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EnvelopeWithTimePeriod(EnvelopeWithTimePeriodType):
    """gml:EnvelopeWithTimePeriod is provided for envelopes that include a
    temporal extent.

    It adds two time position properties, gml:beginPosition and
    gml:endPosition, which describe the extent of a time-envelope. Since
    gml:EnvelopeWithTimePeriod is assigned to the substitution group
    headed by gml:Envelope, it may be used whenever gml:Envelope is
    valid.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
