earth_gravity = 9.8
moon_gravity = 1.6

mass = float(input("Enter the mass of the object (kg): "))

earth_weight = mass * earth_gravity
moon_weight = mass * moon_gravity

print("Weight on Earth =", earth_weight, "N")
print("Weight on Moon =", moon_weight, "N")