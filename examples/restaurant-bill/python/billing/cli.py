from billing.calculator import calculate_bill


def main():
    items = [
        ("Burger", 12.50, 2),
        ("Fries", 4.00, 2),
        ("Soda", 2.50, 2),
    ]
    tip_rate = 0.15
    bill = calculate_bill(items, tip_rate)

    print("Receipt")
    print("-------")
    for name, price, qty in items:
        print(f"{name}: {qty} x ${price:.2f} = ${price * qty:.2f}")

    print(f"Subtotal: ${bill['subtotal']:.2f}")
    print(f"Discount: -${bill['discount']:.2f}")
    print(f"Tax: ${bill['tax']:.2f}")
    print(f"Tip: ${bill['tip']:.2f}")
    print(f"Total: ${bill['total']:.2f}")
