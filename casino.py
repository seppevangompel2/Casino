class speler:
    def __init__(self,spel,teruggaan, credits = 500):
        self.credits = credits
        self.spel = spel
        self.teruggaan = teruggaan
    def hub(self):
        print(self.credits)
        self.teruggaan = "nee"
        self.spel=0
        self.spel=(int(input("welk spel wil je spelen? ")))
        if self.spel == 1:
            self.spel1()
        elif self.spel==2:
            self.spel2()
    def spel1(self):
        #jouw code
        self.teruggaan = (input("wil je verder spelen? "))
        if self.teruggaan == "N":
            self.hub()
    def spel2(self):
        #jouw code
        self.teruggaan = (input("wil je verder spelen? "))
        if self.teruggaan == "N":
            self.hub()
    def spel3(self):
        #jouw code
        self.teruggaan = (input("wil je verder spelen? "))
        if self.teruggaan == "N":
            self.hub()
    def spel4(self):
        #jouw code
        self.teruggaan = (input("wil je verder spelen? "))
        if self.teruggaan == "N":
            self.hub()
    def spel5(self):
        #jouw code
        self.teruggaan = (input("wil je verder spelen? "))
        if self.teruggaan == "N":
            self.hub()
speler1=speler(0,"nee")
#eventuele instanties
speler1.hub()
