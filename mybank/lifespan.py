import json
import pathlib

from mybank.settings import DATA_DIR


def load_accounts() -> tuple:
    with open(DATA_DIR / "accounts.json", mode="r") as f:
        accounts = json.load(f)

    print("accounts.json faylidan muvaffaqiyatli o'qildi.")
    # print(accounts)

    return accounts["count"], accounts["records"]


def save_accounts(accounts_data: dict):
    with open(DATA_DIR / "accounts_tmp.json", "w") as f:
        json.dump(accounts_data, f, indent=4)

    pathlib.Path.unlink(DATA_DIR / "accounts.json")
    pathlib.Path.rename(DATA_DIR / "accounts_tmp.json", DATA_DIR / "accounts.json")

    print("Akkauntlar saqlandi!")
    return True


def load_transactions() -> dict:
    with open(DATA_DIR / "transactions.json", mode="r") as f:
        transactions = json.load(f)

    print("transactions.json faylidan muvaffaqiyatli o'qildi.")
    # print(transactions)

    return transactions["count"], transactions["records"]


def save_transactions(transactions_data: dict):
    with open(DATA_DIR / "transactions_tmp.json", "w") as f:
        json.dump(transactions_data, f, indent=4)

    pathlib.Path.unlink(DATA_DIR / "transactions.json")
    pathlib.Path.rename(
        DATA_DIR / "transactions_tmp.json", DATA_DIR / "transactions.json"
    )

    print("Tranzaksiyalar saqlandi!")
    return True