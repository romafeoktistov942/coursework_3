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
    