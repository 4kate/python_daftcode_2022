# Uzupełnij funkcję `simple_functional_calc` aby za pomocą
# kolejnych wowołań dało się wykonywać operację dodawania i
# odejmowania. Pierwsze wywołanie będzie zawierało wartość
# pierwszego operandu, drugie wywołanie będzie zawierało
# znak reprezentujący operację a trzecie wywołanie będzie
# zawierało wartość drugiego operandu. Operacją może być
# dodawanie ('+') lub odejmowanie ('-').
#
# Przykład 1:
# simple_functional_calc(1)('+')(1) == 2
#
# Przykład 2:
# simple_functional_calc(1)('-')(1) == 0
#

def simple_functional_calc(a):
    def simple_functional_calc_b(b):
        def simple_functional_calc_c(c):
            if b == '+':
                return (a + c)
            elif b == '-':
                return (a - c)
        return simple_functional_calc_c
    return simple_functional_calc_b
