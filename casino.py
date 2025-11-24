import random
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
        #jouw code
        self.teruggaan = (input("wil je verder spelen? "))
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



