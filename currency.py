def convert_currency(usd):
    exchange_rates = {
        "INR": 83.0,
        "EUR": 0.91,
        "GBP": 0.79,
    }
    inr = usd * exchange_rates["INR"]
    eur = usd * exchange_rates["EUR"]
    gbp = usd * exchange_rates["GBP"]
    return inr, eur, gbp
usd_amount = float(input("Enter amount in USD: "))
inr, eur, gbp = convert_currency(usd_amount)
print(f"USD {usd_amount} is equivalent to:")
print(f"INR: ₹{inr:.2f}")
print(f"EUR: €{eur:.2f}")
print(f"GBP: £{gbp:.2f}")