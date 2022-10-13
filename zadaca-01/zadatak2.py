def funkcija(lista, dic):
    assert (
        isinstance(lista, list)
        and isinstance(dic, dict)
        and len(lista) == len(dic)
        and all(isinstance(x, int) for x in lista)
    )
    # return {k: v if 5 <= v <= 10 else -1 for k, v in enumerate(lista)}
    return {k: v if 5 <= v <= 10 else -1 for (k, v) in zip(dic.keys(), lista)}


print(funkcija([8, 7, 1], {1: 2, 2: 1, 3: 2}))  # > {1: 8, 2: 7, 3: -1}
