
def km_to_miles (km):
    return km * 0.621371

def celsius_to_fahrenheit (c):
    return (c * 9/5) + 32

def kg_to_grams (kg):
    return kg * 1000

print ("Unit Converter")
print (" 1. Kilometres to Miles")
print (" 2. Celsius to Fahrenheit")
print (" 3. Kilograms to grams")

choice = int (input ("Enter your choice (1-3): "))
Value = float (input ("Enter the value: "))

if choice == 1:
    print ("Result:", km_to_miles (Value), "miles")
elif choice == 2:
    print ("Result:", celsius_to_fahrenheit (Value))
elif choice == 3:
    print ("Result:", kg_to_grams (Value), "grams")
else:
    print (" Invalid Choice!")


# Unit Converter using modules & Functions
