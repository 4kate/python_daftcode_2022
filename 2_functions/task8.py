# Ulepsz kalkulator z `task6` tak aby był w stanie
# wykonać działanie dowolnej długości.
#
# Przykład:
# calculator(1)('+')(4)('-')(2)('=') == 3
#
# * Kalkulator musi wspierać działania dodawania
#   i odejmowania
# * Każde działanie kończy się znakiem '='
# * Nie korzystaj ze zmiennych globalnych i importów
#
# Powodzenia!


def calculator(a):
        def simple_functional_calc_b(b):
                if b != '=':
                    def simple_functional_calc_c(c):
                        if b == '+':
                            result = (a + c)
                        elif b == '-':
                            result = (a - c)
                        return calculator(result)
                    return simple_functional_calc_c
                else:
                    result = a
                    return result
        return simple_functional_calc_b

## second version
'''class calculator:
    def __init__(self, value, operator=''):
        self.value = value
        self.operator = operator

    def __call__(self, value):
        if value == '=': return self.value 
        elif value == '+': return calculator(self.value, operator='+')
        elif value == '-': return calculator(self.value, operator='-')
        else:
            if self.operator == '+': 
                return calculator(self.value + value, operator='')
            elif self.operator == '-': 
                return calculator(self.value - value, operator='')'''
