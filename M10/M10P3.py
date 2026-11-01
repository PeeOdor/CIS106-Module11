# Piotr Olechno
# Module 10 - Problem 3: Out-the-door price of a car

def compute_out_the_door(msrp, make, model, ev_code):
    if ev_code.upper() == "Y":
        percent_off = 0.30
    elif make.lower() == "honda" and model.lower() == "accord":
        percent_off = 0.10
    elif make.lower() == "toyota" and model.lower() == "rav4":
        percent_off = 0.15
    else:
        percent_off = 0.05
    new_msrp = msrp - msrp * percent_off
    total = new_msrp * 1.07     # add 7% sales tax
    return total

total_msrp = 0
total_sales = 0

response = input("Do you want to run the program? (Yes or No): ")
while response.lower() == "yes":
    make = input("Enter make: ")
    model = input("Enter model: ")
    ev_code = input("Electric vehicle? (Y or N): ")
    msrp = float(input("Enter MSRP: "))

    price = compute_out_the_door(msrp, make, model, ev_code)
    print(f"Out the door price: ${price:,.2f}")

    total_msrp += msrp
    total_sales += price

    response = input("Do you want to run the program again? (Yes or No): ")

print(f"Sum of all MSRPs: ${total_msrp:,.2f}")
print(f"Sum of all sales prices: ${total_sales:,.2f}")