import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture()
def item_1():
    return Item('Смартфон', 10000, 20)


@pytest.fixture()
def phone_1():
    return Phone("iPhone 14", 120000, 5, 2)
