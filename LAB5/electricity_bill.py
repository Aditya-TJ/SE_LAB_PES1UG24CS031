
"""Calculate electricity bills and save billing records."""

import json

from defusedxml import ElementTree as ET

SLABS = [(100, 3.5), (200, 5.0), (300, 6.5)]
HIGH_RATE = 8.0
FIXED_CHARGE = 75

METER_XML = """<meters>
    <meter id='M1' prev='1200' curr='1350'/>
    <meter id='M2' prev='5000' curr='5420'/>
    <meter id='M3' prev='800' curr='760'/>
</meters>"""

bills = []


def read_meters(xml_text):
    """Read meter IDs and previous/current readings from XML."""
    root = ET.fromstring(xml_text)
    return [
        (meter.get("id"), int(meter.get("prev")), int(meter.get("curr")))
        for meter in root.findall("meter")
    ]


def calculate_units(previous, current):
    """Calculate units consumed from two meter readings."""
    if current < previous:
        print("Warning: meter reading went backwards")
        return 0
    return current - previous


def energy_charge(units):
    """Calculate the energy charge using the slab rates."""
    charge = 0
    lower = 0
    remaining = units

    for limit, rate in SLABS:
        slab_units = min(remaining, limit - lower)
        if slab_units > 0:
            charge += slab_units * rate
            remaining -= slab_units
        lower = limit

    return charge + remaining * HIGH_RATE


def generate_bill(meter_id, units, tax_rate=0.05, extras=None):
    """Generate a bill and add it to the billing records."""
    if extras is None:
        extras = {}

    amount = energy_charge(units) + FIXED_CHARGE + sum(extras.values())
    bill = {
        "meter": meter_id,
        "units": units,
        "amount": round(amount * (1 + tax_rate), 2),
    }
    bills.append(bill)
    return bill


def average_bill():
    """Return the average bill amount, or zero when there are no bills."""
    if not bills:
        return 0
    return round(sum(bill["amount"] for bill in bills) / len(bills), 2)


def save_bills(file_name="bills.json"):
    """Save billing records as formatted JSON."""
    with open(file_name, "w", encoding="utf-8") as output_file:
        json.dump(bills, output_file, indent=2)


def main():
    """Calculate, display, and save electricity bills."""
    for meter_id, previous, current in read_meters(METER_XML):
        units = calculate_units(previous, current)
        generate_bill(meter_id, units)

    generate_bill("M4", 50, extras={"late_fee": 25})

    for bill in bills:
        print(
            bill["meter"],
            "used",
            bill["units"],
            "units, bill Rs.",
            bill["amount"],
        )

    highest = max(bills, key=lambda bill: bill["amount"])
    print("Highest bill:", highest["meter"])
    print("Average bill:", average_bill())
    total = sum(bill["amount"] for bill in bills)
    print("Total billed:", round(total, 2))

    save_bills()
    print("Saved", len(bills), "bills to bills.json")


if __name__ == "__main__":
    main()
