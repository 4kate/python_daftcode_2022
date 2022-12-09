def return_int():
    # Przypisz do zmiennej `result` dowolną wartość typu `int`
    result: int = 1
    return result


def return_string():
    # Przypisz do zmiennej `result` wartość typu `string` dłuższą niż 4 znaki
    result: str = 'new string'
    return result


def return_float():
    # Przypisz do zmiennej `result` wartość typu `float` z zakresu (-1, 1)
    result: float = 0.1
    return result


def return_false():
    # Przypisz do zmiennej `result` wartość typu `bool` o wartości fałszu
    result: bool = False
    return result


def convert_to_int(numeric_string: str):
    # Przypisz do zmiennej `result` wartość `numeric_string` przekonwertowaną
    # na typ `int`
    result: int = int(numeric_string)
    return result


def return_complex(real: int):
    # Dodaj do zmiennej `real` dowolną wartość tak, aby powstała liczba urojona
    # Utworzoną liczbę urojoną przypisz do zmiennej `result`
    result: complex = real + 1j
    return result
