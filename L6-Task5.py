class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f" лоыар ывлоар ылоар ыловар лыво лывоар "


class Pen(Stationery):
    def draw(self):
        return f"Рисуем {self.title}"


class Pencil(Stationery):
    def draw(self):
        return f"Рисуем {self.title}"


class Handle(Stationery):
    def draw(self):
        return f"Рисуем {self.title}"


pen = Pen("ручкой")
print(pen.draw())
pencil = Pencil("карандашем")
print(pencil.draw())
handle = Handle("маркером")
print(handle.draw())
