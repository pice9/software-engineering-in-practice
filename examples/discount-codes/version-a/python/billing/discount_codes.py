DISCOUNT_CODES = {
    "SAVE5": lambda amount: 5.0,
    "SAVE10": lambda amount: amount * 0.1,
    "SAVE20": lambda amount: amount * 0.2,
}

def apply_discount_code(amount: float, code: str):
    if code not in DISCOUNT_CODES:
        raise ValueError(f"unknown discount code: {code}") from None
    discount_fn = DISCOUNT_CODES[code]
    return discount_fn(amount)