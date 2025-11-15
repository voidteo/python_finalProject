import uuid
from datetime import datetime

from mybank.settings import DATETIME_FORMAT


class BankAccount:
    def __init__(
        self,
        username: str,
        password: str,
        name: str,
        account_number: str,
        balance: int,
        created_at: datetime,
        id: uuid.UUID = None,
    ) -> None:
        self.id = uuid.uuid4() if not id else id
        self.username = username
        self.password = password
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.is_active = True
        self.created_at = created_at

    def to_dict(self):
        return {
            "id": str(self.id),
            "username": self.username,
            "password": self.password,
            "name": self.name,
            "account_number": self.account_number,
            "balance": self.balance,
            "is_active": self.is_active,
            "created_at": self.created_at.strftime(DATETIME_FORMAT),
        }

    def __str__(self):
        return f"BankAccount<name={self.name}>"


class Transaction:
    def __init__(
        self,
        account_id: uuid.UUID,
        type: str,
        amount: int,
        status: str,
        created_at: datetime,
    ) -> None:
        self.id = uuid.uuid4()
        self.type = type
        self.account_id = account_id
        self.amount = amount
        self.status = status
        self.created_at = created_at

    def to_dict(self):
        return {
            "id": str(self.id),
            "account_id": str(self.account_id),
            "type": self.type,
            "amount": self.amount,
            "status": self.status,
            "created_at": self.created_at.strftime(DATETIME_FORMAT),
        }

    def __str__(self) -> str:
        return f"Transaction<sender={self.sender_name}, amount={self.amount}>"