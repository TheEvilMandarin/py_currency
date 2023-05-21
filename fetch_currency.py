def fetch_currency(json_rates, code):
    Previous = json_rates["Valute"][code]["Previous"]
    Nominal = json_rates["Valute"][code]["Nominal"]
    Value = json_rates["Valute"][code]["Value"]
    Name = json_rates["Valute"][code]["Name"]

    prev = Previous / Nominal
    val = Value / Nominal
    return prev, val, Name
