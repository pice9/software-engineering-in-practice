def calculate_subtotal(items: list[tuple[str, float, int]]) -> float:
    subtotal = 0
    for item, price, quantity in items:
        subtotal += price * quantity
    return subtotal


def calculate_discount(subtotal: float) -> float:
    if subtotal >= 50:
        return subtotal * 0.1
    return 0


def calculate_tax(amount: float) -> float:
    return amount * 0.08


def calculate_tip(amount: float, tip_rate: float) -> float:
    return amount * tip_rate


def calculate_bill(items: list[tuple[str, float, int]], tip_rate: float) -> dict[str, float]:
    bill = {}

    bill["subtotal"] = calculate_subtotal(items)

    bill["discount"] = calculate_discount(bill["subtotal"])

    bill["tax"] = calculate_tax(bill["subtotal"] - bill["discount"])

    bill["tip"] = calculate_tip(bill["subtotal"] - bill["discount"], tip_rate)

    bill["total"] = round(bill["subtotal"] - bill["discount"] + bill["tax"] + bill["tip"], 2)

    return bill
