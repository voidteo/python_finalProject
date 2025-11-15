from mybank.session import load_session, check_session_is_valid
from mybank.auth import login, register_account, get_account_profile, logout, delete_account
from mybank.utils import do_you_want_continue, print_commands
from mybank.services import deposit, withdraw, view_transactions


login_command = [
    "0. Log In",
]

register_command = [
    "1. Register New Account",
]

protected_commands = [
    "2. Get Profile",
    "3. Deposit",
    "4. Withdraw",
    "5. My Transactions",
    "6. Log Out",
    "7. Delete Account",
]

admin_commands = [
    "8. View All Accounts",
    "9. Search Account",
    "10. View All Transactions",
]

exit_command = ["-1. Exit"]


def print_menu(account_id: str, expires_at: str) -> None:
    if not account_id:
        print_commands(commands=login_command + register_command + exit_command)
    elif (
        account_id
        and expires_at
        and check_session_is_valid(account_id=account_id, session_expires_at=expires_at)
    ):
        print_commands(commands=protected_commands + exit_command)


def main_menu() -> None:
    while True:
        account_id, expires_at = load_session()
        print_menu(account_id, expires_at)

        choice: int = int(input("Enter your choice: "))

        if choice == 0:
            # LOGIN
            login()
            do_you_want_continue()
            continue
        elif choice == 1:
            # REGISTER
            register_account()
            do_you_want_continue()
        elif choice == 2:
            # PROFILE
            get_account_profile(account_id=account_id)
            do_you_want_continue()
        elif choice == 3:
            # DEPOSIT
            deposit(account_id=account_id, amount=int(input("Enter amount: ")))
            do_you_want_continue()
        elif choice == 4:
            # WITHDRAW
            withdraw(account_id=account_id, amount=int(input("Enter amount: ")))
            do_you_want_continue()
        elif choice == 5:
            # MY TRANSACTIONS
            view_transactions(account_id=account_id)
            do_you_want_continue()
        elif choice == 6:
            # LOGOUT
            logout()
            do_you_want_continue()
        elif choice == 7:
            # DELETE ACCOUNT
            is_confirmed = input(
                "Rostdan akkauntingizni o'chirmoqchimisiz? (Ha (1)/Yoq (0)): "
            )
            if is_confirmed != "1":
                continue
            delete_account(account_id=account_id)
            pass
        else:
            print("Exit")
            break