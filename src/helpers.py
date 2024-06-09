import json
from datetime import datetime as dt


def get_operations(file_name: str) -> list:
    with open(f"data/{file_name}", "r") as data:
        operations = json.loads(data.read())
    return operations


def get_only_executed(sorted_operations: list) -> list:
    executed_operations = [
        tr for tr in sorted_operations if tr.get("state") == "EXECUTED"
    ]
    return executed_operations


def sort_operations_by_date(all_operations: list) -> list:
    sorted_operations = sorted(
        all_operations,
        key=lambda x: (
            dt.strptime(x.get("date", ""), "%Y-%m-%dT%H:%M:%S.%f")
            if x.get("date")
            else dt.min
        ),
        reverse=True,
    )

    return sorted_operations


def mask_account(account_number: str) -> str:
    """
    Masks an account number, revealing only the last 4 digits.

    Args:
        account_number (str): The account number to be masked.

    Returns:
        str: The masked account number.
    """
    masked_account = "**" + account_number[-4:]
    return masked_account


def mask_card(card_number: str) -> str:
    """
    Masks a card number, revealing only the first 6 and last 4 digits.

    Args:
        card_number (str): The card number to be masked.

    Returns:
        str: The masked card number, formatted in groups of 4 digits separated by spaces.
    """
    masked_number = card_number[:6] + "*" * 6 + card_number[-4:]
    masked_number = " ".join(
        [masked_number[i : i + 4] for i in range(0, len(masked_number), 4)]
    )
    return masked_number


def get_transaction_info(transaction_params: str) -> str:
    """
    Retrieves and masks sensitive information from a transaction.

    Args:
        transaction_params (str): A string containing transaction parameters.

    Returns:
        str: A string containing the masked account number or card number.
    """
    number = transaction_params.split(" ")[-1]
    system = transaction_params.split(" ")[:-1]

    if len(number) != 16:
        return " ".join(system) + " " + mask_account(number)
    else:
        return " ".join(system) + " " + mask_card(number)
    
def format_operation_to_output(operation: dict) -> str:
    first_line = (
        dt.strptime(operation["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime(
            "%d.%m.%Y"
        )
        + " "
        + operation["description"]
        + "\n"
    )

    if operation.get("from"):
        second_line = (
            get_transaction_info(operation.get("from"))
            + " -> "
            + get_transaction_info(operation.get("to"))
            + "\n"
        )
    else:
        second_line = get_transaction_info(operation.get("to")) + "\n"

    third_line = (
        operation["operationAmount"]["amount"]
        + " "
        + operation["operationAmount"]["currency"]["name"]
    )

    return first_line + second_line + third_line
