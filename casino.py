import random

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

class Deck:
    card_categories = ['Harten', 'Ruiten', 'Klaveren', 'Schoppen']
    cards_list = ['Aas', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Boer', 'Vrouw', 'Heer']

    def __init__(self):
        self.cards = [Card(card, category) for category in self.card_categories for card in self.cards_list]
        random.shuffle(self.cards)

    def pop(self):
        return self.cards.pop()

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

def play_blackjack(chips=100):
    while True:
        if chips <= 0:
            print("\nJe hebt geen chips meer! Spel is afgelopen.")
            break

        print(f"\nJe hebt {chips:.0f} chips.")

        # Plaats een inzet
        while True:
            try:
                bet = float(input("Plaats je inzet: "))
                if bet <= 0 or bet > chips:
                    print(f"Ongeldige inzet. Je hebt {chips:.0f} chips.")
                else:
                    break
            except ValueError:
                print("Voer een geldig getal in.")

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
            print(f"\n{player}, Score: {player.score()}")
            print(f"Dealer toont: {dealer.cards[0]}")

            choice = input('Wil je nog een kaart? (j/n): ').lower()
            if choice == 'j':
                player.add_card(deck.pop())
                if player.score() > 21:
                    print(f"\n{player}, Score: {player.score()}")
                    print("Speler heeft verloren! Dealer wint.")
                    chips -= bet
                    break
            elif choice == 'n':
                break
            else:
                print("Ongeldige keuze. Probeer opnieuw.")

        # Beurt van de dealer
        if player.score() <= 21:
            print(f"\nDealer toont: {dealer}, Score: {dealer.score()}")
            while dealer.score() < 17:
                dealer.add_card(deck.pop())
                print(f"Dealer trekt: {dealer.cards[-1]}, Score: {dealer.score()}")

            # Bepaal de winnaar
            player_score = player.score()
            dealer_score = dealer.score()

            print(f"\n{player}, Score: {player_score}")
            print(f"{dealer}, Score: {dealer_score}")

            if dealer_score > 21:
                print("Dealer heeft verloren! Speler wint.")
                chips += bet * 1.5  # Winst: 1.5x de inzet
            elif player_score > dealer_score:
                print("Speler wint!")
                chips += bet * 1.5  # Winst: 1.5x de inzet
            elif dealer_score > player_score:
                print("Dealer wint!")
                chips -= bet  # Verlies: inzet kwijt
            else:
                print("Gelijkspel.")
                chips += bet  # Gelijkspel: inzet terug

        print(f"\nJe hebt nu {chips:.0f} chips.")

        # Vraag of de speler nog een keer wil spelen
        play_again = input("\nWil je nog een keer spelen? (j/n): ").lower()
        if play_again != 'j':
            print("Bedankt voor het spelen!")
            break

# Start het spel met 100 chips
play_blackjack(100)
