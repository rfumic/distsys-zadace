def funkcija(lista):
    return sorted([{"id": ID, "ime": ime, "prezime": prezime} for ID, ime, prezime in lista if ime[0] == prezime[0]],key=lambda i: i["id"])


print(funkcija([(121, "Ivan", "Ivic"), (431, "Pero", "Horvat"), (31, "Marija", "Maric")]))
# > [{‘id’: 31, ‘ime’: ‘Marija’, ‘prezime’: ‘Maric’}, {‘id’: 121, ‘ime’:‘Ivan’, ‘prezime’: ‘Ivic’}]
