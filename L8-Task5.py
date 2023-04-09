class Warehouse:
    technic = []

    def push(self, equipment):
        self.technic.append(equipment)


class OfficeEquipment:
    def __init__(self, type, model, sn):
        self.type = str(type)
        self.model = str(model)
        self.sn = str(sn)

    def __str__(self):
        return f"{self.type} {self.model}"


class Printer(OfficeEquipment):
    def __init__(self, model, sn, is_color: bool):
        self.is_color = is_color
        super().__init__('Принтер', model, sn)


class Scanner(OfficeEquipment):
    def __init__(self, model, sn, format):
        self.format = format
        super().__init__('Сканер', model, sn)


class Copier(OfficeEquipment):
    def __init__(self, model, sn, for_pc: bool):
        self.for_pc = for_pc
        super().__init__('Ксерокс', model, sn)


warehouse = Warehouse()
warehouse.push(Printer('Epson L120', 'N6SS549876548', True))
