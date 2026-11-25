from billing.calculator import calculate_subtotal, calculate_discount, calculate_tax, calculate_tip, calculate_bill

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