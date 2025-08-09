CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_str = input("Enter the temperature to convert: ").strip()
        if not temp_str.replace('.', '', 1).lstrip('-').isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        temp = float(temp_str)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is equal to {result:.2f}°F")
        elif unit == 'F':
            result = convert_to_celsius(temp)
            print(f"{temp}°F is equal to {result:.2f}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()

