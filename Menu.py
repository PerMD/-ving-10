import Avtale_Manager
import Sted_Manager
import kategori_Manager


def menu():
    while True:
        print("[1] Option 1: Lese inn avtaler fra fil")
        print("[2] Option 2: Skriv avtalene for fil")
        print("[3] Option 3: Skriv inn en ny avtale")
        print("[4] Option 4: Skriv ut alle avtalene")
        print("[5] Option 5: Slett en avtale")
        print("[6] Option 6: Rediger en avtale")
        print("[7] Option 7: Skriv inn ny kategori")
        print("[8] Option 8: Skriv inn nytt sted")
        print("[9] Option 9: Finn avtale på bestemt sted")
        print("[10] Option 10: legg til kategori til avtale")
        print("[0] Avslutt")

        valg = int(input("Skriv inn ditt valg: "))

        if valg == 1:
            # Lese inn avtaler fra fil
            print("Valg 1 har blitt valgt")
            Avtale_Manager.les_avataler()
            Avtale_Manager.print_avtale_liste()

        elif valg == 2:
            # Skriv avtalene til en fil
            print("Valg 2 har blitt valgt")
            Avtale_Manager.skriv_avataler()

        elif valg == 3:
            # Skriv inn en ny avtale
            print("Valg 3 har blitt valgt")
            Avtale_Manager.ny_avtale()

        elif valg == 4:
            # Skriv ut alle avtalene
            print("Valg 4 har blitt valgt")
            Avtale_Manager.print_avtale_liste()

        elif valg == 5:
            # Slett en avtale
            print("Valg 5 har blitt valgt")
            Avtale_Manager.slett_avtale()

        elif valg == 6:
            # Rediger en avtale
            print("Valg 6 har blitt valgt")
            Avtale_Manager.rediger_avtaler()

        elif valg == 7:
            # Skriv inn ny kategori
            print("Valg 7 har blitt valgt")
            kategori_Manager.lag_ny_kategori()

        elif valg == 8:
            # Skriv inn nytt sted
            print("Valg 8 har blitt valgt")
            Sted_Manager.lag_nytt_sted()

        elif valg == 9:
            # Finn avtale på bestemt sted
            print("Valg 9 har blitt valgt")
            Avtale_Manager.print_samme_lokasjon()

        elif valg == 10:
            # Legg til kategori til avtale
            print("valg 10 har blitt valgt")

            Avtale_Manager.print_avtale_liste()
            index = int(input("Hvilken avtale vil du gi en kategori?: "))
            avtale = Avtale_Manager.alle_avtaler[index]

            print("")

            kategori_Manager.print_alle_kategorier()
            index1 = int(input("Hvilken kategori?: "))
            kategori = kategori_Manager.alle_kategorier[index1]

            Avtale_Manager.legg_til_kategori(avtale, kategori)

        else:
            break

        print()
