POOP_TIME = 40 #How many cycles between when the tamagotchi sleeps
SLEEP_TIME = 100 #How many cycles between when the tamagotchi poops

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
        self.time_since_poop = 0 #It has just been born, it cannot have pooped more then 0 seconds ago
        self.sick = False #The tamagotchi is not born sick
        self.is_alive = True #It is born alive

    def __str__(self):
        #just quickly assemble the stats of the tamagotchi into a string for testing
        output_string = str(self.health) + " " + str(self.hunger) + " " + str(self.happiness) + " " + str(self.care) + " " + str(self.light) + " " + str(self.is_sleep) + " " + str(self.time_since_sleep) + " " + str(self.age) + " " + str(self.weight) + " " + str(self.poop) + " " + str(self.time_since_poop) + " " + str(self.sick) + " " + str(self.is_alive)
        return output_string

    def feed_snack(self):
        #Adjusts the Tamagotchi's values when it eats a snack
        self.health += -25 #Snacks are not healthy, so, they decrease a Tamagotchi's health, making it more prone to sickness
        self.happiness += 50 #increases happiness because it likes snacks, this is about 1/5 of the happiness scale
        self.weight += 1 #increases the weight by one, as per the original Tamagotchi's programming
        if self.health < 0: #Ensures that health does not go below 0
            self.health = 0
        if self.happiness > 255: #Ensures that happiness does not go above 255
            self.happiness = 255

    def feed_meal(self):
        #adjusts the tamagotchi's stats when it eats a meal
        self.hunger += 50 #Increases hunger by about 1/5 of the maximum, as per the original tamagotchi
        self.weight += 2 #Increases the weight by two, as per the original 
        if self.hunger > 255: #ensures that hunger does not go above 255
            self.hunger = 255
        
    def get_variables(self):
        stat_list = [self.health, self.hunger, self.happiness, self.care, self.light, self.is_sleep, self.time_since_sleep, self.age, self.weight, self.poop, self.time_since_poop, self.sick, self.is_alive]
        return stat_list

    def cycle_variables(self, stat_list) -> None:
        (self.health, self.hunger, self.happiness, self.care, self.light, self.is_sleep,self.time_since_sleep, self.age, self.weight, self.poop, self.time_since_poop,self.sick, self.is_alive) = stat_list

    def toggle_light(self):
        #toggles the light of the tamagotchi whenever the function is called
        self.light = not self.light

    def bathroom(self):
        #Clears all of the poop whenever the function is called
        self.poop = 0

    def medicine(self):
        #increments health by 50 whenever the tamagotchi is treated with medicine
        self.health += 50
        if self.health > 255: #If health exceeds the maximum of 255 during this, it resets it to 255
            self.health = 255

    def game(self, is_correct) -> None:
        if is_correct:
            self.happiness += 50 
        self.weight -= 1
        if self.happiness > 255: self.happiness = 255
        if self.happiness < 0: self.happiness = 0
        if self.weight < 1: self.weight = 1

    def increment_health(self) -> None:
        """
        Decreases and increases health based off the hunger, happiness, poop, and other variables
        """
        self.health -= 2 - self.hunger//100
        self.health -= 2 - self.happiness//100
        if not self.light:
            if self.is_sleep:
                self.health +=1
        self.health -= int((((abs(self.weight - 30)+1)*(10**-1))**1.5))
        self.health -= self.poop
        if self.health > 255:
            self.health = 255
        if self.health < 0:
            self.health = 0

    def increment_hunger(self):
        #slowly deteriorates the hunger of the tamagotchi over time in the cycle function
        self.hunger -= 1
        if self.hunger < 0: #The minimum for hunger is 0, so, sets it to 0 if it goes below
            self.hunger = 0

    def increment_happiness(self) -> None:
        self.happiness -= 1 
        if self.happiness < 0:
            self.happiness = 0

    def increment_care(self):
        #Updates the care for this cycle by adding the current values of health, hunger and happiness
        self.care += self.health + self.hunger + self.happiness

    def check_sleep(self):
        #Checks to see if it is time for the tamagotchi to either wake up or go to sleep, doing so if it is
        if self.time_since_sleep >= SLEEP_TIME:
            self.time_since_sleep = 0 #Resets the counter since the state of being asleep has changed
            self.is_sleep = not self.is_sleep #Toggles the state of sleep, waking it up if it is asleep, or going to bed if it is awake
        else:
            self.time_since_sleep += 1 #Otherwise, simply increases the number of cycles since it last toggled is_sleep

    def increment_age(self):
        """
        Increments age by .1
        """
        age = self.age
        age += 0.1
        self.age = round(age,1)

    def increment_poop(self):
        #checks whether the tamagotchi is supposed to poop, pooping if enough cycles have passed
        if self.time_since_poop >= POOP_TIME: #If enough cycles have passed since it last pooped
            self.time_since_poop = 0 #Reset the counter of how long since it has pooped
            self.poop += 1 #And poop
        else: #If it hasn't been long enough yet, add one to the amount of cycles since it has last pooped
            self.time_since_poop += 1 
        if self.poop > 4: #Ensures that poop cannot be greator than 4, as per the original tamagotchi
            self.poop = 4

    def is_sick(self):
        #makes the tamagotchi sick if it's health is below 100
        if self.health <= 100:
            self.sick = True
        else: #If it is above 100, makes the tamagothi not sick
            self.sick = False

    def is_dead(self):
        #sets the state of the tamagotchi to dead if it is at 0 health
        if self.health == 0:
            self.is_alive = False
        else: #Otherwise, sets the tamagotchi to be alive
            self.is_alive = True