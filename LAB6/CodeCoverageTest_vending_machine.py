"""Tests used to measure statement (code) coverage of vending_machine.py."""

import pytest

from vending_machine import make_change, purchase, select_item


def test_select_item_outcomes():
    stock = {"cola": 2, "chips": 0, "candy": 1}
    assert select_item("water", stock, 200) == "invalid"
    assert select_item("chips", stock, 200) == "sold_out"
    assert select_item("cola", stock, 149) == "insufficient"
    assert select_item("cola", stock, 150) == "ok"
    assert select_item("candy", {}, 75) == "sold_out"


def test_make_change_outcomes():
    assert make_change(0) == []
    assert make_change(185) == [100, 50, 25, 10]
    assert make_change(1) is None
    with pytest.raises(ValueError, match="negative amount"):
        make_change(-1)


def test_purchase_outcomes_and_stock_updates():
    stock = {"cola": 2, "chips": 0}
    assert purchase("water", stock, 200) == ("invalid", [])
    assert purchase("chips", stock, 200) == ("sold_out", [])
    assert purchase("cola", stock, 149) == ("insufficient", [])
    assert purchase("cola", stock, 151) == ("no_exact_change", [])
    assert stock["cola"] == 2
    assert purchase("cola", stock, 185) == ("dispensed", [25, 10])
    assert stock["cola"] == 1
