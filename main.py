from src.helpers import *


def main():
    """
    This is the main function of the program. 
    It reads transactions from a JSON file, sorts them by date in descending order, 
    filters out only the executed transactions and prints the latest 5 transactions.
    """
    all_operations = get_operations('operations.json')
    sorted_operations = sort_operations_by_date(all_operations)
    executed_operations = get_only_executed(sorted_operations)
    last_five_operations = executed_operations[:5]

    
    for operation in last_five_operations:
        formated_operation_info = format_operation_to_output(operation)
        print(formated_operation_info, end='\n\n') 


if __name__ == "__main__":
    main()
