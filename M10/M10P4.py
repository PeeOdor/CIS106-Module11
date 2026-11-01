# Piotr Olechno
# Module 10 - Problem 4: Train ticket price

def compute_ticket_price(miles):
    if miles >= 30:
        price = 12
    elif miles >= 20:
        price = 10
    elif miles >= 10:
        price = 8
    else:
        price = 5
    return price

total_tickets = 0

response = input("Do you want to run the program? (Yes or No): ")
while response.lower() == "yes":
    last_name = input("Enter last name: ")
    miles = float(input("Enter miles from downtown Chicago: "))

    price = compute_ticket_price(miles)
    print(f"{last_name}, your ticket price is ${price:,.2f}")
    total_tickets += price

    response = input("Do you want to run the program again? (Yes or No): ")

print(f"Sum of all ticket prices: ${total_tickets:,.2f}")