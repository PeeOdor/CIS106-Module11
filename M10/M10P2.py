# Piotr Olechno
# Module 10 - Problem 2: Gallons of paint for a room (with bonus)

def compute_wall_sqft(length, width, height):
    return 2 * length * height + 2 * width * height

# Bonus a: area of ceiling or floor
def compute_ceiling_area(length, width):
    return length * width

response = input("Do you want to run the program? (Yes or No): ")
while response.lower() == "yes":
    length = float(input("Enter room length (ft): "))
    width = float(input("Enter room width (ft): "))
    height = float(input("Enter room height (ft): "))

    wall_sqft = compute_wall_sqft(length, width, height)
    wall_gallons = wall_sqft / 50
    print(f"Wall square footage: {wall_sqft:,.2f}")
    print(f"Gallons of wall paint needed: {wall_gallons:,.2f}")

    # Bonus b-d
    ceiling_area = compute_ceiling_area(length, width)
    ceiling_gallons = ceiling_area / 50
    print(f"Ceiling/floor area: {ceiling_area:,.2f}")
    print(f"Gallons of ceiling paint or floor varnish needed: {ceiling_gallons:,.2f}")

    response = input("Do you want to run the program again? (Yes or No): ")