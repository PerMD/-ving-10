import Kategori

alle_kategorier = []


def lag_ny_kategori():
    ide = int(input("id: ")) 
    navn = input("navn: ")
    prioritet = int(input("prioritet: "))
    ny_kategori = Kategori.Kategori(ide, navn, prioritet)
    alle_kategorier.append(ny_kategori)
    return alle_kategorier


def print_alle_kategorier(liste_inn=None):
    if liste_inn is None:
        liste_inn = alle_kategorier

    for i in range(len(liste_inn)):
        print(f"[{i}] {liste_inn[i]}")
