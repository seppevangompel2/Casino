class Speler:
    def __init__(self, spel, teruggaan, c_redits=500, naam=None, inzet=0, kaart=0, kaart2=0, keuze=0):
        self.c_redits = c_redits
        self.spel = spel
        self.teruggaan = teruggaan
        self.naam = naam
        self.inzet = inzet
        self.kaart = kaart
        self.kaart2 = kaart2
        self.keuze = keuze

    def save_name(self):
        while True:
            self.naam = input("Wat is uw naam? ")
            try:
                with open("names.txt", "r") as document:
                    regels = document.readlines()
            except FileNotFoundError:
                regels = []

            bestaande_namen = [regels[i].strip() for i in range(0, len(regels), 2)]

            if self.naam in bestaande_namen:
                print("Deze naam bestaat al, credits worden bijgewerkt.")
                index = bestaande_namen.index(self.naam) * 2 + 1
                regels[index] = str(self.c_redits) + "\n"
                with open("names.txt", "w") as document:
                    document.writelines(regels)
                break
            else:
                with open("names.txt", "a") as document:
                    document.write(self.naam + "\n")
                    document.write(str(self.c_redits) + "\n")
                print('Naam ', self.naam, ' is toegevoegd.')
                break

    def hub(self):
        print(f"\n--- Hub ---")
        print(f"Credits: {self.c_redits}")
        antwoord = input('Wil je je stats opslaan? Y/N: ')
        if antwoord.upper() == 'Y':
            self.save_name()
        print("Welke game wil je spelen?")
        print("----------------------------------------")
        print("1: Slotmachine")
        print("2: Hoger Lager")
        print("3: Paardenrace")
        print("4: Roulette")
        print("5: Black Jack")
        print("----------------------------------------")
        self.spel = int(input("Input: "))
        if self.spel == 1:
            self.slotmachine()
        elif self.spel == 2:
            self.hogerlager()
        elif self.spel == 3:
            self.paardenrace()
        elif self.spel == 4:
            self.roulette()
        elif self.spel == 5:
            self.black_jack()

    # ---------------- Spellen ----------------
    def slotmachine(self):
        print("\n--- Slotmachine ---")
        print(f"Credits: {self.c_redits}")
        self.teruggaan = input("Wil je verder spelen? (Y/N): ")
        if self.teruggaan.upper() == "N":
            self.hub()
        else:
            self.slotmachine()

    def hogerlager(self):
        print("\n--- Hoger/Lager ---")
        print(f"Credits: {self.c_redits}")
        self.inzet = int(input("Wat is jouw inzet? "))
        if self.inzet > self.c_redits:
            print("Niet genoeg credits! Terug naar hub.")
            self.hub()
            return
        self.c_redits -= self.inzet
        self.randomizer()
        self.keuze = input("Kies hoger (H) of lager (L): ").upper()
        self.randomizer2()
        if (self.keuze == "L" and self.kaart2 <= self.kaart) or (self.keuze == "H" and self.kaart2 >= self.kaart):
            winst = self.inzet * 2
            self.c_redits += winst
            print(f"Je wint {winst} credits!")
        else:
            print(f"Je verliest {self.inzet} credits!")
        print(f"Credits nu: {self.c_redits}")
        self.teruggaan = input("Verder spelen? (Y/N): ")
        if self.teruggaan.upper() == "Y":
            self.hogerlager()
        else:
            self.hub()

    def paardenrace(self):
        print("\n--- Paardenrace ---")
        print(f"Credits: {self.c_redits}")
        # Optioneel: inzet toevoegen
        self.teruggaan = input("Wil je verder spelen? (Y/N): ")
        if self.teruggaan.upper() == "Y":
            self.paardenrace()
        else:
            self.hub()

    def roulette(self):
        import random
        print("\n--- Roulette ---")
        print(f"Credits: {self.c_redits}")
        self.inzet = int(input("Wat is je inzet? "))
        if self.inzet > self.c_redits:
            print("Niet genoeg credits! Terug naar hub.")
            self.hub()
            return
        self.c_redits -= self.inzet

        print("Je kan inzetten op: 1=1 getal, 2=2 getallen, 3=3 getallen, 12=dozijn, even, oneven")
        keuze = input("Wat kies je? ").lower()

        if keuze == "1":
            gekozen = [int(input("Welk getal (0-36)? "))]
        elif keuze == "2":
            gekozen = [int(input("Getal 1: ")), int(input("Getal 2: "))]
        elif keuze == "3":
            gekozen = [int(input(f"Getal {i+1}: ")) for i in range(3)]
        elif keuze == "12":
            keuze2 = input("Kies dozijn 1 (1-12), 2 (13-24), 3 (25-36): ")
            if keuze2 == "1":
                gekozen = list(range(1,13))
            elif keuze2 == "2":
                gekozen = list(range(13,25))
            elif keuze2 == "3":
                gekozen = list(range(25,37))
            else:
                print("Ongeldige keuze. Terug naar hub.")
                self.hub()
                return
        elif keuze == "even":
            gekozen = [i for i in range(1,37) if i % 2 == 0]
        elif keuze == "oneven":
            gekozen = [i for i in range(1,37) if i % 2 == 1]
        else:
            print("Ongeldige keuze. Terug naar hub.")
            self.hub()
            return

        resultaat = random.randint(0,36)
        print(f"Het balletje valt op: {resultaat}")
        if resultaat in gekozen:
            winst = self.inzet * 2
            self.c_redits += winst
            print(f"Je hebt gewonnen {winst} credits!")
        else:
            print(f"Je hebt verloren {self.inzet} credits!")

        print(f"Credits nu: {self.c_redits}")
        verder = input("Verder spelen? (Y/N): ")
        if verder.upper() == "Y":
            self.roulette()
        else:
            self.hub()

    def black_jack(self):
        print("\n--- Black Jack ---")
        print(f"Credits: {self.c_redits}")
        self.inzet = int(input("Wat is je inzet? "))
        if self.inzet > self.c_redits:
            print("Niet genoeg credits! Terug naar hub.")
            self.hub()
            return
        self.c_redits -= self.inzet
        import random
        if random.choice([True, False]):
            winst = self.inzet * 2
            self.c_redits += winst
            print(f"Je wint {winst} credits!")
        else:
            print(f"Je verliest {self.inzet} credits!")
        print(f"Credits nu: {self.c_redits}")
        verder = input("Verder spelen? (Y/N): ")
        if verder.upper() == "Y":
            self.black_jack()
        else:
            self.hub()

    # ---------------- Kaarten ----------------
    def randomizer(self):
        import random
        self.kaart = random.randint(1,13)
        print(f"Kaart 1: {self.kaart}")

    def randomizer2(self):
        import random
        self.kaart2 = random.randint(1,13)
        print(f"Kaart 2: {self.kaart2}")

# ---------------- Start ----------------
speler1 = Speler(0,'N',500, None, 0,0,0,0)
speler1.hub()
