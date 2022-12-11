# TODO Написать 3 класса с документацией и аннотацией типов
class Pot:
    def __init__(self, capacity_volume: int, occupied_volume: int):
        """
               Создание и подготовка к работе объекта "Кастрюля"
               :param capacity_volume: Объем кастрюли
               :param occupied_volume: Объем занимаемой жидкости
               Примеры:
               >>> pot1 = Pot(1000, 0)
               """
        if not isinstance(capacity_volume, (int)):
            raise TypeError("Объем кастрюли указан не целочисленным значением")
        if not capacity_volume > 0:
            raise ValueError("Объем кастрюли не может быть отрицательным")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int)):
            raise TypeError("Объем занимаемого места указан не целочисленным значением")
        if occupied_volume < 0:
            raise ValueError("Объем занимаемого места не может быть отрицательным")
        self.occupied_volume = occupied_volume

    def is_empty_pot(self) -> bool:
        """
                Функция которая проверяет является ли кастрюля пустой
                :return: Является ли кастрюля пустой
                Примеры:
                >>> pot1 = Pot(1000, 0)
                >>> pot1.is_empty_pot()
                """
        ...

    def add_ingredients_to_pot(self, ingredients: int) -> None:
        """
               Добавление ингредиентов в кастрюлю.
               :param ingredients: Объем добавляемых ингредиентов
               :raise ValueError: Если количество добавляемых ингредиентов превышает свободное место в кастрюле, то вызываем ошибку
               Примеры:
               >>> pot1 = Pot(1000, 0)
               >>> pot1.add_ingredients_to_pot(500)
               """
        if not isinstance(ingredients, (int)):
            raise TypeError("Объем добавляемых ингредиентов должнен быть типа int")
        if ingredients < 0:
            raise ValueError("Объем добавляемых ингредиентов должнен быть выражен положительным числом")
        ...


class Pillbox:
    def __init__(self, capacity_slots: int, occupied_slots: int):
        """
                Создание и подготовка к работе объекта "Таблетница"
                :param capacity_slots: Общее количество слотов в таблетнице
                :param occupied_slots: Количество занятых слотов в таблетнице
                Примеры:
                    >>> pillbox1 = Pillbox(7, 0)
                      """
        if not isinstance(capacity_slots, (int)):
            raise TypeError("Объем таблетницы указан не целочисленным значением")
        if not capacity_slots > 0:
            raise ValueError("Объем таблетницы не может быть отрицательным")
        self.capacity_slots = capacity_slots

        if not isinstance(occupied_slots, (int)):
            raise TypeError("Объем занимаемого места указан не целочисленным значением")
        if occupied_slots < 0:
            raise ValueError("Объем занимаемого места не может быть отрицательным")
        self.occupied_slots = occupied_slots

    def is_recharged_pillbox(self) -> bool:
        """
                Функция которая проверяет является ли таблетница заполненной
                :return: Является ли таблетница пустой
                Примеры:
                    >>> pillbox1 = Pillbox(7, 0)
                    >>> pillbox1.is_recharged_pillbox()
                """
        ...

    def add_tabs_to_pillbox(self, tabs: int):
        """
                Добавление таблеток в таблетницу.
                :param tabs: Объем добавляемых ингредиентов
                :raise ValueError: Если количество добавляемых таблеток превышает свободное место в таблетнице, то вызываем ошибку
                Примеры:
                    >>> pillbox1 = Pillbox(7, 0)
                    >>> pillbox1.add_tabs_to_pillbox(12)
                """
        if not isinstance(tabs, (int)):
            raise TypeError("Добавляемые таблетки должнны быть типа int")
        if tabs < 0:
            raise ValueError("Добавляемые таблетки должнны быть выражены положительным числом")
        ...

    def last_slot_used(self, used_slots: int) -> None:
        """
                Метод увеличивает последний исапользованный слот.
                :param used_slots: Количество использованных слотов
                """
        ...

class CreditCard:
    def __init__(self, owner_name: str, available_funds: int):
        """
               Создание и подготовка к работе объекта "Кредитка"
               :param owner_name: Имя владельца
               :param available_funds: Сумма доступных средств на карте
               Примеры:
               >>> creditcard1 = CreditCard("John", 300)
               """
        if not isinstance(owner_name, (str)):
            raise TypeError("Имя владельца должно быть выраженно буквами")
        self.owner_name = owner_name

        if not isinstance(available_funds, (int, float)):
            raise TypeError("Сумма доступных средств на карте указана неверно")
        if available_funds < 0:
            raise ValueError("ОСумма доступных средств на карте не может быть отрицательной")
        self.available_funds = available_funds

    def withdraw_money(self, withdrawn_money: int) -> None:
        """
                Метод уменьшает количество средств на каре.
                :param withdrawn_money: Количество снятых средств с карты
                :raise TypeError: Если введен неверный тип данных, возвращается ошибка
                :raise ValueError: Если сумма отрицательная, возвращается ошибка
                :return: Обновленная сумма на счету
                """
        ...

    def add_money(self, added_money: int) -> None:
        """
                Метод увеличивает количество средств на каре.
                :param added_money: Количество добавленных средств на карту
                :raise TypeError: Если введен неверный тип данных, возвращается ошибка
                :raise ValueError: Если сумма положительная, возвращается ошибка
                :return: Обновленная сумма на счету
                """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
