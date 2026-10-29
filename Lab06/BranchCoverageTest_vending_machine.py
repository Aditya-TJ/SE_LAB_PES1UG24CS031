"""Tests that exercise both outcomes of every decision in vending_machine.py."""

import pytest

from vending_machine import make_change, purchase, select_item


def test_select_item_branches():
    stock = {"cola": 1, "chips": 0, "candy": 1}
    assert select_item("water", stock, 500) == "invalid"
    assert select_item("cola", stock, 500) == "ok"
    assert select_item("chips", stock, 500) == "sold_out"
    assert select_item("cola", stock, 149) == "insufficient"
    assert select_item("cola", stock, 150) == "ok"
    assert select_item("candy", {}, 75) == "sold_out"


def test_make_change_branches_and_loop_exits():
    assert make_change(0) == []
    assert make_change(190) == [100, 50, 25, 10, 5]
    assert make_change(1) is None
    with pytest.raises(ValueError, match="negative amount"):
        make_change(-1)


def test_purchase_branches():
    stock = {"cola": 2, "chips": 0}
    assert purchase("water", stock, 200) == ("invalid", [])
    assert purchase("chips", stock, 200) == ("sold_out", [])
    assert purchase("cola", stock, 149) == ("insufficient", [])
    assert purchase("cola", stock, 151) == ("no_exact_change", [])
    assert stock["cola"] == 2
    assert purchase("cola", stock, 185) == ("dispensed", [25, 10])
    assert stock["cola"] == 1
