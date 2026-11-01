# Piotr Olechno
# Module 10 - Problem 5: Assessed value of a home

def compute_assessed_value(county, market_value):
    county = county.strip().lower()
    if county == "cook":
        percent = 0.90
    elif county == "dupage":
        percent = 0.80
    elif county == "mchenry":
        percent = 0.75
    elif county == "kane":
        percent = 0.60
    else:
        percent = 0.70
    assessed_value = market_value * percent
    return assessed_value

total_market = 0
total_assessed = 0

response = input("Do you want to run the program? (Yes or No): ")
while response.lower() == "yes":
    county = input("Enter county: ")
    market_value = float(input("Enter market value: "))

    assessed = compute_assessed_value(county, market_value)
    print(f"Assessed value: ${assessed:,.2f}")
    total_market += market_value
    total_assessed += assessed

    response = input("Do you want to run the program again? (Yes or No): ")

print(f"Sum of all market values: ${total_market:,.2f}")
print(f"Sum of all assessed values: ${total_assessed:,.2f}")