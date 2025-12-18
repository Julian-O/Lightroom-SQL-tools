import os
import pytz
from tzlocal import get_localzone


# unix timestamp for LR date reference (2001,1,1,0,0,0)
TIMESTAMP_LRBASE = 978307200


# work around on cygwin problem :
#
env_tz = os.getenv(
    "TZ"
)  # exists on cygwin and cause exception on tzlocal.get_localzone()
localzone = pytz.timezone(env_tz) if env_tz else get_localzone()
utczone = pytz.utc
