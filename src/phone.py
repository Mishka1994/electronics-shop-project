from src.item import Item


class Phone(Item):
    """
    Класс наследует поведение от класса Item
    При инициализации принимает один доп. параметр
    __number_of_sim: количество сим_карт в устройстве
    """
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, numb):
        if isinstance(numb, int) and numb > 0:
            self.__number_of_sim = numb
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if isinstance(self, Item) and issubclass(other.__class__, Item):
            return self.quantity + other.quantity

