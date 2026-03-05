def add(a, b):
    return a + b
def add_with_bug(a, b):
    return a * b

def calculator_tax_bugged(income):
    return income * 0.15

def calculator_tax(income):
    if income < 0:
        raise ValueError(
            "could not have negative income"
        )
    return int(income * 0.15 * 100) / 100
