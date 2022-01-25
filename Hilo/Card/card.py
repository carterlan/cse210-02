import random 

class Card:

    def __init__(self):
        self.card_1 = random.randint(1,13)
        self.card_2 = random.randint(1,13)
        self.points = 300
    
    def card(self):
        self.card_2 = random.randint(1,13)
        


    def low(self):
        #If player choses low
        self.card_2 = random.randint(1,13)
        if self.card_1 < self.card_2:
            return self.points + 100
        
        if self.card_1 > self.card_2:
            return self.points - 75
    
    def high (self):
        #If player choses high
        if self.card_1 > self.card_2:
            return self.points + 100
        
        if self.card_1 < self.card_2:
            return self.points - 75

      
