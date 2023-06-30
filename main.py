from settings import PATH_WITH_FIXTURES
from utils import get_data, delete_empty_operations, get_first_five_sorted_operations

data = get_data(PATH_WITH_FIXTURES)

new_data = delete_empty_operations(data)

five_operations = get_first_five_sorted_operations(new_data)

print(five_operations)


if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
