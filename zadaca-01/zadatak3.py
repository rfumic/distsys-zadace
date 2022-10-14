def funkcija(artikli):
    assert (
        isinstance(artikli, list)
        and all(isinstance(x, dict) for x in artikli)
        and all(
            [
                i == {"cijena", "naziv", "kolicina"}
                for i in [set(j.keys()) for j in artikli]
            ]
        )
    )
    return {
        "ukupno": {
            "artikli": [v for d in artikli for k, v in d.items() if k == "naziv"],
            "cijena": sum(d["cijena"] * d["kolicina"] for d in artikli),
        }
    }


print(
    funkcija(
        [
            {"cijena": 8, "naziv": "Kruh", "kolicina": 1},
            {"cijena": 13, "naziv": "Sok", "kolicina": 2},
            {"cijena": 7, "naziv": "Upaljac", "kolicina": 1},
        ]
    )
)  # > {'ukupno': {'artikli': ['Kruh', 'Sok', 'Upaljac'], 'cijena': 41}}
