from time import sleep


class TrafficLight:
    __color = ("Красный", "Жёлтый", "Зелёный")

    def turning_color(self):
        c = 0
        while c < 3:
            print(f"Сейчас горит {self.__color[c]} цвет")
            if c == 0:
                sleep(7)
                c += 1
            elif c == 1:
                sleep(2)
                c += 1
            elif c == 2:
                sleep(5)
                c = 0


TrafficLight_object = TrafficLight()
TrafficLight_object.turning_color()
