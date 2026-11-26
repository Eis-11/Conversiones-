def celsius_a_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_a_celsius(f):
    return (f - 32) * 5 / 9


def km_a_millas(km):
    return km * 0.621371


def millas_a_km(millas):
    return millas / 0.621371


def kg_a_libras(kg):
    return kg * 2.20462


if __name__ == "__main__":
    print("25 °C =", celsius_a_fahrenheit(25), "°F")
    print("10 km =", km_a_millas(10), "millas")