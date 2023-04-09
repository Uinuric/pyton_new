class Warehouse:
    technic = []

    def push(self, equipment):
        if equipment.type == "Принтер":
            if (isinstance(equipment.is_color, bool)):
                self.technic.append(equipment)
                print(f"Добавлен принтер:  {equipment.model}")
            else:
                print(f"По данному параметру не понятно о цветности принтера: {equipment.is_color}")
        elif equipment.type == "Ксерокс":
            if (isinstance(equipment.for_pc, bool)):
                self.technic.append(equipment)
                print(f"Добавлен МФУ:  {equipment.model}")
            else:
                print(f"По данному параметру не понятно по подключении к ПК: {equipment.for_pc}")


class OfficeEquipment:
    def __init__(self, type, model, sn):
        self.type = str(type)
        self.model = str(model)
        self.sn = str(sn)


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
warehouse.push(Printer("HP 1010", "654456654", 456))
warehouse.push(Printer("Kyosera 2040", "12321456", False))
warehouse.push(Copier("Epson", "654456654", "kjsdksdj"))
warehouse.push(Copier("Xerox 520", "12321456", False))
