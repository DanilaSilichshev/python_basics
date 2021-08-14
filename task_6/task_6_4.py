class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Автомобиль поехал")

    def stop(self):
        print("Автомобиль остановился")

    def turn(self, direction):
        print(f"Автомобиль повернул {direction}")

    def show_speed(self):
        print(f"Текущая скорость составляет {self.speed} км/ч")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость составляет {self.speed} км/ч")

        if self.speed > 60:
            print(f"Скорость {self.name} выше позволительной")


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость составляет {self.speed} км/ч")

        if self.speed > 40:
            print(f"Скорость {self.name} выше позволительной")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_message(self, other_car):
        print(f"По скорости со спортивным автомобилем {self.name} уж точно не сравнится {other_car.name}")


unidentified = Car(70, "Бирюзовый", "Неопознанный", False)
ferrari = SportCar(350, "Красный", "Ferrari", False)
police = PoliceCar(140, "Сине-белый", "УАЗ")
gazel = WorkCar(50, "Зелёный", "Газель", False)
mercedes = TownCar(59, "Серебристый", "Мерседес А-класс", False)
print(unidentified.name, police.is_police, mercedes.speed)
unidentified.go()
unidentified.turn("налево")
unidentified.stop()
gazel.show_speed()
mercedes.show_speed()
ferrari.show_message(police)
