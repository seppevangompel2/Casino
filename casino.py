import random
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
                print(f"Credits remaining: {self.credits}")
                print("----------------------------------------")
            else:
                self.credits += 100
                print("----------------------------------------")
                print(f"Rolled:{result}")
                print("+100C")
                print(f"Credits remaining: {self.credits}")
                print("----------------------------------------")
        elif last_digit == second_last_digit:
            self.credits += 40
            print("----------------------------------------")
            print(f"Rolled:{result}")
            print("+40C")
            print(f"Credits remaining: {self.credits}")
            print("----------------------------------------")

        else:
            self.credits -= 10
            print("----------------------------------------")
            print(f"Rolled:{result}")
            print("-10C")
            print(f"Credits remaining: {self.credits}")
            print("----------------------------------------")

slot1 = Slotmachine(500)
stop = 0
while stop == 0 and slot1.credits > 0:
    answer = input("Roll?: ")
    if answer == "Y":
        slot1.roll()
    elif answer == "E" or answer == "N":
        stop = 1