
from src.helpers import mask_account, mask_card, get_transaction_info

def test_mask_account():
    assert mask_account("72731966109147704472") == "**4472"

def test_mask_card():
    assert mask_card("5999414228426353") == "5999 41** **** 6353"


def test_get_transaction_info():
    
    card_number = "Visa Platinum 1246377376343588"
    account_number = "Счет 72731966109147704472"
   

    transaction_info = get_transaction_info(card_number)

    assert isinstance(transaction_info, str)
   
    assert transaction_info == "Visa Platinum 1246 37** **** 3588"

    transaction_info = get_transaction_info(account_number)

    assert isinstance(transaction_info, str)

    assert transaction_info == "Счет **4472"


