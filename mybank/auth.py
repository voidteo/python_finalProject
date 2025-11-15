import json
from datetime import datetime, timezone

from mybank.middlewares import log_action
from mybank.models import BankAccount
from mybank.settings import accounts, DATA_DIR
from mybank.lifespan import load_accounts, save_accounts
from mybank.session import save_session


@log_action
def login():
    accounts["count"], accounts["records"] = load_accounts()

    username: str = input("Username: ")
    password: str = input("Password: ")

    is_found, found_account_id = False, None
    for account in accounts["records"]:
        if (
            username == account["username"]
            and password == account["password"]
            and account["is_active"]
        ):
            is_found = True
            found_account_id = account["id"]
            break

    if not is_found:
        print("Bunday account mavjud emas.")
        return False

    save_session(account_id=found_account_id)

    print("Login successful!")

    return True


@log_action
def register_account():
    accounts["count"], accounts["records"] = load_accounts()

    print("Siz yangi akkaunt ochmoqchisiz. Quyidagi ma'lumotlarni kiriting:")

    username: str = input("Username: ")

    for account in accounts["records"]:
        if username == account["username"]:
            print("Bunday username allaqachon bor!")
            return False

    password: str = input("Password: ")
    if len(password) < 8 or not password.isalnum():
        print(
            "Parolingiz 8 ta harfdan kam bo'lmasligi va faqat alphanumeric bo'lishi shart."
        )
        return False
    confirm_password: str = input("Confirm Password: ")
    if password != confirm_password:
        print("Password mismatch.")
        return False

    name: str = input("F.I.Sh: ")
    account_number: str = input("Akkaunt raqamingiz: ")
    balance: int = int(input("Mavjud balansingiz: "))
    created_at: datetime = datetime.now(timezone.utc)

    new_account: BankAccount = BankAccount(
        username=username,
        password=password,
        name=name,
        account_number=account_number,
        balance=balance,
        created_at=created_at,
    )

    accounts["records"].append(new_account.to_dict())
    accounts["count"] += 1

    save_accounts(accounts_data=accounts)
    print("New account successfully registered!")

    return True


@log_action
def get_account_profile(account_id: str):
    accounts["count"], accounts["records"] = load_accounts()

    for account in accounts["records"]:
        if account["is_active"] and account["id"] == account_id:
            print(account)
            break


def logout():
    with open(DATA_DIR / "session.json", "w") as f:
        json.dump({"account_id": None, "expires_at": None}, f, indent=4)


def delete_account(account_id: str):
    accounts["count"], accounts["records"] = load_accounts()

    for account in accounts["records"]:
        if account["is_active"] and account["id"] == account_id:
            account["is_active"] = False
            break

    print("Account successfully deleted!")