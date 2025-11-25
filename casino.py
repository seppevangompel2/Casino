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
        print("----------------------------------------")
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
            print("----------------------------------------")
        else:
            print(f"Naam {self.naam} is toegevoegd.")
            print("----------------------------------------")
        accounts[self.naam] = self.c_redits

        # Schrijf alles netjes terug
        with open("names.txt", "w") as document:
            for naam, c_redits in accounts.items():
                document.write(f"{naam}\n{c_redits}\n")

    def load_stats(self):
        self.naam = input("Wat is uw naam van uw account? ").strip()
        print("----------------------------------------")
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
            print("----------------------------------------")
        else:
            print("Naam niet gevonden, probeer opnieuw.")
            print("----------------------------------------")

    def play_blackjack(self):
        while True:
            if self.c_redits <= 0:
                print("\nJe hebt geen chips meer! Spel is afgelopen.")
                print("----------------------------------------")
                break
            print(f"\nJe hebt {self.c_redits:.0f} chips.")
            print("----------------------------------------")
            # Plaats een inzet
            while True:
                try:
                    bet = float(input("Plaats je inzet: "))
                    print("----------------------------------------")
                    if bet <= 0 or bet > self.c_redits:
                        print(f"Ongeldige inzet. Je hebt {self.c_redits:.0f} chips.")
                        print("----------------------------------------")
                    else:
                        break
                except ValueError:
                    print("Voer een geldig getal in.")
                    print("----------------------------------------")
            # Initialiseer het spel
            deck = Deck()
            player = Player("Speler")
            dealer = Player("Dealer")
            # Geef begin kaarten
            player.add_card(deck.pop())
            player.add_card(deck.pop())
            dealer.add_card(deck.pop())
            dealer.add_card(deck.pop())
            # Beurt van de speler
            while True:
                print("----------------------------------------")
                print(f"\n{player}, Score: {player.score()}")
                print(f"Dealer toont: {dealer.cards[0]}")
                print("----------------------------------------")
                choice = input('Wil je nog een kaart? (y/n): ').lower()
                print("----------------------------------------")
                if choice == 'y':
                    player.add_card(deck.pop())
                    if player.score() > 21:
                        print(f"\n{player}, Score: {player.score()}")
                        print("----------------------------------------")
                        print("Speler heeft verloren! Dealer wint.")
                        print("----------------------------------------")
                        self.c_redits -= bet
                        break
                elif choice == 'n':
                    break
                else:
                    print("Ongeldige keuze. Probeer opnieuw.")
                    print("----------------------------------------")
            # Beurt van de dealer
            if player.score() <= 21:
                print(f"\nDealer toont: {dealer}, Score: {dealer.score()}")
                print("----------------------------------------")
                while dealer.score() < 17:
                    dealer.add_card(deck.pop())
                    print(f"Dealer trekt: {dealer.cards[-1]}, Score: {dealer.score()}")
                    print("----------------------------------------")
                # Bepaal de winnaar
                player_score = player.score()
                dealer_score = dealer.score()
                print(f"\n{player}, Score: {player_score}")
                print("----------------------------------------")
                print(f"{dealer}, Score: {dealer_score}")
                print("----------------------------------------")
                if dealer_score > 21:
                    print("Dealer heeft verloren! Speler wint.")
                    print("----------------------------------------")
                    self.c_redits += bet * 1.5  # Winst: 1.5x de inzet
                elif player_score > dealer_score:
                    print("Speler wint!")
                    print("----------------------------------------")
                    self.c_redits += bet * 1.5  # Winst: 1.5x de inzet
                elif dealer_score > player_score:
                    print("Dealer wint!")
                    print("----------------------------------------")
                    self.c_redits -= bet  # Verlies: inzet kwijt
                else:
                    print("Gelijkspel.")
                    print("----------------------------------------")
                    self.c_redits = self.c_redits  # Gelijkspel: inzet terug
            print(f"\nJe hebt nu {self.c_redits:.0f} chips.")
            print("----------------------------------------")
            # Vraag of de speler nog een keer wil spelen
            play_again = input("\nWil je nog een keer spelen? (y/n): ").lower()
            print("----------------------------------------")
            if play_again != 'Y':
                print("Bedankt voor het spelen!")
                print("----------------------------------------")
                break

    def hub(self):
        print("----------------------------------------")
        print(f"\n--- Hub ---")
        print("----------------------------------------")
        print(f"Credits: {self.c_redits}")
        print("----------------------------------------")
        antwoord = input('Wil je je stats opslaan of laden? O/L: ')
        print("----------------------------------------")
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
        print("----------------------------------------")
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
        print("----------------------------------------")
        print("\n--- Hoger/Lager ---")
        print("----------------------------------------")
        print(f"Credits: {self.c_redits}")
        print("----------------------------------------")
        self.inzet = int(input("Wat is jouw inzet? "))
        print("----------------------------------------")
        if self.inzet > self.c_redits:
            print("Niet genoeg credits! Terug naar hub.")
            print("----------------------------------------")
            self.hub()
            return
        self.c_redits -= self.inzet
        self.randomizer()
        self.keuze = input("Kies hoger (H) of lager (L): ").upper()
        print("----------------------------------------")
        self.randomizer2()
        if (self.keuze == "L" and self.kaart2 <= self.kaart) or (self.keuze == "H" and self.kaart2 >= self.kaart):
            winst = self.inzet * 2
            self.c_redits += winst
            print(f"Je wint {winst} credits!")
            print("----------------------------------------")
        else:
            print(f"Je verliest {self.inzet} credits!")
            print("----------------------------------------")
        print(f"Credits nu: {self.c_redits}")
        print("----------------------------------------")
        self.teruggaan = input("Verder spelen? (Y/N): ")
        if self.teruggaan.upper() == "Y":
            self.hogerlager()
        else:
            self.hub()

    def paardenrace(self):
        print("----------------------------------------")
        print("typ uw paardnummers waarop je credits wilt zetten")
        print("----------------------------------------")
        inputs = input().split()
        gekozen_paarden = [int(x) for x in inputs]
        inzet = int(input("hoeveel wil je inzetten?"))
        print("----------------------------------------")
        race1.run_race(gekozen_paarden, inzet)
        self.teruggaan = input("wil je verder spelen? ")
        if self.teruggaan == "N":
            self.hub()
        elif self.teruggaan == "Y":
            self.paardenrace()
        print("\n--- Paardenrace ---")
        print(f"Credits: {self.c_redits}")
        print("----------------------------------------")
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
        print("----------------------------------------")
        if self.inzet > self.c_redits:
            print("Niet genoeg credits! Terug naar hub.")
            print("----------------------------------------")
            self.hub()
            return
        self.c_redits -= self.inzet

        print("Je kan inzetten op: 1=1 getal, 2=2 getallen, 3=3 getallen, 12=dozijn, even, oneven")
        print("----------------------------------------")
        keuze = input("Wat kies je? ").lower()
        print("----------------------------------------")

        if keuze == "1":
            gekozen = [int(input("Welk getal (0-36)? "))]
            print("----------------------------------------")
        elif keuze == "2":
            gekozen = [int(input("Getal 1: ")), int(input("Getal 2: "))]
            print("----------------------------------------")
        elif keuze == "3":
            gekozen = [int(input(f"Getal {i+1}: ")) for i in range(3)]
            print("----------------------------------------")
        elif keuze == "12":
            keuze2 = input("Kies dozijn 1 (1-12), 2 (13-24), 3 (25-36): ")
            print("----------------------------------------")
            if keuze2 == "1":
                gekozen = list(range(1,13))
                print("----------------------------------------")
            elif keuze2 == "2":
                gekozen = list(range(13,25))
                print("----------------------------------------")
            elif keuze2 == "3":
                gekozen = list(range(25,37))
                print("----------------------------------------")
            else:
                print("Ongeldige keuze. Terug naar hub.")
                print("----------------------------------------")
                self.hub()
                return
        elif keuze == "even":
            gekozen = [i for i in range(1,37) if i % 2 == 0]
        elif keuze == "oneven":
            gekozen = [i for i in range(1,37) if i % 2 == 1]
        else:
            print("Ongeldige keuze. Terug naar hub.")
            print("----------------------------------------")
            self.hub()
            return

        resultaat = random.randint(0,36)
        print(f"Het balletje valt op: {resultaat}")
        print("----------------------------------------")
        if resultaat in gekozen:
            winst = self.inzet * 2
            self.c_redits += winst
            print(f"Je hebt gewonnen {winst} credits!")
            print("----------------------------------------")
        else:
            print(f"Je hebt verloren {self.inzet} credits!")
            print("----------------------------------------")

        print(f"Credits nu: {self.c_redits}")
        print("----------------------------------------")
        verder = input("Verder spelen? (Y/N): ")
        if verder.upper() == "Y":
            self.roulette()
        else:
            self.hub()

    def black_jack(self):
        print("\n--- Black Jack ---")
        print(f"Credits: {self.c_redits}")
        print("----------------------------------------")
        self.inzet = int(input("Wat is je inzet? "))
        if self.inzet > self.c_redits:
            print("----------------------------------------")
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
        print("----------------------------------------")
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
        print("----------------------------------------")

    def randomizer2(self):
        import random
        self.kaart2 = random.randint(1,13)
        print(f"Kaart 2: {self.kaart2}")
        print("----------------------------------------")

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
    print("----------------------------------------")
    def __init__(self):
        self.winnende_paard = None
        self.tal_paarden = 12

    def run_race(self, gekozen_paarden, inzet_bedrag):
        import random
        if inzet_bedrag > speler1.c_redits:
            print("je hebt niet genoeg credits")
            print("----------------------------------------")
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
class Deck:
    card_categories = ['Harten', 'Ruiten', 'Klaveren', 'Schoppen']
    cards_list = ['Aas', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Boer', 'Vrouw', 'Heer']
    def __init__(self):
        import random
        self.cards = [Card(card, category) for category in self.card_categories for card in self.cards_list]
        random.shuffle(self.cards)
    def pop(self):
        return self.cards.pop()

class Card:
    def __init__(self, card, category):
        self.card = card
        self.category = category
    def value(self):
        if self.card in ['Boer', 'Vrouw', 'Heer']:
            return 10
        elif self.card == 'Aas':
            return 11
        else:
            return int(self.card)
    def __repr__(self):
        return f"{self.card} {self.category}"
class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)
    def score(self):
        total = sum(card.value() for card in self.cards)
        aces = sum(1 for card in self.cards if card.card == 'Aas')
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def __repr__(self):
        return f"{self.name}: {', '.join(str(card) for card in self.cards)}"


speler1=Speler(0,"N")
Hoger_Lager=HogerLager(0, 0, 0,'L')
race1 = Paardenrace()
#start game
speler1.hub()

#bron f strings: https://www.geeksforgeeks.org/python/formatted-string-literals-f-strings-python/
