from src.helpers import (
    mask_account,
    mask_card,
    get_transaction_info,
    get_operations,
    sort_operations_by_date,
    format_operation_to_output,
    get_only_executed,
)


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


def test_get_operations():
    operations = get_operations("operations.json")
    assert isinstance(operations, list)
    assert len(operations) > 0


def test_sort_operations_by_date():
    operations = get_operations("operations.json")
    sorted_operations = sort_operations_by_date(operations)
    assert isinstance(sorted_operations, list)
    assert len(sorted_operations) == len(operations)
    assert sorted_operations[1]["date"] < sorted_operations[0]["date"]

def test_get_only_executed():
    operations = get_operations("operations.json")
    executed_operations = get_only_executed(operations)
    assert isinstance(executed_operations, list)
    assert len(executed_operations) <= len(operations)
    for operation in executed_operations:
        assert operation["state"] == "EXECUTED"

def test_format_operation_to_output():
    operations = get_operations("operations.json")
    sorted_operations = sort_operations_by_date(operations)
    executed_operations = get_only_executed(sorted_operations)
    output = format_operation_to_output(executed_operations[0])
    assert isinstance(output, str)
    assert len(output) > 0
    assert "08.12.2019" in output
    assert "Счет" in output
    assert "USD" in output
