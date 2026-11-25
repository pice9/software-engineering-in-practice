from billing.calculator import (
    calculate_bill,
    calculate_discount,
    calculate_subtotal,
    calculate_tax,
    calculate_tip,
)


def test_calculate_subtotal_sums_multiple_items():
    items = [("Burger", 12.50, 2), ("Fries", 4.00, 2)]

    result = calculate_subtotal(items)

    assert result == 33.00


def test_calculate_discount_when_subtotal_less_than_50():
    subtotal = 45

    result = calculate_discount(subtotal)

    assert result == 0


def test_calculate_discount_when_subtotal_more_or_equal_50():
    subtotal = 50

    result = calculate_discount(subtotal)

    assert result == 5


def test_calculate_tax():
    subtotal = 76

    tax = calculate_tax(subtotal)

    assert tax == 6.08


def test_calculate_tip():
    subtotal = 32

    tip = calculate_tip(subtotal, 0.2)

    assert tip == 6.4


def test_calculate_bill():
    items = [
        ("Burger", 12.50, 2),
        ("Fries", 4.00, 2),
        ("Soda", 2.50, 2),
    ]
    tip_rate = 0.15

    bill = calculate_bill(items, tip_rate)

    assert bill["total"] == 46.74


def test_calculate_bill_applies_tax_after_discount_on_large_order():
    # Tax
    subtotal = 60
    discount = calculate_discount(subtotal)

    tax = calculate_tax(subtotal - discount)

    assert tax == 4.32

    # Tip
    subtotal = 60
    discount = calculate_discount(subtotal)
    tip_rate = 0.15

    tip = calculate_tip(subtotal - discount, tip_rate)

    assert tip == 8.1

    # Total
    items = [("Steak", 30, 2)]
    tip_rate = 0.15

    bill = calculate_bill(items, tip_rate)

    assert bill["total"] == 66.42
