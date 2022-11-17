class Kategori:
    navn = ""
    prioritet = 1
    
    def __init__(self, ide: int, navn: str, prioritet: int):
        self.ide = ide
        self.navn = navn
        self.prioritet = prioritet


    def __str__(self):
        return f"ID: {self.ide} | Navn: {self.navn} | Prioritet: {self.prioritet}"
              
