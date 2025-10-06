input = float(input("Enter temperature in Celsius: "))
temp_in_fahrenheit = (input * 1.80) + 32.00
temp_in_Kelvin = input + 273.15
output = [temp_in_fahrenheit, temp_in_Kelvin]
print(f"Temperature at {input}°C is {output[0]}°F and {output[1]}K")
