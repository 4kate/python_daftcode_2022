# Uzupełnij deklarację funkcji `multi_calculator` tak,
# aby funkcja działała analogicznie do funkcji `simple_calculator`,
# z tą różnicą, że obsługuje więcej niż dwa argumenty pozycyjne.
#
# * Jeśli funkcja nie otrzyma żadnych argumentów powinna
#   zwrócić `0` niezależnie od `operation`
# * Jeśli funckja otrzyma jeden argument pozycyjny powinna
#   zwrócić jego wartość niezależnie od `operation`
# * Domyślną operacją jest dodawanie
#
# Przykład 1:
# multi_calculator(1, 1, 1, 1, 1, 1) == 6
#
# Przykład 2:
# multi_calculator(10, 1, 1, operation='-') == 8
#
# Przykład 3:
# multi_calculator(operation='|') == 0
#
# Przykład 4:
# multi_calculator(3) == 3


def multi_calculator(a:int=None, b:int=None, *args, operation:str='+'):
    if a is None and b is None and len(args)==0:
        result = 0
    elif a is not None and b is None:
        result = a
    elif a is None and b is not None:
        result = b
    elif operation == '-':
        result = a - b - sum(args)
    elif operation == '*':
        result = a * b
        for arg in args:
            result = result * arg
    elif operation == '**':
        result = a ** b
        for arg in args:
            result = result ** arg
    elif operation == '|':
        result = a | b
        for arg in args:
            result = result | arg
    elif operation == '&':
        result = a & b
        for arg in args:
            result = result & arg
    else:
        result=  a + b + sum(args)

    return result
