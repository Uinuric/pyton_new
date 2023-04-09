class OfficeEquipment:
    def __init__(self, type, model, sn):
        self.type = str(type)
        self.model = str(model)
        self.sn = str(sn)


class Printer(OfficeEquipment):
    def __init__(self, model, sn, is_color: bool):
        self.is_color = is_color


class Scanner(OfficeEquipment):
    def __init__(self, model, sn, format):
        self.format = format


class Copier(OfficeEquipment):
    def __init__(self, model, sn, for_pc: bool):
        self.for_pc = for_pc
