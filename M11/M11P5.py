# Module 11 Problem 5 - Total and tax using global variables

TAX_RATE = 0.07

total = 0.0   # global
tax = 0.0     # global

def compute_total_and_tax(quantity, unit_price):
    global total, tax
    total = quantity * unit_price
    tax = total * TAX_RATE

quantity = int(input("Enter quantity: "))
unit_price = float(input("Enter unit price: "))

compute_total_and_tax(quantity, unit_price)

print("Total: $", format(total, ",.2f"), sep="")
print("Tax:   $", format(tax, ",.2f"), sep="")