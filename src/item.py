import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", newline='', encoding='cp1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for x in reader:
                Item.all.append(Item(x["name"], x["price"], x["quantity"]))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            raise Exception("Длина превышает 10 символов")
        else:
            self.__name = new_name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @staticmethod
    def string_to_number(string):
        """
        Из переданной строки возвращает первый символ-цифру.
        @param string: Строка для поиска символа.
        @return: Возвращает цифру.
        """
        for x in range(len(string)):
            if string[x].isdigit():
                return int(string[x])
