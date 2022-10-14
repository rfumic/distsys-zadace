def funkcija(l1, l2):
    assert len(l1) == len(l2)
    return [x if x == y else -1 for x, y in zip(l1, l2)]


print(funkcija([1, 2, 3, 4, 5], [2, 2, 4, 4, 5]))  # > [-1, 2, -1, 4, 5]
