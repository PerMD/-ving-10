from datetime import datetime

from Main import Kategori
import Sted


class Avtale:
    def __init__(self, tittel: str, sted: Sted.Sted, starttidspunk: datetime, varighet: int):
        self.tittel = tittel
        self.sted = sted
        self.starttidspunkt = starttidspunk
        self.varighet = varighet
        self.kategori = []

    def __str__(self):
        outstr = f"Tittel: {self.tittel} | Lokasjon: {self.sted.get_adresse_streng()} " \
               f"| Start tid: {self.starttidspunkt.time()} | Varighet: {self.varighet} minutter"

        if len(self.kategori) != 0:
            katstr = self.kategori[0].navn
            for kat in self.kategori[1:]:
                katstr += ", " + kat.navn
            outstr += f" | Kategorier: {katstr}"

        return outstr
