from datetime import datetime, timezone, timedelta

from mybank.middlewares import log_action
from mybank.lifespan import load_accounts, load_transactions, save_accounts, save_transactions
from mybank.settings import accounts, transactions
from mybank.models import Transaction


def deposit(account_id: str, amount: int):
    accounts["count"], accounts["records"] = load_accounts()
    transactions["count"], transactions["records"] = load_transactions()
    is_found = False
    
    for account in accounts["records"]:
        if account["is_active"] and account["id"] == account_id:
            is_found = True
            account["balance"] += amount
            
    new_transaction = Transaction(
        account_id=account_id,
        type="deposit",
        amount=amount,
        status="completed",
        created_at=datetime.now(timezone.utc),
    )
    transactions["records"].append(new_transaction.to_dict())
    transactions["count"] += 1
    
    save_accounts(accounts)
    save_transactions(transactions)

    return is_found


def withdraw(account_id: str, amount: int):
    accounts["count"], accounts["records"] = load_accounts()
    is_found = False
    
    for account in accounts["records"]:
        if account["is_active"] and account["id"] == account_id:
            is_found = True
            account["balance"] -= amount
    
    new_transaction = Transaction(
        account_id=account_id,
        type="deposit",
        amount=amount,
        status="completed",
        created_at=datetime.now(timezone.utc),
    )
    transactions["records"].append(new_transaction.to_dict())
    transactions["count"] += 1
    
    save_accounts(accounts)
    save_transactions(transactions)

    return is_found


def view_transactions(account_id: str):
    transactions["count"], transactions["records"] = load_transactions()

    for transaction in transactions["records"]:
        if transaction["account_id"] == account_id:
            print(transaction)


@log_action
def view_all_accounts():
    # print("Barcha akkauntlar ro'yxati:")
    # for i, account in enumerate(accounts["records"]):
    #     print(f"{i + 1}. {account["name"]} - {account["balance"]}")

    # is_end: str = input("Operatsiyani yakunlashni istaysizmi? ")
    # if is_end == "\n":
    #     return None
    pass


@log_action
def search_account():
    # searched_name = input("Qidirilayotgan account egasini kiriting: ")

    # print("===== Natijalar =====")
    # for i, account in enumerate(accounts["records"]):
    #     if account["is_active"] == True and searched_name.lower() in account["name"].lower():
    #         print(
    #             f"{i + 1}. {account["id"]} - {account["name"]} - {account["account_number"]}"
    #         )

    # is_end: str = input("Operatsiyani yakunlashni istaysizmi? ")
    # if is_end == "\n":
    #     return None
    pass