from datetime import datetime, timezone


def myprint(msg: str, level: str = None):
    defaultmsg = "[{}] {} {}"
    currtime = datetime.now(timezone.utc)

    default_level = "INFO"
    print(defaultmsg.format(default_level if not level else level, msg, currtime))