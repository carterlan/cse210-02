import random 

class Card:

    def __init__(self):
        self.card_1 = 0
        self.card_2 = 0
        self.points = 300

    def show_card(self): 
    
        card_1 = random.randint(1,13)
        card_2 = random.randint(1,13)

    def low(self):
        if self.card_1 < self.card_2:
            return self.points + 100
        
        if self.card_1 > self.card_2:
            return self.ppints - 300
    
    def high (self):
        if self.card_1 > self.card_2:
            return self.points + 100
        
        if self.card_1 < self.card_2:
            return self.points - 75

      
