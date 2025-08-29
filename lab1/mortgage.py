"""Calculate the monthly cost of a loan."""

import json
from pathlib import Path


# Input
json_file = Path(__file__).with_name("loan_details.json")
with open(json_file, "r", encoding="utf-8") as file:
    content = file.read()
data = json.loads(content)

house_price = data["house_price"]
deductible = data["deductible"]
years = data["years"]
yearly_interest_rate_pct = data["yearly_interest_rate_pct"]
monthly_fee = data["monthly_fee"]


# Computation
loan = house_price - deductible
months = years * 12

yearly_rate = yearly_interest_rate_pct / 100
monthly_rate = yearly_rate / 12

discount_factor = (1 - (1 + monthly_rate) ** -months) / monthly_rate
monthly_term_amount = loan / discount_factor + monthly_fee
monthly_term_amount = round(monthly_term_amount, 2)


# Output
print(f'Monthly term amount: {monthly_term_amount}')
