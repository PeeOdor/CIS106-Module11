# Module 11 Problem 3 - Sales report: commission and next year's target

def compute_commission(sales):
    if sales > 100000:
        commission = sales * 0.10
    else:
        commission = sales * 0.05
    target = sales * 0.05
    return commission, target

last_name = input("Enter salesperson's last name: ")
sales = float(input("Enter sales: "))

commission, target = compute_commission(sales)

print("Salesperson:        ", last_name)
print("Commission:         $", format(commission, ",.2f"), sep="")
print("Next year's target: $", format(target, ",.2f"), sep="")