# pylint: disable=missing-docstring

# TODO: add some currency rates
RATES = {

    "USDEUR": 0.85,
    "GBPEUR": 1.13,
    "CHFEUR": 0.86,
    "EURGBP": 0.885
}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    value = amount[0]
    origin_currency = amount[1]
    target_currency = currency
    total_currency = origin_currency + target_currency

    if total_currency in RATES:
       return round(value * RATES[total_currency])
