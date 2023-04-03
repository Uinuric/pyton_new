class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f"Поехала {self.name} "

    def stop(self):
        return f"Остановилась "

    def turn(self, direction):
        return f" поворот на  {direction} "

    def show_speed(self):
        return f"Скорость {self.speed}"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f"Скорость выше допустимой {self.speed}"


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Скорость выше допустимой {self.speed}"


class PoliceCar(Car):
    pass


town = TownCar("Трамвай ", 80, "белый", False)
print(f"{town.go()}, {town.color}, {town.show_speed()}, {town.turn('лево')}, {town.turn('право')}, {town.stop()}")

sport = SportCar("Спортивный автомобиль ", 160, "синяя", False)
print(f"{sport.go()}, {sport.color}, {sport.turn('лево')}, {sport.turn('право')}, {sport.stop()}")

work = WorkCar("Рабочая машина ", 10, "оранжевая", False)
print(f"{work.go()}, {work.color}, {work.show_speed()}, {work.turn('лево')}, {work.turn('право')}, {work.stop()}")

policeCar = PoliceCar('ГИБДД', 120, 'в полосочку', True)
print(f"{policeCar.go()}, {policeCar.color}, {policeCar.turn('лево')}, {policeCar.turn('право')}, {policeCar.stop()}")
