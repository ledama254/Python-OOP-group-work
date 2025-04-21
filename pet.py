class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting at mid-level
        self.energy = 5   # Starting at mid-level
        self.happiness = 5  # Starting at mid-level
        self.tricks = []  # For storing learned tricks
        
    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} eats happily. Hunger decreases, happiness increases!")
    
    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} takes a nap. Energy restored!")
    
    def play(self):
        if self.energy >= 2:  # Need energy to play
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} plays excitedly!")
        else:
            print(f"{self.name} is too tired to play right now.")
    
    def get_status(self):
        print("\n" + "="*20)
        print(f"{self.name}'s Status:")
        print(f"Hunger: {'★' * self.hunger}{'☆' * (10 - self.hunger)}")
        print(f"Energy: {'★' * self.energy}{'☆' * (10 - self.energy)}")
        print(f"Happiness: {'★' * self.happiness}{'☆' * (10 - self.happiness)}")
        print("="*20 + "\n")
    
    # Bonus methods
    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} learned a new trick: {trick}!")
            self.happiness = min(10, self.happiness + 1)
            self.energy = max(0, self.energy - 1)
        else:
            print(f"{self.name} already knows {trick}.")
    
    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks:")
            for i, trick in enumerate(self.tricks, 1):
                print(f"{i}. {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")