from dataclasses import dataclass
from seabeepy.metadata.gmd.pt_locale_type import PtLocaleType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class PtLocale(PtLocaleType):
    class Meta:
        name = "PT_Locale"
        namespace = "http://www.isotc211.org/2005/gmd"
