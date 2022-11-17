import copy

import Avtale
import datetime
import jsonpickle

from Main import Sted_Manager, Kategori

alle_avtaler = []


# Input i tilfellet noen vil printe en spesifik liste istedet for den globale lista
def print_avtale_liste(Overskrift=None, liste_inn=None):
    if liste_inn is None:
        liste_inn = alle_avtaler

    if Overskrift is not None:
        print(Overskrift)

    for i in range(len(liste_inn)):
        print(f"[{i}] {liste_inn[i]}")


def sjekk_dato(dato: datetime):
    sortert_avtaler = []
    for avtale in alle_avtaler:
        if avtale.starttidspunkt == dato:
            sortert_avtaler.append(avtale)
    return sortert_avtaler


def avtale_streng(tittel: str):
    tittel_avtaler = []
    for avtale in alle_avtaler:
        if avtale.tittel.find(tittel) != -1:
            tittel_avtaler.append(avtale)
    return tittel_avtaler


def slett_avtale():
    print_avtale_liste()
    del alle_avtaler[int(input("Skriv inn Indexen til avtalen du har lyst til å slette: "))]
    
    
def rediger_avtaler():
    print_avtale_liste()
    index = int(input("Skriv inn Indexen på avtalen du har lyst å endre på: "))
    avtale = alle_avtaler.pop(index)
    print(avtale)
    ny_avtale()
    

def ny_avtale():
    tittel = input("tittel: ")

    # print liste av steder og få index
    Sted_Manager.print_alle_steder()

    # vil brukeren lage et nytt sted?
    index = int(input("sted: "))
    if index >= len(Sted_Manager.alle_steder):
        sted = Sted_Manager.lag_nytt_sted()
    else:
        sted = Sted_Manager.alle_steder[index]

    try:
        starttidspunkt = datetime.datetime(int(input("År: ")), int(input("Måned: ")), int(input("Dag: ")),  int(input("Time: ")))
    except:
        print("Feil tidspunkt. Prøv på ny")
        ny_avtale()

    varighet = int(input("hvor lenge den varer: "))
    avtale = Avtale.Avtale(tittel, sted, starttidspunkt, varighet)
    alle_avtaler.append(avtale)
    return avtale

def print_samme_lokasjon():
    spesifike_avtaler = []

    # Sted_Manager.print_alle_steder()
    Sted_Manager.print_alle_steder()

    index = int(input("Hvilket sted vil du se?: "))
    valgtSted = Sted_Manager.alle_steder[index]

    for avtale in alle_avtaler:
        if avtale.sted.navn == valgtSted.navn:
            spesifike_avtaler.append(avtale)

    print_avtale_liste(None, spesifike_avtaler)


def legg_til_kategori(avtale, kategori: Kategori.Kategori):
    avtale.kategori.append(kategori)


def skriv_avataler():
    fil = open("text.json", "w", encoding='utf-8')
    jsonstr = jsonpickle.encode(alle_avtaler)
    fil.writelines(jsonstr)
    fil.close()


def les_avataler():
    fil = open("text.json", "r", encoding='utf-8')
    decoded = jsonpickle.decode(fil.read())
    alle_avtaler.clear()
    alle_avtaler.extend(decoded)
    fil.close()
