from .bot import BotBase
import logging
from collections import namedtuple

__version__ = "1.0.2"


logging.getLogger(__name__).addHandler(logging.NullHandler())
VersionInfo = namedtuple("VersionInfo", "major minor micro releaselevel serial")
version_info = VersionInfo(
    major=1, minor=0, micro=2, releaselevel="production", serial=0
)
