import json
from datetime import datetime
from settings import PATH_WITH_FIXTURES


#def get_data(path):
    with open(path) as file:
        return json.load(file)


data = get_data(PATH_WITH_FIXTURES)


#def delete_empty_operations(operations):
    operations.remove({})
    return operations


new_data = delete_empty_operations(data)


#def get_first_five_sorted_operations(operation_list):
    return sorted(
        operation_list,
        key=lambda operation_data: (operation_data['state'], operation_data['date']),
        reverse=True
    )[:5]


five_operations = get_first_five_sorted_operations(new_data)







#class Operation:
    #def __init__(self, oper_id, oper_date_, transw_state, operation_amount, description_type, _to_, _from_=''):
        self.oper_id = oper_id
        self.oper_date = self._encoded_date(oper_date_)
        self.transw_state = transw_state
        self.operation_amount = operation_amount
        self.description_type = description_type
        self._to_ = self.numbers_masking(_to_)
        self._from_ = self.numbers_masking(_from_)if _from_ else ''

    #def _encoded_date(self, oper_date):
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        oper_date = datetime.strptime(oper_date, date_format)
        return datetime.strftime(oper_date, '%d.%m.%Y')

    @staticmethod
    #def numbers_masking(account_number: str) -> str:
        """
        Метод принимает на входе строку с номером кредитной карты
        или номером счета и возвращает их с частично замаскированными
        символом '*' цифрами
        """
        if account_number.startswith('Счет'):
            list_card_number = account_number.split(' ')
            new_number = f'**{list_card_number[-1][-4:]}'
        else:
            list_card_number = account_number.split(' ')
            new_number = f'{list_card_number[-1][0: 4]} {list_card_number[-1][4: 6]}** **** {list_card_number[-1][-4:]}'
        list_card_number[-1] = new_number
        return ' '.join(list_card_number)






    def __str__(self):
        return f'{self.oper_date} {self.description_type}\n{self._from_} -> {self._to_}\n{self.operation_amount["amount"] + " " + self.operation_amount["currency"]["name"] }'


