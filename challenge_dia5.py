def farenheit(temperatura):
    temperatura_f = (temperatura * 9/5) + 32
    return temperatura_f

temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temperatura_fahrenheit = farenheit(temperatura_celsius)

print(f"La temperatura en fahrenheit es: {temperatura_fahrenheit}")