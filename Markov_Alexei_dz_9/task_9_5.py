class Stationery:

    def __init__(self, title: str) -> None:
        ...

    def draw(self) -> None:
        ...


# определите классы ниже согласно условий задания
class Pen(Stationery): ...
class Pencil(Stationery): ...
class Handle(Stationery): ...


if __name__ == '__main__':
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')
    pen.draw()  # Pen: приступил к отрисовке объекта "Ручка"
    handle.draw()  # Handle: приступил к отрисовке объекта "Маркер"
    pencil.draw()  # Пример вывода ниже в многострочном комментарии
    """
    Запуск отрисовки
    Pencil: приступил к отрисовке объекта "Карандаш"
    """