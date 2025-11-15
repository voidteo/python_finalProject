import pathlib

accounts: dict = {"count": 0, "records": []}
transactions: dict = {"count": 0, "records": []}
DATA_DIR = pathlib.Path.cwd() / "data"
DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


SESSION_EXPIRE_MINUTES = 60