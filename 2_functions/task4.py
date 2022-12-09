# Uzupełnij funkcję `adder` tak, aby przyjmowała jeden argument
# pozycyjny i zwracała funkcję. Zwrócona funkcja powinna przyjmować
# jeden argument pozycyjny i zwracać sumę otrzymanego argumentu i
# argumentu przekazanego wcześniej do funkcji adder
#
# Przykład:
# adder(1)(2) == 3


def adder(a):
    def adder2(b):
        return a+b
    return adder2
