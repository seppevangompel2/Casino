import random

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
    def Hoger_Lager(self):
        #jouw code
        Hoger_Lager.start_game(self)
        self.teruggaan = (input("wil je verder spelen? "))
        if self.teruggaan == "N":
            self.hub()
        elif self.teruggaan == "Y":
            self.Hoger_Lager()
    def paardenrace(self):
        #jouw code
        self.teruggaan = (input("wil je verder spelen? "))
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
        self.inzet=int(input("wat is jouw inzet? "))
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

#eventuele instanties
speler1=Speler(0,"N")
Hoger_Lager=Hoger_Lager(0,0,0)

#start game
speler1.hub()

