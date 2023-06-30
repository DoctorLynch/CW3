import re
from datetime import datetime


class Operation:
    def __init__(self, oper_id, oper_date, transw_state, operation_amount, description_type, _to_, _from_=''):
        self.oper_id = oper_id
        self.oper_date = oper_date
        self.transw_state = transw_state
        self.operation_amount = operation_amount
        self.description_type = description_type
        self._to_ = self._encode_data(_to_)
        self._from_ = self._encode_data(_from_) if _from_ else ''

    @staticmethod
    def _encode_data(value):
        data = value.split()
        number_card = data[-1]
        if value.startswith('Счет'):
            data[-1] = '**' + data[-1][-4:]
            return ' '.join(data)

        hidden_number = number_card[0:6] + '******' + number_card[-4:]
        result = ' '.join(re.findall('(.{%s}|.+$)' % 4, hidden_number))
        data[-1] = result
        return ' '.join(data)
    @property
    def _encoded_date(self):
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        date = datetime.strptime(self.date, date_format)
        return date.date().strftime('%d.%m.%Y')
    def get_into_for_operation(self):
            return f'{self._encoded_date} {self.description_type} {self._from_ if self._from_ else ''} ->


