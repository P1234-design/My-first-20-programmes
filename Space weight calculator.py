print("INTERGALACTIC WEIGHT CALCULATOR")

try:
    earth_weight = float(input("Write your weight on Earth (in kg): "))
except ValueError:
    print("ERROR! Please enter a valid number.")
    raise SystemExit

planets = {
    "1": ("Moon", 0.165),
    "2": ("Mars", 0.377),
    "3": ("Jupiter", 2.34),
    "4": ("Black Hole", None)
}

while True:
    choice = input("Where do you want to go? (1 = Moon, 2 = Mars, 3 = Jupiter, 4 = Black Hole): ").strip()

    if choice not in planets:
        print("Please choose only from the given options: 1, 2, 3, or 4.")
        continue

    if choice == "4":
        print("In a Black Hole, gravity is infinite, so your weight is effectively infinite. You are spaghettified!")
        break

    planet, gravity = planets[choice]
    weight = earth_weight * gravity
    print(f"On {planet}, your weight is: {weight:.3f} kg")
    break
