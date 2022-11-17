import datetime
from unittest import TestCase
import Avtale
import Avtale_Manager
import Menu
import Sted
from Main import Sted_Manager


class Test(TestCase):
    def test_avtale_klasse(self):
        sted = Sted.Sted(0, "Sandnes", "Skogvokterveien", 4325, "Sandnes")
        Sted_Manager.alle_steder.append(sted)
        avtale = Avtale.Avtale("Avtale", sted, datetime.datetime(2022, 10, 25), 100)
        print(avtale)

    def test_sjekk_dato(self):
        sted = Sted.Sted(0, "Sandnes", "Skogvokterveien", 4325, "Sandnes")
        sted2 = Sted.Sted(1, "Stavanger", "Stavangerveien", 4029, "Stavanger")
        Sted_Manager.alle_steder.append(sted)
        Sted_Manager.alle_steder.append(sted2)
        avtale = Avtale.Avtale("Avtale", sted, datetime.datetime(2022, 10, 25), 100)
        avtale1 = Avtale.Avtale("Avtale1", sted2, datetime.datetime(2022, 9, 25), 100)
        Avtale_Manager.alle_avtaler.append(avtale)
        Avtale_Manager.alle_avtaler.append(avtale1)

        output = Avtale_Manager.sjekk_dato(datetime.datetime(2022, 10, 25))
        print(output[0].starttidspunkt)
        
    def test_avtale_streng(self):
        sted = Sted.Sted(0, "Sandnes", "Skogvokterveien", 4325, "Sandnes")
        Sted_Manager.alle_steder.append(sted)
        avtale = Avtale.Avtale("korrektdawdd", sted, datetime.datetime(2022, 10, 25), 100)
        avtale1 = Avtale.Avtale("feil", sted, datetime.datetime(2022, 9, 25), 100)
        Avtale_Manager.alle_avtaler.append(avtale)
        Avtale_Manager.alle_avtaler.append(avtale1)

        output = Avtale_Manager.avtale_streng("korrekt")
        print(output[0].tittel)

    def test_meny(self):
        sted = Sted.Sted(0, "Sandnes", "Skogvokterveien", 4325, "Sandnes")
        sted1 = Sted.Sted(1, "Sandnes", "Skogvokterveien", 4325, "Sandnes")
        sted2 = Sted.Sted(1, "Stavanger", "Stavanger", 4020, "Stavanger")
        Sted_Manager.alle_steder.append(sted)
        Sted_Manager.alle_steder.append(sted1)
        Sted_Manager.alle_steder.append(sted2)


        avtale = Avtale.Avtale("Avtale", sted, datetime.datetime(2022, 10, 25), 100)
        avtale1 = Avtale.Avtale("Avtale1", sted1, datetime.datetime(2022, 9, 25), 100)
        avtale2 = Avtale.Avtale("Avtale1", sted2, datetime.datetime(2022, 9, 25), 100)

        Avtale_Manager.alle_avtaler.append(avtale)
        Avtale_Manager.alle_avtaler.append(avtale1)
        Avtale_Manager.alle_avtaler.append(avtale2)

        Menu.menu()

    def test_fil_skriving_og_lesing(self):
        sted = Sted.Sted(0, "Sandnes", "Skogvokterveien", 4325, "Sandnes")
        avtale = Avtale.Avtale("Avtale", sted, datetime.datetime(2022, 10, 25, 12, 45), 100)
        Avtale_Manager.alle_avtaler.append(avtale)
        Avtale_Manager.skriv_avataler()
        Avtale_Manager.les_avataler()

    def test_ny_avtale(self):
        avtale = Avtale_Manager.ny_avtale()
        print(avtale)
