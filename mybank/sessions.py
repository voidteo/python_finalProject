import json
from datetime import datetime, timezone, timedelta

from mybank.settings import SESSION_EXPIRE_MINUTES, DATETIME_FORMAT, DATA_DIR, accounts
from mybank.lifespan import load_accounts


def load_session():
    empty_session = {"account_id": None, "expires_at": None}

    with open(DATA_DIR / "session.json", "r") as f:
        session_data = json.load(f)

    # if session_data["expires_at"] and datetime.now() < datetime.strptime(session_data["expires_at"], DATETIME_FORMAT):
    #     return session_data["account_id"], session_data["expires_at"]
    if session_data["account_id"]:
        return session_data["account_id"], session_data["expires_at"]

    return empty_session["account_id"], empty_session["expires_at"]


def save_session(account_id: str):
    expires_at = datetime.now(timezone.utc) + timedelta(minutes=SESSION_EXPIRE_MINUTES)
    session_data = {
        "account_id": account_id,
        "expires_at": expires_at.strftime(DATETIME_FORMAT),
    }

    with open(DATA_DIR / "session.json", "w") as f:
        json.dump(session_data, f, indent=4)

    return True


def check_session_is_valid(account_id: str, session_expires_at: str):
    accounts["count"], accounts["records"] = load_accounts()

    for account in accounts["records"]:
        if account["id"] == account_id:
            return True

    # if datetime.now(timezone.utc) > datetime.strptime(session_expires_at, DATETIME_FORMAT):
    #     return False

    return False