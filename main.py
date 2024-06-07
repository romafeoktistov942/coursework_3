import json
import datetime as dt
from helpers import *


def main():
    """
    This is the main function of the program. 
    It reads transactions from a JSON file, sorts them by date in descending order, 
    filters out only the executed transactions and prints the latest 5 transactions.
    """
    with open("operations.json", "r") as data:
        transactions = json.loads(data.read())

    transactions = sorted(
        transactions,
        key=lambda x: (
            dt.datetime.strptime(x.get("date", ""), "%Y-%m-%dT%H:%M:%S.%f")
            if x.get("date")
            else dt.datetime.min
        ),
        reverse=True,
    )

    transactions = [tr for tr in transactions if tr.get("state") == "EXECUTED"][
        :5
    ]

    for tr in transactions:

        # первая строчка

        operation_info = (
            dt.datetime.strptime(tr["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime(
                "%d.%m.%Y"
            )
            + " "
            + tr["description"]
        )

        if tr.get("from"):
            operation_route = (
                get_transaction_info(tr.get("from"))
                + " -> "
                + get_transaction_info(tr.get("to"))
            )
        else:
            operation_route = get_transaction_info(tr.get("to"))

        print(operation_info)
        print(operation_route)
        print(
            tr["operationAmount"]["amount"]
            + " "
            + tr["operationAmount"]["currency"]["name"],
            end="\n\n",
        )


if __name__ == "__main__":
    main()
