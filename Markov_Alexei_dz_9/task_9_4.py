class Car:
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self) -> None:
        self.speed += 15
        print(f'Машина {self.name} повысила скорость на 15: {self.speed}')

    def stop(self) -> None:
        self.speed = 0
        print(f'{self.name}: остановилась')

    def turn(self, direction: str) -> None:
        if ['направо', 'налево', 'прямо', 'назад'].count(direction):
            print(f'{self.name}: движется {direction}')
        else:
            raise ValueError('нераспознанное направление движения')

    def show_speed(self) -> None:
        print(f'{self.name}: текущая скорость {self.speed} км/час')
        if self.is_police:
            print(f'Вруби мигалку и забудь про скорость!')


class TownCar(Car):
    def show_speed(self) -> None:
        if self.speed > 60:
            print(f'Alarm!!! Speed!!!')
        else:
            print(f'{self.name}: текущая скорость {self.speed} км/час')


class WorkCar(Car):
    def show_speed(self) -> None:
        if self.speed > 40:
            print(f'Alarm!!! Speed!!!')
        else:
            print(f'{self.name}: текущая скорость {self.speed} км/час')


class SportCar(Car): ...


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str):
        super().__init__(speed, color, name)
        self.is_police = True


if __name__ == '__main__':
    town_car = TownCar(41, "red", 'WW_Golf')
    work_car = WorkCar(41, 'yellow', 'BobCat')
    police_car = PoliceCar(120, "blue", 'BMW')
    sport_car = SportCar(300, 'white', 'Ferrari')
    town_car.go()  # Машина WW_Golf повысила скорость на 15: 56
    town_car.show_speed()  # WW_Golf: текущая скорость 56 км/час
    work_car.show_speed()  # Alarm!!! Speed!!!
    town_car.stop()  # WW_Golf: остановилась
    police_car.show_speed()
    sport_car.turn('назад')  # Ferrari(SportCar): движется назад
    sport_car.turn('right')
