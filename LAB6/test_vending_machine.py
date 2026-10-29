import pytest
from vending_machine import select_item, make_change, purchase

#Example test cases:
def test_invalid_item():
    assert select_item("water", {}, 100) == "invalid"

def test_no_change_needed():
    assert make_change(0) == []

#Write the rest of the test cases so that the code is 90- 100% covered.
