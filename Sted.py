class Sted:
    ide = 0
    navn = ""
    gateadresse = ""
    postnummer = 0
    poststed = ""

    def __init__(self, ide: int, navn: str, gateadresse: str, postnummer: int, poststed: str):
        self.ide = ide
        self.navn = navn
        self.gateadresse = gateadresse
        self.postnummer = postnummer
        self.poststed = poststed

    def __str__(self):
        return f"ID: {self.ide} | Navn: {self.navn} | Adresse: {self.gateadresse}_{self.postnummer}_{self.poststed}"

    def get_adresse_streng(self):
        return f"{self.gateadresse}_{self.postnummer}_{self.poststed}"
