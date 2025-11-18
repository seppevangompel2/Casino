import random

class Speler:
    def __init__(self, spel, teruggaan, credits=500):
        self.credits = credits
        self.spel = spel
        self.teruggaan = teruggaan

    def hub(self):
        print(self.credits)
        self.teruggaan = "nee"
        self.spel = 0
        print("Welke game wil je spelen?")
        print("----------------------------------------")
        print("1: Slotmachine")
        print("2: Hoger Lager")
        print("3: Paardenrace")
        print("4: Roulette")
        print("5: Black Jack")
        print("----------------------------------------")
        self.spel = int(input("input: "))
        if self.spel == 1:
            self.Slotmachine()
        elif self.spel == 2:
            self.Hoger_Lager()
        elif self.spel == 3:
            self.Paardenrace()
        elif self.spel == 4:
            self.Roulette()
        elif self.spel == 5:
            self.Black_Jack()

    def Slotmachine(self):
        self.teruggaan = input("wil je verder spelen? ")
        if self.teruggaan == "N":
            self.hub()
        elif self.teruggaan == "Y":
            self.Slotmachine()

    def Hoger_Lager(self):
        Hoger_Lager.start_game(self)
        self.teruggaan = input("wil je verder spelen? ")
        if self.teruggaan == "N":
            self.hub()
        elif self.teruggaan == "Y":
            self.Hoger_Lager()

    def Paardenrace(self):
        print("typ uw paardnummers waarop je credits wilt zetten")
        inputs = input().split()
        gekozen_paarden = [int(x) for x in inputs]
        inzet = int(input("hoeveel wil je inzetten?"))
        race1.run_race(gekozen_paarden, inzet, self)
        self.teruggaan = input("wil je verder spelen? ")
        if self.teruggaan == "N":
            self.hub()
        elif self.teruggaan == "Y":
            self.Paardenrace()

    def Roulette(self):
        self.teruggaan = input("wil je verder spelen? ")
        if self.teruggaan == "N":
            self.hub()
        elif self.teruggaan == "Y":
            self.Roulette()

    def Black_Jack(self):
        self.teruggaan = input("wil je verder spelen? ")
        if self.teruggaan == "N":
            self.hub()
        elif self.teruggaan == "Y":
            self.Black_Jack()


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


speler1 = Speler(0, "N")
race1 = Paardenrace()
speler1.hub()
