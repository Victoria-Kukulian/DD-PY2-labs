import doctest


class Cars:
    """ Базовый класс автомобилей.
    :param brand: производитель
    :param model: модель
    :param speed: скорость
    """
    def __init__(self, brand: str, model: str, speed: int):
        self.brand = brand
        self.model = model
        self.speed = speed

    def __str__(self) -> str:
        return f"Производитель {self.brand}, модель {self.model}, скорость {self.speed}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(brand={self.brand!r}, model={self.model!r}), speed={self.speed!r}"

    def speed_check(self, speed: int) -> str:
        """
        Метод, проверяющий, что скорость автомобиля задана типом int и превышает 0.
        :param speed: скорость
        :raise TypeError: вызвать ошибку, если указан не тип int.
        :raise ValueError: вызвать ошибку, если указана скорость равная 0 или ниже.
        """

        if not isinstance(speed, int):
            raise TypeError("Cкорость автомобиля должна быть типа int")
        elif self.speed <= 0:
            raise ValueError("Cкорость автомобиля должна быть более 0")
        return f"Скорость автмобиля указана верно."

    def increase_speed(self, speed_increase: int) -> None:
        """
        Метод, увеличивающий скорость на заданное значение.
        :param speed_increase: значение, на которое увеличивается скорость
        """
        self.speed += speed_increase


class Lorry(Cars):
    """
    Подкласс грузовиков класса автомобилей.
    :param brand: производитель
    :param model: модель
    :param speed: скорость
    :param cargo_load: вес перевозимого груза
    """
    def __init__(self, brand: str, model: str, speed: int, cargo_load: int):
        super().__init__(brand, model, speed)
        self.cargo_load = cargo_load

    def __str__(self) -> str:
        """
        Перегрузка метода __str__ в связи с появлением нового атрибута.
        """
        return f"{super().__str__()}, вес перевозимого груза: {self.cargo_load!r}"

    def __repr__(self) -> str:
        """
        Перегрузка метода __repr__ в связи с появлением нового атрибута.
        """
        return f"{super().__repr__()}, {self.cargo_load!r})"

    def increase_speed(self, speed_increase: int) -> None:
        """
        Перегрузка метода класса increase_speed с учетом влияния веса перевозимого груза.
        :param speed_increase: значение, на которое увеличивается скорость
        """
        self.speed += speed_increase * (1 + self.cargo_load / 1000)


if __name__ == "__main__":
    doctest.testmod()
    pass
