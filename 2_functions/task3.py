# Uzupełnij funkcję `collection_updater` tak, aby przyjmowała
# dowolną ilość argumentów pozycyjnych i jeden opcjonalny `keyword`
# o nazwie `collection`. Funkcja powinna uzupełnić listę przekazaną
# jako `collection` o elementy przekazane jej jako argumenty pozycyjne.
# Jeśli funkcja nie otrzyma `collection`, powinna sama zadbać o stworzenie listy
# i uzupełnienie jej o wartości z argumentów pozycyjnych.
#
# Przykład 1:
# list_updated(1, 2, 3) == [1, 2, 3]
#
# Przykład 2:
# list_updater(1, 2, 3, collection=[5]) == [5, 1, 2, 3]


def list_updater(*args, collection = None):
    collection = collection if collection else []
    for arg in args:
        collection.append(arg)
    return collection
