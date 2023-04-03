from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 1
        while True:
            print(f"На светофоре горит {TrafficLight.__color[i - 1]} цвет")
            if i == 1:
                sleep(7)
            elif i == 2:
                sleep(2)
            elif i == 3:
                sleep(5)
                i = 0
            i += 1


my_class = TrafficLight()
my_class.running()
