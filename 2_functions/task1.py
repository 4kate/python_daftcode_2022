# Uzupelnij deklarację funkcji `simple_adder` tak, aby
# przyjomowała dwa argumenty i zwracała ich sumę.


def simple_adder(a,b):
    return a + b


# Uzupełnij deklarację funkcji `simple_subtractor` tak,
# aby przymowała dwa `keyword arguments` o nazwach `x` i `y`
# i zwracała ich różnicę. Niech `x` będzie odjemną.


def simple_subtractor(x,y):
    return x - y


# Uzupełnij deklarację funkcji `simple_calculator` tak,
# aby przyjmowała dwa argumenty pozycyjne i jeden `keyword`.
# Dwa argumenty pozycyjne mają być operandami operacji zdefiniowanej
# jako `keyword` `operation`. Jeśli `operation` nie zostanie
# przekazane jako parametr wywołania, funkcja powinna wykonać
# operację dodawania. `operation` może być jednym z '+', '-', '*',
# '**', '|' lub '&'.
#
# Przykład 1:
# simple_calculator(1, 2) == 3
#
# Przykład 2:
# simple_calculator(2, 1, operation='-') == 1


def simple_calculator(a, b, operation='+'):
    if operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '**':
        return a ** b
    elif operation == '|':
        return a | b
    elif operation == '&':
        return a & b
    else:
        return a + b
