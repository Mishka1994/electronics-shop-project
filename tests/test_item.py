"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


def test_item_name(item_1):
    assert item_1.name == 'Смартфон'
    assert item_1.price == 5000
    assert item_1.quantity == 5


def test_calc_total_price(item_1):
    assert item_1.calculate_total_price() == 25000.0


def test_apply_discount(item_1):
    Item.pay_rate = 0.8
    item_1.apply_discount()
    assert item_1.price == 4000.0

