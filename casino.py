class Speler:
    def __init__(self, spel, teruggaan, c_redits = 500, naam=None):
        self.c_redits = c_redits
        self.spel = spel
        self.teruggaan = teruggaan
        self.naam = naam
    def save_name(self):
        print('wat is uw naam?')
        self.naam = input('uw naam: ')
        document = open('names.txt', 'a')
        document.write(' \n')
        document.write(self.naam)
        document.close()
    def hub(self):
        print("credits", self.c_redits)
        self.teruggaan = "nee"
        self.spel=0
        print("Welke game wil je spelen?")
        print("----------------------------------------")
        print("1: Slotmachine")
        print("2: Hoger Lager")
        print("3: Paardenrace")
        print("4: Roulette")
        print("5: Black Jack")
        print("----------------------------------------")
        self.spel=(int(input("input: ")))
        if self.spel == 1:
            self.slotmachine()
        elif self.spel==2:
            self.hogerlager()
        elif self.spel==3:
            self.paardenrace()
        elif self.spel==4:
            self.roulette()
        elif self.spel==5:
            self.black_jack()
    def slotmachine(self):
        #jouw code
        self.teruggaan = (input("wil je verder spelen? "))
        if self.teruggaan == "N":
            self.hub()
        elif self.teruggaan == "Y":
            self.slotmachine()
    def hogerlager(self, player):
        #jouw code
        HogerLager.start_game(self, player)
        self.teruggaan = (input("wil je verder spelen? "))
        if self.teruggaan == "N":
            self.hub()
        elif self.teruggaan == "Y":
            self.hogerlager()
    def paardenrace(self):
        #jouw code
        self.teruggaan = (input("wil je verder spelen? "))
        if self.teruggaan == "N":
            self.hub()
        elif self.teruggaan == "Y":
            self.paardenrace()
    def roulette(self):
        #jouw code
        import random
        # klasse roulette aanmaken en beschrijven
        class Roulette:
            def __init__(self, getal, kleur, kolom):
                self.getal = getal
                self.kleur = kleur
                self.kolom = kolom

            def the_roullete(self):
                self.getal = random.randint(1, 36)
            def check_forwin(self):
                for aantal_duur in range(12):
                    if gekozen_getallen[aantal_duur] == self.getal:
                        print('Je hebt gewonnen.')
                else:
                    print('Je bent verloren.')

        # subklassen maken en beschrijven
        class Gamekolom1(Roulette):
            def __init__(self, getal, kleur='rood', kolom=1):
                super().__init__(getal, kleur, kolom)

            def printinfo(self):
                print(self.getal)
                print(self.kleur)

        class Gamekolom2(Roulette):
            def __init__(self, getal, kleur='rood', kolom=2):
                super().__init__(getal, kleur, kolom)

        class Gamekolom3(Roulette):
            def __init__(self, getal, kleur='rood', kolom=3):
                super().__init__(getal, kleur, kolom)

        # instanties maken
        # onderaan de foto
        getal1_kolom1 = Gamekolom1(getal=1)
        getal2_kolom1 = Gamekolom1(getal=4, kleur='zwart')
        getal3_kolom1 = Gamekolom1(getal=7)
        getal4_kolom1 = Gamekolom1(getal=10, kleur='zwart')
        getal5_kolom1 = Gamekolom1(getal=13, kleur='zwart')
        getal6_kolom1 = Gamekolom1(getal=16)
        getal7_kolom1 = Gamekolom1(getal=19)
        getal8_kolom1 = Gamekolom1(getal=22, kleur='zwart')
        getal9_kolom1 = Gamekolom1(getal=25)
        getal10_kolom1 = Gamekolom1(getal=28, kleur='zwart')
        getal11_kolom1 = Gamekolom1(getal=31, kleur='zwart')
        getal12_kolom1 = Gamekolom1(getal=34)

        # middelste balk foto
        getal1_kolom2 = Gamekolom1(getal=2)
        getal2_kolom2 = Gamekolom1(getal=5, kleur='zwart')
        getal3_kolom2 = Gamekolom1(getal=8)
        getal4_kolom2 = Gamekolom1(getal=11, kleur='zwart')
        getal5_kolom2 = Gamekolom1(getal=14)
        getal6_kolom2 = Gamekolom1(getal=17, kleur='zwart')
        getal7_kolom2 = Gamekolom1(getal=20, kleur='zwart')
        getal8_kolom2 = Gamekolom1(getal=23)
        getal9_kolom2 = Gamekolom1(getal=26, kleur='zwart')
        getal10_kolom2 = Gamekolom1(getal=29, kleur='zwart')
        getal11_kolom2 = Gamekolom1(getal=32)
        getal12_kolom2 = Gamekolom1(getal=35, kleur='zwart')

        # bovenste kolom foto
        getal1_kolom3 = Gamekolom1(getal=3)
        getal2_kolom3 = Gamekolom1(getal=6, kleur='zwart')
        getal3_kolom3 = Gamekolom1(getal=9)
        getal4_kolom3 = Gamekolom1(getal=12)
        getal5_kolom3 = Gamekolom1(getal=15, kleur='zwart')
        getal6_kolom3 = Gamekolom1(getal=18)
        getal7_kolom3 = Gamekolom1(getal=21)
        getal8_kolom3 = Gamekolom1(getal=24, kleur='zwart')
        getal9_kolom3 = Gamekolom1(getal=27)
        getal10_kolom3 = Gamekolom1(getal=30)
        getal11_kolom3 = Gamekolom1(getal=33, kleur='zwart')
        getal12_kolom3 = Gamekolom1(getal=36)

        roullete = Roulette(0, None, None)
        # begin met het spel
        print('Hoeveel credits wil je inzetten?')
        print('Je kan kiezen: 1, 2, 3, 12, even of oneven.')
        aantal_credits = input('1, 2, 3, 12 of even of oneven: ')
        roullete.the_roullete()
        print("Het balletje valt op:", roullete.getal)
        if aantal_credits == '1':
            print('Goed, welk getal wil je?')
            print('Je kan de getallen 0-36 kiezen.')
            gekozen_getallen = input('getal tussen 0 en 36: ')
        if aantal_credits == '2':
            print('Goed, welke getallen wil je?')
            print('Je kan de getallen 0-36 kiezen.')
            gekozen_getal1 = input('getal 1 tussen 0 en 36: ')
            gekozen_getal2 = input('getal 2 tussen 0 en 36: ')
            gekozen_getallen = [gekozen_getal1, gekozen_getal2]
        if aantal_credits == '3':
            print('Goed, wil je een verticale rij of 3 aparte getallen?')
            antwoord = input('rij of getal: ')
            if antwoord == 'rij':
                print('Oké, welke verticale rij wil je?')
                rij = input('kies en rij van 1-12: ')
                if rij == '1':
                    gekozen_getallen = [getal1_kolom1, getal1_kolom2, getal1_kolom3]
                if rij == '2':
                    gekozen_getallen = [getal2_kolom1, getal2_kolom2, getal2_kolom3]
                if rij == '3':
                    gekozen_getallen = [getal3_kolom1, getal3_kolom2, getal3_kolom3]
                if rij == '4':
                    gekozen_getallen = [getal4_kolom1, getal4_kolom2, getal4_kolom3]
                if rij == '5':
                    gekozen_getallen = [getal5_kolom1, getal5_kolom2, getal5_kolom3]
                if rij == '6':
                    gekozen_getallen = [getal6_kolom1, getal6_kolom2, getal6_kolom3]
                if rij == '7':
                    gekozen_getallen = [getal7_kolom1, getal7_kolom2, getal7_kolom3]
                if rij == '8':
                    gekozen_getallen = [getal8_kolom1, getal8_kolom2, getal8_kolom3]
                if rij == '9':
                    gekozen_getallen = [getal9_kolom1, getal9_kolom2, getal9_kolom3]
                if rij == '10':
                    gekozen_getallen = [getal10_kolom1, getal10_kolom2, getal10_kolom3]
                if rij == '11':
                    gekozen_getallen = [getal11_kolom1, getal11_kolom2, getal11_kolom3]
                if rij == '12':
                    gekozen_getallen = [getal12_kolom1, getal12_kolom2, getal12_kolom3]
            if antwoord == 'getal':
                print('Kies een kolom met het getal erin.')
                gekozen_getallen = [0, getal1_kolom1, getal2_kolom1, getal3_kolom1, getal4_kolom1, getal5_kolom1,
                                    getal6_kolom1, getal7_kolom1, getal8_kolom1, getal9_kolom1, getal10_kolom1,
                                    getal11_kolom1, getal12_kolom1]
                gekozen_getallen.clear()
                for duur in range(3):
                    lijn = input('1, 2, of 3: ')
                    if lijn == '1':
                        print('welk getal wil je als eerste van deze getallen?')
                        getalvraag = input('1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12: ')
                        if getalvraag == '1':
                            gekozen_getallen.append(getal1_kolom1)
                        if getalvraag == '2':
                            gekozen_getallen.append(getal2_kolom1)
                        if getalvraag == '3':
                            gekozen_getallen.append(getal3_kolom1)
                        if getalvraag == '4':
                            gekozen_getallen.append(getal4_kolom1)
                        if getalvraag == '5':
                            gekozen_getallen.append(getal5_kolom1)
                        if getalvraag == '6':
                            gekozen_getallen.append(getal6_kolom1)
                        if getalvraag == '7':
                            gekozen_getallen.append(getal7_kolom1)
                        if getalvraag == '8':
                            gekozen_getallen.append(getal8_kolom1)
                        if getalvraag == '9':
                            gekozen_getallen.append(getal9_kolom1)
                        if getalvraag == '10':
                            gekozen_getallen.append(getal10_kolom1)
                        if getalvraag == '11':
                            gekozen_getallen.append(getal11_kolom1)
                        if getalvraag == '12':
                            gekozen_getallen.append(getal12_kolom1)

                        for getallen_range in range(12):
                            gekozen_getallen[getallen_range].printinfo()
                    if lijn == '1':
                        print('welk getal wil je als eerste van deze getallen?')
                        getalvraag = input('1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12: ')
                        if getalvraag == '1':
                            gekozen_getallen.append(getal1_kolom2)
                        if getalvraag == '2':
                            gekozen_getallen.append(getal2_kolom2)
                        if getalvraag == '3':
                            gekozen_getallen.append(getal3_kolom2)
                        if getalvraag == '4':
                            gekozen_getallen.append(getal4_kolom2)
                        if getalvraag == '5':
                            gekozen_getallen.append(getal5_kolom2)
                        if getalvraag == '6':
                            gekozen_getallen.append(getal6_kolom2)
                        if getalvraag == '7':
                            gekozen_getallen.append(getal7_kolom2)
                        if getalvraag == '8':
                            gekozen_getallen.append(getal8_kolom2)
                        if getalvraag == '9':
                            gekozen_getallen.append(getal9_kolom2)
                        if getalvraag == '10':
                            gekozen_getallen.append(getal10_kolom2)
                        if getalvraag == '11':
                            gekozen_getallen.append(getal11_kolom2)
                        if getalvraag == '12':
                            gekozen_getallen.append(getal12_kolom2)

                    if lijn == '3':
                        print('welk getal wil je als eerste van deze getallen?')
                        getalvraag = input('1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12: ')
                        if getalvraag == '1':
                            gekozen_getallen.append(getal1_kolom3)
                        if getalvraag == '2':
                            gekozen_getallen.append(getal2_kolom3)
                        if getalvraag == '3':
                            gekozen_getallen.append(getal3_kolom3)
                        if getalvraag == '4':
                            gekozen_getallen.append(getal4_kolom3)
                        if getalvraag == '5':
                            gekozen_getallen.append(getal5_kolom3)
                        if getalvraag == '6':
                            gekozen_getallen.append(getal6_kolom3)
                        if getalvraag == '7':
                            gekozen_getallen.append(getal7_kolom3)
                        if getalvraag == '8':
                            gekozen_getallen.append(getal8_kolom3)
                        if getalvraag == '9':
                            gekozen_getallen.append(getal9_kolom3)
                        if getalvraag == '10':
                            gekozen_getallen.append(getal10_kolom3)
                        if getalvraag == '11':
                            gekozen_getallen.append(getal11_kolom3)
                        if getalvraag == '12':
                            gekozen_getallen.append(getal12_kolom3)
                for getallen_range in range(3):
                    gekozen_getallen[getallen_range].printinfo()
        if aantal_credits == '12':
            print('Okidoki, wil je een horizontale lijn van 12 getallen of wil je 12 verschillende getallen?')
            antwoord = input('lijn of getal: ')
            if antwoord == 'lijn':
                print('welke lijn wil je kiezen?')
                lijn = input('1, 2, of 3: ')
                if lijn == '1':
                    gekozen_getallen = [getal1_kolom1, getal2_kolom1, getal3_kolom1, getal4_kolom1, getal5_kolom1, getal6_kolom1, getal7_kolom1, getal8_kolom1, getal9_kolom1, getal10_kolom1, getal11_kolom1, getal12_kolom1]
                    for getallen_range in range(12):
                        gekozen_getallen[getallen_range].printinfo()
                        gekozen_getallen[getallen_range].check_forwin()
                if lijn == '2':
                    gekozen_getallen = Gamekolom2
                    print(gekozen_getallen)
                if lijn == '3':
                    gekozen_getallen = Gamekolom3
                    print(gekozen_getallen)
            if antwoord == 'getal':
                print('Goed, welke getallen wil je?')
                print('Je kan de getallen 0-36 kiezen.')
                gekozen_getal1 = input('getal 1 tussen 0 en 36: ')
                gekozen_getal2 = input('getal 2 tussen 0 en 36: ')
                gekozen_getal3 = input('getal 3 tussen 0 en 36: ')
                gekozen_getal4 = input('getal 4 tussen 0 en 36: ')
                gekozen_getal5 = input('getal 5 tussen 0 en 36: ')
                gekozen_getal6 = input('getal 6 tussen 0 en 36: ')
                gekozen_getal7 = input('getal 7 tussen 0 en 36: ')
                gekozen_getal8 = input('getal 8 tussen 0 en 36: ')
                gekozen_getal9 = input('getal 9 tussen 0 en 36: ')
                gekozen_getal10 = input('getal 10 tussen 0 en 36: ')
                gekozen_getal11 = input('getal 11 tussen 0 en 36: ')
                gekozen_getal12 = input('getal 12 tussen 0 en 36: ')
                gekozen_getallen = [gekozen_getal1, gekozen_getal2, gekozen_getal3, gekozen_getal4, gekozen_getal5, gekozen_getal6, gekozen_getal7, gekozen_getal8, gekozen_getal9, gekozen_getal10, gekozen_getal11, gekozen_getal12]
                for getallen_range in range(12):
                    gekozen_getallen[getallen_range].printinfo()
        if aantal_credits == 'even':
            print('Oké, de gekozen getallen zijn even getallen.')
            gekozen_getallen = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
            for getallen_range in range(12):
                gekozen_getallen[getallen_range].printinfo()
        if aantal_credits == 'oneven':
            print('Oké, de gekozen getallen zijn oneven getallen.')
            gekozen_getallen = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]
            for getallen_range in range(12):
                gekozen_getallen[getallen_range].printinfo()


        self.teruggaan = (input("wil je verder spelen? "))
        if self.teruggaan == "N":
            self.hub()
        elif self.teruggaan == "Y":
            self.roulette()

    def black_jack(self):
        #jouw code
        self.teruggaan = (input("wil je verder spelen? "))
        if self.teruggaan == "N":
            self.hub()
        elif self.teruggaan == "Y":
            self.black_jack()
#eventuele andere klassen
class HogerLager:
    def __init__(self,inzet,kaart,kaart2,keuze):
        self.inzet=inzet
        self.kaart = kaart
        self.kaart2=kaart2
        self.keuze = keuze
    def start_game(self,player):
        self.inzet=int(input("wat is jouw inzet? "))
        player.c_redits -=self.inzet
        self.randomizer()
        self.keuze = input("kies hoger (H) of lager (L). ")
        self.randomizer2()
        if self.keuze == "L":
            if self.kaart2 <= self.kaart:
                player.c_redits += self.inzet * 2
                print("je verdient ", self.inzet, "credits")
        if self.keuze == "H":
            if self.kaart2 >= self.kaart:
                player.c_redits += self.inzet * 2
                print("je verdient ", self.inzet, "credits")
    def randomizer2(self):
        import random
        kaartnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.kaart2 = random.choice(kaartnummers)
        print(self.kaart2)
    def randomizer(self):
        import random
        kaartnummers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.kaart = random.choice(kaartnummers)
        print (self.kaart)


#eventuele instanties
speler1=Speler(0,"N")
HogerLager(0,0,0, None)

#start game
speler1.save_name()
speler1.hub()





