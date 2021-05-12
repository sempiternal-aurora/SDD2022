class Tamagotchi():
    def __init__(self):
        #sets up all of the basic stats of the tamagotchi
        print("Initialising Tamagotchi") #Tells the user that the Tamagotchi is being created
        self.health = 255 #all health hunger and happiness start at their maximun values of 255
        self.hunger = 255
        self.happiness = 255
        self.care = 0 #starts at 0, acts as a measure of the quality of a tamagotchi's life, so gets larger with better treatment
        self.light = True #The light starts turned on
        self.is_sleep = False #The tamagotchi starts waking up
        self.time_since_sleep = 0 #The Tamagotchi has just woken up, for convinence
        self.age = 0 #It follows it's whole life, so we start at 0
        self.weight = 15 #Not entirely sure about, but start at an ideal weight, or there abouts. May change this as we see fit
        self.poop = 0 #It has not existed long enough to poop yet, thus, no poop

    def __str__(self):
        #just quickly assemble the stats of the tamagotchi into a string for testing
        output_string = str(self.health) + " " + str(self.hunger) + " " + str(self.happiness) + " " + str(self.care) + " " + str(self.light) + " " + str(self.is_sleep) + " " + str(self.time_since_sleep) + " " + str(self.age) + " " + str(self.weight) + " " + str(self.poop)
        return output_string

    def feed_snack(self):
        #Adjusts the Tamagotchi's values when it eats a snack
        self.health += -25 #Snacks are not healthy, so, they decrease a Tamagotchi's health, making it more prone to sickness
        self.happiness += 50 #increases happiness because it likes snacks, this is about 1/5 of the happiness scale
        self.weight += 1 #increases the weight by one, as per the original Tamagotchi's programming

    def feed_meal(self):
        #adjusts the tamagotchi's stats when it eats a meal
        self.hunger += 50 #Increases hunger by about 1/5 of the maximum, as per the original tamagotchi
        self.weight += 2 #Increases the weight by two, as per the original tamagotchis

tamagotchi = Tamagotchi()
print(tamagotchi)