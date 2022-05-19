class Road:

    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width

    def calculate(self, height: int = 5, mass_m_2: int = 25) -> int:
        return int((self._length * self._width * height * mass_m_2) / 1000)

if __name__ == '__main__':
    road = Road(5000, 20)
    print(f'Для изготовления покрытия дороги нужно {road.calculate()} тонн.')