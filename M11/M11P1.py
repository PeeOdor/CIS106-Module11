# Module 11 Problem 1 - Discount using a function that returns two values

def compute_discount(quantity, price, discount_rate):
    discount_amount = quantity * price * discount_rate
    discounted_price = quantity * price - discount_amount
    return discount_amount, discounted_price

quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))
discount_rate = float(input("Enter discount rate (e.g. 0.10 for 10%): "))

discount_amount, discounted_price = compute_discount(quantity, price, discount_rate)

print("Quantity:         ", quantity)
print("Price:            $", format(price, ",.2f"), sep="")
print("Discount amount:  $", format(discount_amount, ",.2f"), sep="")
print("Discounted price: $", format(discounted_price, ",.2f"), sep="")