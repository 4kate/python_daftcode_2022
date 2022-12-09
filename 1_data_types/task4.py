def simple_conditional(a: int):
    # Uzupełnij poniższe wyrażenie warunkowe tak, aby zmienna `result` przyjmowała
    # wartość `True` tylko wtedy gdy zmienna `a` ma wartość większą niż 10

    result: bool = False

    if a > 10:
        result = True

    return result


def zero_comparision(a: int):
    # Uzupełnij poniższe wyrażenie warunkowe tak, aby zmienna result miała wartość
    # 1 gdy zmienna `a` jest większa od 0, -1 gdy mniejsza od 0 i 0 gdy ma wartość 0

    if a > 0:
        result = 1
    elif a < 0:
        result = -1
    else:
        result = 0

    return result


def list_searching(a: int, b: list):
    # Uzupełnij poniższe wyrażenie warunkowe tak, aby zmienna `result` miała wartość
    # `True` tylko wtedy, gdy wartość zapisana w zmiennej `a` znajduje się w liście
    # `b`
    result: bool = False

    if a in b:
        result = True

    return result


def roman_numerals(a: int):
    # Napisz instrukcję warunkową, która dla liczb z przedziału 1 - 10 przypisze do zmiennej `result`
    # jej odpowiednik w notacji rzymskiej np. 3 -> "III". Jeśli liczba będzie spoza tego przedziału
    # przypisz do zmiennej `result` pustego stringa ("")
    result: str = ""

    # Tutaj wpisz odpowiednie wyrażenie warunkowe
    if a == 1:
            result: str = "I"
                
    elif a == 2:
            result: str = "II"

    elif a == 3:
            result: str = "III"
                
    elif a == 4:
            result: str = "IV"
        
    elif a == 5:
            result: str = "V"
                
    elif a == 6:
            result: str = "VI"

    elif a == 7:
            result: str = "VII"
                
    elif a == 8:
            result: str = "VIII"
        
    elif a == 9:
            result: str = "IX"
                
    elif a == 10:
            result: str = "X"
                
    return result
