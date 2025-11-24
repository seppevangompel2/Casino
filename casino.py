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
    def slotmachine(self):
        import random
        result = random.randint(111, 999)
        last_digit = result % 10
        second_last_digit = (result // 10) % 10
        if (result % 111) == 0:
            if result == 777:
                self.c_redits += 500
                print("----------------------------------------")
                print(f"Rolled:{result}")
                print("Jackpot! +200C")
                print(f"Credits: {self.c_redits}")
                print("----------------------------------------")
            else:
                self.c_redits += 100
                print("----------------------------------------")
                print(f"Rolled:{result}")
                print("+100C")
                print(f"Credits: {self.c_redits}")
                print("----------------------------------------")
        elif last_digit == second_last_digit:
            self.c_redits += 40
            print("----------------------------------------")
            print(f"Rolled:{result}")
            print("+40C")
            print(f"Credits: {self.c_redits}")
            print("----------------------------------------")

        else:
            self.c_redits -= 10
            print("----------------------------------------")
            print(f"Rolled:{result}")
            print("-10C")
            print(f"Credits: {self.c_redits}")
            print("----------------------------------------")

        return self.c_redits

    def save_name(self):
        self.naam = input("Wat is uw naam? ").strip()

        # Lees bestaande accounts
        accounts = {}
        try:
            with open("names.txt", "r") as document:
                regels = document.readlines()
            i = 0
            while i < len(regels) - 1:
                naam = regels[i].strip()
                try:
                    c_redits = int(regels[i + 1].strip())
                except ValueError:
                    c_redits = 500
                accounts[naam] = c_redits
                i += 2
        except FileNotFoundError:
            pass

        # Update of voeg nieuwe naam toe
        if self.naam in accounts:
            print("Deze naam bestaat al, credits worden bijgewerkt.")
        else:
            print(f"Naam {self.naam} is toegevoegd.")
        accounts[self.naam] = self.c_redits

        # Schrijf alles netjes terug
        with open("names.txt", "w") as document:
            for naam, c_redits in accounts.items():
                document.write(f"{naam}\n{c_redits}\n")

    def load_stats(self):
        self.naam = input("Wat is uw naam van uw account? ").strip()

        accounts = {}
        try:
            with open("names.txt", "r") as document:
                regels = document.readlines()
            i = 0
            while i < len(regels) - 1:
                naam = regels[i].strip()
                try:
                    c_redits = int(regels[i + 1].strip())
                except ValueError:
                    c_redits = 500
                accounts[naam] = c_redits
                i += 2
        except FileNotFoundError:
            pass

        if self.naam in accounts:
            self.c_redits = accounts[self.naam]
            print(f'Je account {self.naam} heeft {self.c_redits} credits.')
        else:
            print("Naam niet gevonden, probeer opnieuw.")
    def hub(self):
        print(f"\n--- Hub ---")
        print(f"Credits: {self.c_redits}")
        antwoord = input('Wil je je stats opslaan of laden? O/L: ')
        if antwoord.upper() == 'O':
            self.save_name()
        elif antwoord.upper() == 'L':
            self.load_stats()
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
        print("typ uw paardnummers waarop je credits wilt zetten")
        inputs = input().split()
        gekozen_paarden = [int(x) for x in inputs]
        inzet = int(input("hoeveel wil je inzetten?"))
        race1.run_race(gekozen_paarden, inzet)
        self.teruggaan = input("wil je verder spelen? ")
        if self.teruggaan == "N":
            self.hub()
        elif self.teruggaan == "Y":
            self.paardenrace()
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

class Slotmachine:
    def __init__(self, c_redits):
        self.c_redits = c_redits
    def roll(self):
        import random
        result = random.randint(111,999)
        last_digit = result % 10
        second_last_digit = (result // 10) % 10
        if (result % 111) == 0:
            if result == 777:
                self.c_redits += 500
                print("----------------------------------------")
                print(f"Rolled:{result}")
                print("Jackpot! +200C")
                print(f"Credits: {self.c_redits}")
                print("----------------------------------------")
            else:
                self.c_redits += 100
                print("----------------------------------------")
                print(f"Rolled:{result}")
                print("+100C")
                print(f"Credits: {self.c_redits}")
                print("----------------------------------------")
        elif last_digit == second_last_digit:
            self.c_redits += 40
            print("----------------------------------------")
            print(f"Rolled:{result}")
            print("+40C")
            print(f"Credits: {self.c_redits}")
            print("----------------------------------------")

        else:
            self.c_redits -= 10
            print("----------------------------------------")
            print(f"Rolled:{result}")
            print("-10C")
            print(f"Credits: {self.c_redits}")
            print("----------------------------------------")
    def stop(self):
        return self.c_redits
class HogerLager:
    def __init__(self,inzet,kaart,kaart2, keuze1):
        self.inzet=inzet
        self.kaart = kaart
        self.kaart2=kaart2
        self.keuze1 = keuze1
    def start_game(self,player):
        print("credits:", player.c_redits)
        print("----------------------------------------")
        self.inzet=int(input("wat is jouw inzet? "))
        print("----------------------------------------")
        if self.inzet > player.c_redits:
            print("je hebt niet zoveel geld.")
            print("----------------------------------------")
            self.start_game(player)
        player.c_redits -=self.inzet
        self.randomizer()
        print("kies hoger of lager.")
        print("----------------------------------------")
        print("H: hoger")
        print("L: lager")
        print("----------------------------------------")
        self.keuze1 = input("input ")
        print("----------------------------------------")
        self.randomizer2()
        if self.keuze1 == "L":
            if self.kaart2 <= self.kaart:
                player.c_redits += self.inzet * 2
                print("je verdient ", self.inzet, "credits")
                print("----------------------------------------")
        if self.keuze1 == "H":
            if self.kaart2 >= self.kaart:
                player.c_redits += self.inzet * 2
                print("je verdient ", self.inzet, "credits")
                print("----------------------------------------")
    def randomizer2(self):
        import random
        kaartnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.kaart2 = random.choice(kaartnummers)
        print("tweede kaart:",self.kaart2)
        print("----------------------------------------")
    def randomizer(self):
        import random
        kaartnummers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.kaart = random.choice(kaartnummers)
        print("getrokken kaart:",self.kaart)
        print("----------------------------------------")
class Paardenrace:
    def __init__(self):
        self.winnende_paard = None
        self.tal_paarden = 12

    def run_race(self, gekozen_paarden, inzet_bedrag):
        import random
        if inzet_bedrag > speler1.c_redits:
            print("je hebt niet genoeg credits")
            return

        speler1.c_redits -= inzet_bedrag
        self.winnende_paard = random.randint(1, self.tal_paarden)
        print("----------------------------------------")
        print("winnend paard:", self.winnende_paard)

        if self.winnende_paard in gekozen_paarden:
            print("je wint")
            winst = (self.tal_paarden * inzet_bedrag) // len(gekozen_paarden)
            speler1.c_redits += winst
        else:
            print("je verliest")

        print("Credits:", speler1.c_redits)
        print("----------------------------------------")
speler1=Speler(0,"N")
Hoger_Lager=HogerLager(0, 0, 0,'L')
race1 = Paardenrace()
#start game
speler1.hub()

#bron f strings: https://www.geeksforgeeks.org/python/formatted-string-literals-f-strings-python/
