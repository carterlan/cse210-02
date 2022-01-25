import random 

class Card:

    def __init__(self):
        self.value = 0
        self.points = 300

    def show_card(self): 
    
      card = random.randint(1,13)
