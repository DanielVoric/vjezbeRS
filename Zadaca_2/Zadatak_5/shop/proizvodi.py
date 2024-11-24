class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        print(f"Proizvod {self.naziv} s cijenom {self.cijena} s dostupnom kolicinom {self.dostupna_kolicina}")
    

Proizvod("Cokolada", 2, 10)
Proizvod("Keksi", 4, 15)
skladiste = [Proizvod("Cokolada", 2, 10), Proizvod("Keksi", 4, 15)]


def dodaj_proizvod(naziv,cijena,dostupna_kolicina):

    noviproizvod = Proizvod(naziv, cijena, dostupna_kolicina)
    skladiste.append(noviproizvod)

