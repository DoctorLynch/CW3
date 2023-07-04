from pathlib import Path
from app.models.data import get_data, get_first_five_sorted_operations
from app.models.operation import Operation
from settings import PATH_WITH_FIXTURES
from tests.conftest import valid_data


def test_get_data():
    data = get_data(PATH_WITH_FIXTURES)
    assert isinstance(data, list)
    assert isinstance(data[0], dict)


