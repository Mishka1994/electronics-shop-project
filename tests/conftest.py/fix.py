import pytest
from src.item import Item


@pytest.fixture()
def item_1():
    return Item('Смарфтон', 5000, 5)
