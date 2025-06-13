# Taxas de câmbio fixas (idealmente viriam de uma API)
RATES = {
    ("BRL", "USD"): 0.19,
    ("BRL", "EUR"): 0.18,
    ("USD", "BRL"): 5.56,
    ("USD", "EUR"): 0.94,
    ("EUR", "BRL"): 5.60,
    ("EUR", "USD"): 1.06,
}

def convert_currency(value: float, currency_from: str, currency_to: str) -> float:
    """Converte um valor entre duas moedas com base em taxas fixas."""
    if currency_from == currency_to:
        return round(value, 2)
    
    rate = RATES.get((currency_from, currency_to), 1.0)
    
    return round(value * rate, 2)