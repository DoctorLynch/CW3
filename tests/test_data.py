from datetime import datetime
from pathlib import Path
from app.models.data import get_data, get_first_five_sorted_operations
from app.models.operation import Operation
from settings import PATH_WITH_FIXTURES

from tests.conftest import valid_data


def test_get_data():
    data = get_data(PATH_WITH_FIXTURES)
    assert isinstance(data, list)
    assert isinstance(data[0], dict)

def test_numbers_masking():
    number_1 = Operation
    assert number_1.numbers_masking('1596837868705199') == '1596 83** **** 5199'

def test_Operation():
    number_2 = Operation(441945886, "EXECUTED", "2019-08-26T10:50:58.294041", {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    }, "Перевод организации", "Maestro 1596837868705199", "Счет 64686473678894779589")
    assert number_2.__init__(441945886, "EXECUTED", "2019-08-26T10:50:58.294041", {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    }, "Перевод организации", "Maestro 1596837868705199", "Счет 64686473678894779589")

# def test_get_first_five_sorted_operations(valid_data):
#     data = get_data(PATH_WITH_FIXTURES)
#     data.data = valid_data
#
#     operation_list = data.get_first_five_sorted_operations()
#     assert isinstance(operation_list, list)
#     assert isinstance(operation_list[0], Operation)
#     assert len(operation_list) == 2
#     assert operation_list[1].oper_id == valid_data[0]['id']


