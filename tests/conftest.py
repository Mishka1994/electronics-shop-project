import pytest
from src.item import Item


@pytest.fixture()
def item_1():
    return Item('Смартфон', 5000, 5)
