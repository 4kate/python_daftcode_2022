# Uzupełnij funkcje `memorizer` i `caller`.
#
# Funkcja `memorizer` jako argument otrzyma listę funkcji.
#
# Funkcja `caller` jako argument otrzyma listę tych samych funkcji
# jak `memorize` w losowej kolejności. Zadaniem `caller` jest
# wywołanie ich w takiej kolejności w jakiej zostały przekazane
# do `memorizer`.
#
# Funkcje `memorizer` i `caller` zostaną wykorzystane w przybliżeniu
# w poniższy sposób:
#
# functions_list = [func1, func2, func3]
# memorizer(functions_list)
# shuffle(functions_list)
# caller(funcions_list)
#
# Po wykonaniu powyższych kroków funkcje z `functions_list`
# powinny zostać wywołane w kolejności func1, func2, func3
# przez funkcję `caller`
#
# * Nie używaj zmiennych globalnych
# * Nie korzystaj z importów
# * Rezultat wykonania funkcji `memorizer` i `caller`
#   nie jest wykorzystywany, najlepiej nie korzytać z
#   `return` w ich implementacji


def memorizer(functions: list) -> None:
    pass


def caller(functions: list) -> None:
    functions.sort(key=id)
    for i in functions:
        i()
