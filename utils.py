import json

from settings import PATH_WITH_FIXTURES


def get_data(path):
    with open(path) as file:
        return json.load(file)

def delete_empty_operations(operations):
    operations.remove({})
    return operations


def get_first_five_sorted_operations(operation_list):
    return sorted(
        operation_list,
        key=lambda operation_data: (operation_data['state'], operation_data['date']),
        reverse=True
    )[:5]



class Operation:
    pass


def valid_data(operation_list):
    for operation in operation_list:
        if operation:
            oper = Operation(operation['id'], operation["state"],operation["date"], operation["operationAmount"], operation["description"], operation["from"], operation["to"])



