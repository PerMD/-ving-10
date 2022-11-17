import Sted
import Avtale_Manager

alle_steder = []


def lag_nytt_sted():
    try:
        ide = int(input("ID: "))
        navn = str(input("Navn: "))
        gateadresse = str(input("Adresse: "))
        postnummer = int(input("Postnummer: "))
        poststed = str(input("Poststed: "))
    except ValueError:
        print("Prøv på ny!")
        lag_nytt_sted()

    nytt_sted = Sted.Sted(ide, navn, gateadresse, postnummer, poststed)
    alle_steder.append(nytt_sted)
    return nytt_sted


def print_alle_steder(liste_inn=None):
    if liste_inn is None:
        liste_inn = alle_steder

    for i in range(len(liste_inn)):
        print(f"[{i}] {liste_inn[i]}")
    print(f"[{len(liste_inn)}] Nytt sted")
