class Speler:import random
class Speler:
    def __init__(self,spel,teruggaan, credits = 500):
        self.credits = credits
        self.spel = spel
        self.teruggaan = teruggaan
    def hub(self):
        print("credits", self.credits)
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
        while (self.spel != 1) and (self.spel != 2) and (self.spel != 3) and (self.spel != 4) and (self.spel != 5):
            print("geen mogelijke input, probeer opnieuw.")
            self.spel = (int(input("input: ")))
        if self.spel == 1:
            self.slotmachine()
        elif self.spel==2:
            self.hoger_lager()
        elif self.spel==3:
            self.paardenrace()
        elif self.spel==4:
            self.roulette()
        elif self.spel==5:
            self.black_jack()
    def slotmachine(self):
        slot1 = Slotmachine(self.credits)
        stop = 0
        while stop == 0 and slot1.credits > 0:
            print("Roll?")
            print("----------------------------------------")
            print("Y: ja")
            print("N: nee")
            print("----------------------------------------")
            answer = input("Antwoord: ")
            if answer == "Y":
                slot1.roll()
            elif answer == "E" or answer == "N":
                self.credits = slot1.stop()
                stop = 1
        print("Wil je verder spelen?")
        print("----------------------------------------")
        print("Y: ja")
        print("N: nee")
        print("----------------------------------------")
        self.teruggaan = (input("Antwoord: "))
        if self.teruggaan == "N":
            self.hub()
        elif self.teruggaan == "Y":
            self.slotmachine()
    def hoger_lager(self):
        #jouw code
        Hoger_Lager.start_game(self)
        self.teruggaan = (input("wil je verder spelen? "))
        if self.teruggaan == "N":
            self.hub()
        elif self.teruggaan == "Y":
            self.hoger_lager()
    def paardenrace(self):
        print("typ uw paardnummers waarop je credits wilt zetten")
        inputs = input().split()
        gekozen_paarden = [int(x) for x in inputs]
        inzet = int(input("hoeveel wil je inzetten?"))
        race1.run_race(gekozen_paarden, inzet, self)
        self.teruggaan = input("wil je verder spelen? ")
        if self.teruggaan == "N":
            self.hub()
        elif self.teruggaan == "Y":
            self.paardenrace()
    def roulette(self):
    #jouw code
        import random
        print("\n--- Roulette ---")
        print(f"Credits: {self.credits}")
        inzet = int(input("Wat is je inzet? "))
        if inzet > self.credits:
            print("Niet genoeg credits! Terug naar hub.")
            self.hub()
            return
        self.credits -= inzet
        print("Je kan inzetten op: 1=1 getal, 2=2 getallen, 3=3 getallen, 12=dozijn, even, oneven")
        keuze = input("Wat kies je? ").lower()
        if keuze == "1":
            gekozen = [int(input("Welk getal (0-36)? "))]
        elif keuze == "2":
            gekozen = [int(input("Getal 1: ")), int(input("Getal 2: "))]
        elif keuze == "3":
            gekozen = [int(input(f"Getal {i + 1}: ")) for i in range(3)]
        elif keuze == "12":
            keuze2 = input("Kies dozijn 1 (1-12), 2 (13-24), 3 (25-36): ")
            if keuze2 == "1":
                gekozen = list(range(1, 13))
            elif keuze2 == "2":
                gekozen = list(range(13, 25))
            elif keuze2 == "3":
                gekozen = list(range(25, 37))
            else:
                print("Ongeldige keuze. Terug naar hub.")
                self.hub()
                return
        elif keuze == "even":
            gekozen = [i for i in range(1, 37) if i % 2 == 0]
        elif keuze == "oneven":
            gekozen = [i for i in range(1, 37) if i % 2 == 1]
        else:
            print("Ongeldige keuze. Terug naar hub.")
            self.hub()
            return
        resultaat = random.randint(0, 36)
        print(f"Het balletje valt op: {resultaat}")
        if resultaat in gekozen:
            winst = inzet * 2
            self.credits += winst
            print(f"Je hebt gewonnen {winst} credits!")
        else:
            print(f"Je hebt verloren {inzet} credits!")
        print(f"Credits nu: {self.credits}")
        verder = input("Verder spelen? (Y/N): ")
        if verder.upper() == "Y":
            self.roulette()
        else:
            self.hub()
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
class Slotmachine:
    def __init__(self, credits):
        self.credits = credits
    def roll(self):
        result = random.randint(111,999)
        last_digit = result % 10
        second_last_digit = (result // 10) % 10
        if (result % 111) == 0:
            if result == 777:
                self.credits += 500
                print("----------------------------------------")
                print(f"Rolled:{result}")
                print("Jackpot! +200C")
                print(f"Credits: {self.credits}")
                print("----------------------------------------")
            else:
                self.credits += 100
                print("----------------------------------------")
                print(f"Rolled:{result}")
                print("+100C")
                print(f"Credits: {self.credits}")
                print("----------------------------------------")
        elif last_digit == second_last_digit:
            self.credits += 40
            print("----------------------------------------")
            print(f"Rolled:{result}")
            print("+40C")
            print(f"Credits: {self.credits}")
            print("----------------------------------------")

        else:
            self.credits -= 10
            print("----------------------------------------")
            print(f"Rolled:{result}")
            print("-10C")
            print(f"Credits: {self.credits}")
            print("----------------------------------------")
    def stop(self):
        return self.credits
class Hoger_Lager:
    def __init__(self,inzet,kaart,kaart2):
        self.inzet=inzet
        self.kaart = kaart
        self.kaart2=kaart2
    def start_game(self,player):
        print("credits:", player.credits)
        self.inzet=int(input("wat is jouw inzet? "))
        if self.inzet > player.credits:
            print("je hebt niet zoveel geld.")
            self.start_game(player)
        player.credits -=self.inzet
        self.randomizer()
        self.keuze = input("kies hoger (H) of lager (L). ")
        self.randomizer2()
        if self.keuze == "L":
            if self.kaart2 <= self.kaart:
                player.credits += self.inzet*2
                print("je verdient ", self.inzet, "credits")
        if self.keuze == "H":
            if self.kaart2 >= self.kaart:
                player.credits += self.inzet*2
                print("je verdient ", self.inzet, "credits")
    def randomizer2(self):
        kaartnummers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.kaart2 = random.choice(kaartnummers)
        print(self.kaart2)
    def randomizer(self):
        kaartnummers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.kaart = random.choice(kaartnummers)
        print (self.kaart)
class Paardenrace:
    def __init__(self):
        self.winnende_paard = None
        self.tal_paarden = 12

    def run_race(self, gekozen_paarden, inzet_bedrag, speler):
        if inzet_bedrag > speler.credits:
            print("je hebt niet genoeg credits")
            return

        speler.credits -= inzet_bedrag
        self.winnende_paard = random.randint(1, self.tal_paarden)
        print("winnend paard:", self.winnende_paard)

        if self.winnende_paard in gekozen_paarden:
            print("je wint")
            winst = (self.tal_paarden * inzet_bedrag) // len(gekozen_paarden)
            speler.credits += winst
        else:
            print("je verliest")

        print("nieuwe credits:", speler.credits)

#eventuele instanties
speler1=Speler(0,"N")
Hoger_Lager=Hoger_Lager(0,0,0)
race1 = Paardenrace()
#start game
speler1.hub()



