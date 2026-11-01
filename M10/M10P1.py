# Piotr Olechno
# Module 10 - Problem 1: Next month's sales forecast

def compute_forecast(month, sales):
    month = month.strip().lower()[:3]
    if month in ("jan", "feb", "mar"):
        forecast_percent = 0.10
    elif month in ("apr", "may", "jun"):
        forecast_percent = 0.15
    elif month in ("jul", "aug", "sep"):
        forecast_percent = 0.20
    else:   # oct, nov, dec
        forecast_percent = 0.25
    next_month_sales = sales * (1 + forecast_percent)
    return next_month_sales

response = input("Do you want to run the program? (Yes or No): ")
while response.lower() == "yes":
    last_name = input("Enter last name: ")
    month = input("Enter month (e.g. Jan): ")
    sales = float(input("Enter sales: "))

    next_sales = compute_forecast(month, sales)
    print(f"{last_name}, next month's forecasted sales: ${next_sales:,.2f}")

    response = input("Do you want to run the program again? (Yes or No): ")