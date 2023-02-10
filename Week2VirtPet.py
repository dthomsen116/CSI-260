class VirtualPet:
    hunger = 0
    __mood = 0
    boredom = 0
    happiness = 0
    play = 10
    
    def __init__(self, name, bore, hunger):
        self.name = name
        self.hunger = hunger
        self.bore = bore
        self.happy()
        
    def talk(self):
        print("My name is " + self.name)
        print("Boredom: ", self.bore)
        print("Hunger: ", self.hunger)
        
    def petname(self):
        return(self.name)

    def happy(self):
        if self.boredom < 51:
            self.happy = self.happy + 50
        
        if self.hunger > 75:
            self.happy = self.happy + 50
        
        if self.happy > 80:
            self.__mood = "siked"
        
        if self.happy < 80 and self.happy >= 60:
            self.__mood = "playful"
        
        if self.happy < 59 and self.happy >= 40:
            self.__mood = "surviving"
        
        if self.happy < 39 and self.happy >= 20:
            self.__mood = "barely-surviving"
        
        if self.happy < 20:
            self.__mood = "Agony"
            
        else:
            self.__mood = "frenzied"
        
        
    def feed(self):
        self.hunger = self.feed - 20
        self.play = self.play - 1
        
    def play(self):
        self.play = self.play + 2
        self.bore = self.bore - 10

Matt = VirtualPet("Matt", 50, 100)
Matt.talk()
