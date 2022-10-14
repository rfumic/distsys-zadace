def funkcija(prvi, drugi):
    assert (
        type(prvi) == type(drugi) and isinstance(prvi, dict) or isinstance(prvi, list)
    )
    return prvi + drugi if isinstance(prvi, list) else prvi | drugi


print(funkcija([1, 2, 1, 2], [3, 2]))  # > [1,2,1,2,3,2]
print(funkcija({1: 2, 3: 2}, {5: 2, 4: 1}))  # > {1: 2, 3: 2, 5: 2, 4: 1}
