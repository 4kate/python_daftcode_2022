def subsets_everywhere(elements: set):
    # Napisz program tworzący ze zbioru `elements` zbiór zawierający wszystkie
    # podzbiory `elements` (włącznie z pustym i `elements`).
    # UWAGA: w python zbiory (set) nie mogą być elementami innych zbiorów,
    # proszę użyć `frozenset` jako zbiorów wewnętrznych.
    # Wynik przypisz do zmienej `result`
    x = len(elements)
    s = list(elements)
    result: set = set()
    for i in range(1 << x):
        a = {s[j] for j in range(x) if (i & (1 << j))}
        result.add(frozenset(a))
    
    return result
