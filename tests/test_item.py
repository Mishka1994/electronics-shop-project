"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture()
def item_1():
    return Item('Смарфтон', 5000, 5)


def test_item_name(item_1):
    assert item_1.get_value() == ("Смарфтон", 5000, 5)


def test_calc_total_price(item_1):
    assert item_1.calculate_total_price() == 25000.0


def test_apply_discount(item_1):
    assert item_1.apply_discount() == 5000.0

