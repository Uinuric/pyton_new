class DataStyle:
    def __init__(self, v_date):
        self.v_date = v_date
        self.day, self.month, self.year = map(int, v_date.split('-'))

    @classmethod
    def extract(cls, v_date):
        date = cls(v_date)
        return [date.day, date.month, date.year]

    @staticmethod
    def validate(v_date):
        date = DataStyle(v_date)
        if date.month in range(1, 12):
            return f"прошла успешно"
        else:
            return f" месяц в дате за пределами разумного!"


var_date = '22-16-1983'
real_date = DataStyle(var_date)
print(f"Проверка месяца даты: {real_date.validate(var_date)}")
print(f"Дата преобразована в числа {real_date.extract(var_date)}")
