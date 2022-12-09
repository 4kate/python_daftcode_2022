# Uzupełnij funkcję `multi_adders` tak, aby przyjmowała jeden argument
# pozycyjny i zwracała listę funkcji. W zwracanej liście powinno
# znaleźć się n funkcji. Funkcje w zwracanej liście powinny przyjmować
# jeden argument i zwracać sumę otrzymanego argumentu oraz
# swojej pozycji w liście.
#
# Przykład:
# functions_list = multi_adders(5)
# functions_list[1](10) == 11
# functions_list[4](10) == 14
# len(functions_list) == 5


def multi_adders(a):
    my_list = []
    for i in range(a):
        my_list.append(lambda b, c=i: b+c)

    return my_list
