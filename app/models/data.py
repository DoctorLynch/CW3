import json

from settings import PATH_WITH_FIXTURES


def get_data(path):
    with open(path) as file:
        return json.load(file)


data = get_data(PATH_WITH_FIXTURES)


def delete_empty_operations(operations):
    operations.remove({})
    return operations


new_data = delete_empty_operations(data)


def get_first_five_sorted_operations(operation_list):
    return sorted(
        operation_list,
        key=lambda operation_data: (operation_data['state'], operation_data['date']),
        reverse=True
    )[:5]


five_operations = get_first_five_sorted_operations(new_data)