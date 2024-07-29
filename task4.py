def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

temp = float(input("Enter the temperature: "))
choice = input("Convert to (F)ahrenheit or (C)elsius? ").upper()

if choice == 'F':
    print(f"{temp} Celsius is {celsius_to_fahrenheit(temp)} Fahrenheit")
elif choice == 'C':
    print(f"{temp} Fahrenheit is {fahrenheit_to_celsius(temp)} Celsius")
else:
    print("Invalid choice")
