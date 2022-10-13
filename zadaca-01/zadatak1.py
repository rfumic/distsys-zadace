def funkcija(lista):
    assert all(isinstance(x, str) for x in lista)
    return [x for x in lista if len(x) > 4]

#print(funkcija(['Pas','Macka','Stol'])) # > ['Macka']
#print(funkcija([[1,2,3,3,4],'Macka','Stol'])) # > Error