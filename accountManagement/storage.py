from account import Account

FILE_NAME = "accounts.txt"

def load_accounts():
    accounts = []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                acc = Account.from_string(line)
                if acc:
                    accounts.append(acc)
    except FileNotFoundError:
        pass
    return accounts

def save_all_accounts(accounts):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for acc in accounts:
            f.write(acc.to_string())
import os
from account import Account

FILE_NAME = os.path.join(os.path.dirname(__file__), "accounts.txt")


def load_accounts():
    accounts = []

    if not os.path.exists(FILE_NAME):
        return accounts

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            username, password, role = line.split(",")
            accounts.append(Account(username, password, role))

    return accounts


def save_accounts(accounts):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for acc in accounts:
            f.write(f"{acc.username},{acc.password},{acc.role}\n")
