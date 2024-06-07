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
