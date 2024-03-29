import tamagotchi as tg
import threading
import time
import tkinter as tk
import random
from tkinter.ttk import Progressbar as Progressbar

global tamagotchi
global is_pause
global is_end
tamagotchi = tg.Tamagotchi()
is_pause = False
is_end = False

CYCLE_TIME = 2 #how many seconds between each cycle
UPDATE_SPEED = 100 #How many milliseconds between each time the App_Window syncs with the tamagotchi

class App_Window(tk.Tk):
    #the actual window that the app exist in, a tkinter construct
    def __init__(self):
        tk.Tk.__init__(self) #Make a Tk GUI window object as a part of this object
        self.title("Tamagotchi")
        self.geometry("405x720")
        main_window_frame = tk.Frame(self) #Define and make a frame object in this window object
        main_window_frame.pack()        #Pack the frame to be visible in the window

        self.frames = {} #create a list for all of the pages
        for f in (Main_Page, Stat_Page, Menu_Page, Feed_Page, Game_Page, Death_Page): #initialise all of the pages in order
            frame = f(main_window_frame, self)
            self.frames[f] = frame
            frame.grid(row = 0, column = 0, sticky = 'nsew') #they go in the center of the window, sticking to all of the edges
        
        self.show_frame(Main_Page) #start by showing the main page, in case another one initialised over the top of it

    def show_frame(self, container): 
        #takes the frame requested, and raises it to the top, essentially showing it from the perspective of the user, even though it was there the whole time
        frame = self.frames[container]
        frame.tkraise()

class Feed_Page(tk.Frame):
    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent) #The normal tkinter frame object initiation

        close_menu = tk.Button(self, text = "X", command = lambda: container.show_frame(Main_Page)) # a button that returns the user to the main page
        close_menu.grid(column = 0, row = 0)
        label = tk.Label(self, text="Feed Manu") #A label to tell the user that this is the feed page
        label.grid(column = 1, row = 0)

        medicine_button = tk.Button(self, text = "Feed Medicine", command = lambda: self.feed_medicine(container)) # A button that calls the tamagotchi's medicine whenever it is pressed, also showing the main page as well
        medicine_button.grid(row = 1, column = 1, ipadx = 40, ipady = 25, padx = 100, pady = 50)
        snack_button = tk.Button(self, text = "Feed Snack", command = lambda: self.feed_snack(container)) #A button that calls the tamagotchi's feed snack method whever pressed, also showing the main page
        snack_button.grid(row = 2, column = 1, ipadx = 50, ipady = 25)
        meal_button = tk.Button(self, text = "Feed Meal", command = lambda: self.feed_meal(container)) #a button that calls the tamagotchi's feed meal function, as well as returning the user to the main page when pressed
        meal_button.grid(row = 3, column = 1, ipadx = 55, ipady = 25, pady = 50)
    
    def feed_snack(self, container):
        #Calls the tamagotchi's feed snack method, before returning the user to the main page
        tamagotchi.feed_snack()
        container.show_frame(Main_Page)

    def feed_meal(self, container):
        #Calls the tamagotchi's feed meal method, before returning the user to the main page
        tamagotchi.feed_meal()
        container.show_frame(Main_Page)

    def feed_medicine(self, container):
        #Calls the tamagotchi's medicine method, before returning the user to the main page
        tamagotchi.medicine()
        container.show_frame(Main_Page)

class Death_Page(tk.Frame):
    #A page that is only shown when the tamagotchi is dead
    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent) #Initialises it via the normal tkinter frame object
        
        death_message = tk.Label(self, text = "Oops, your Tamagotchi has died.\nDo you want to restart?") #A message to show that it is really dead
        death_message.grid(column = 0, row = 0, padx = 115, pady = 25, sticky = "n")

        restart_button = tk.Button(self, text = "Restart", padx = 50, pady = 25, command = lambda: self.restart(container)) #A button that when pressed, reinitalises the tamagotchi and returns the user to the main screen
        restart_button.grid(column = 0, row = 1, pady = 50)
        close_button = tk.Button(self, text = "Exit", padx = 50, pady = 25, command = lambda: self.quit(container)) #A button that when pressed, saves the tamagotchi before closing the program
        close_button.grid(column = 0, row = 2)

        self.after(UPDATE_SPEED, lambda: self.check_death(container))

    def quit(self, container):
        #saves the tamagotchi's data, before quitting
        global tamagotchi
        stat_list = tamagotchi.get_variables() #gets the tamagotchi's current state, before saving it to the save file
        save(stat_list) 
        container.destroy() #Destroys the GUI, effectively stopping the entire program

    def restart(self, container):
        #reinitialises the tamagotchi, and closes the death screen
        global tamagotchi
        global is_pause
        tamagotchi = tg.Tamagotchi() #Reinitalises the tamagotchi as a whole new instance.
        is_pause = False #stops the pause, restarting the regular cycling of the tamagotchi
        container.show_frame(Main_Page) #shows the main page again

    def check_death(self, container):
        if not tamagotchi.is_alive:
            global is_pause
            is_pause = True
            container.show_frame(Death_Page)
        self.after(100, lambda: self.check_death(container))            

class Stat_Page(tk.Frame): 
    #the page that shows the stats of the tamagotchi for the user.
    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent) #The normal Tkinter frame object initiation
        self.health = tk.StringVar() #initiates the variables for all of the meters that are shown on the stats page.
        self.hunger = tk.StringVar()
        self.happiness = tk.StringVar()
        self.age = tk.StringVar()
        self.weight = tk.StringVar()

        close_page = tk.Button(self, text = "X", command = lambda: container.show_frame(Main_Page)) # a button that returns the user to the main page
        close_page.grid(column = 0, row = 0)
        label = tk.Label(self, text="Stat Page") #A label to inform the user of what page they are on
        label.grid(column = 1, row = 0, columnspan = 2) 

        health_label = tk.Label(self, text = "Health:")
        health_label.grid(column = 1, row = 1, sticky = "e")
        health_meter = Progressbar(self, orient = "horizontal", length = 250, mode = "determinate", maximum = 255, variable = self.health) #The bar that displays the Tamagotchi's current health
        health_meter.grid(column = 2, row = 1, pady = 50, padx = 20)
        hunger_label = tk.Label(self, text = "Hunger:")
        hunger_label.grid(column = 1, row = 2, sticky = "e")
        hunger_meter = Progressbar(self, orient = "horizontal", length = 250, mode = "determinate", maximum = 255, variable = self.hunger) #The bar that displays the Tamagotchi's current hunger
        hunger_meter.grid(column = 2, row = 2, padx = 20)
        happiness_label = tk.Label(self, text = "Happiness:")
        happiness_label.grid(column = 1, row = 3, sticky = "e")
        happiness_meter = Progressbar(self, orient = "horizontal", length = 250, mode = "determinate", maximum = 255, variable = self.happiness) #The label that displays the Tamagotchi's current happiness
        happiness_meter.grid(column = 2, row = 3, pady = 50, padx = 20)
        age_label = tk.Label(self, text = "Age:")
        age_label.grid(column = 1, row = 4, sticky = "e")
        age_meter = tk.Label(self, textvariable = self.age) #The label that displays the Tamagotchi's current age
        age_meter.grid(column = 2, row = 4, sticky = "w")
        weight_label = tk.Label(self, text = "Weight:")
        weight_label.grid(column = 1, row = 5, sticky = "e")
        weight_meter = tk.Label(self, textvariable = self.weight) #The label that displays the Tamagotchi's current weight
        weight_meter.grid(column = 2, row = 5, pady = 50, sticky = "w")

        self.update_stats()

    def update_health_meter(self):
        health = str(tamagotchi.health)
        self.health.set(health) #updates the health label's variable, thus updating the label

    def update_hunger_meter(self):
        hunger = str(tamagotchi.hunger)
        self.hunger.set(hunger) #updates the hunger label's variable, thus updating the label

    def update_happiness_meter(self):
        happiness = str(tamagotchi.happiness)
        self.happiness.set(happiness) #updates the happiness label's variable, thus updating the label

    def update_age(self):
        age = str(tamagotchi.age)
        self.age.set(age) #updates the age label's variable, thus updating the label

    def update_weight(self):
        weight = str(tamagotchi.weight)
        self.weight.set(weight) #updates the weight label's variable, thus updating the label

    def update_stats(self):
        #The function that is run to update the various meters to show the tamagotchi's most recent varaibles
        self.update_health_meter() #Update the health label
        self.update_hunger_meter() #Update the hunger label
        self.update_happiness_meter() #update the happiness label
        self.update_age() #update the age label
        self.update_weight() #update the weight label
        self.after(UPDATE_SPEED, lambda: self.update_stats())

class Menu_Page(tk.Frame):
    #The main menu page, holding the buttons to either close the GUI, or save the Tamagotchi's data to a save file
    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent) #Initalise it like a tkinter frame object

        close_button = tk.Button(self, text = "X", command = lambda: self.show_main(container)) #A button that returns the user to the main page when pressed
        close_button.grid(column = 0, row = 0)
        label = tk.Label(self, text = "Menu Page") #A label that tells the user that this is the menu page
        label.grid(column = 1, row = 0, padx = 150)

        save_button = tk.Button(self, text = "Save", padx = 50, pady = 25, command = lambda: self.save_button()) #A button that saves the tamagotchi's data when pressed
        save_button.grid(column = 1, row = 1, pady = 100)
        close_button = tk.Button(self, text = "Exit", padx = 55, pady = 25, command = lambda: container.destroy()) #A button that destroys the whole GUI when pressed, effectively ending the program
        close_button.grid(column = 1, row = 2)

    def show_main(self, container):
        #A function that shows the main page when called, also allowing the cycle system to continue
        global is_pause
        is_pause = False #Un pauses the cycle
        container.show_frame(Main_Page) #Returns the user to the main page

    def save_button(self):
        #Gets the Tamagotchi's current state, before saving it to a text file
        global tamagotchi
        vallist = tamagotchi.get_variables()
        save(vallist)

class Game_Page(tk.Frame):
    #The page that is shown when the user wants to play a game with the tamagotchi
    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent) #Initalises it like a normal tkinter frame
        self.correct_button = generate_left_right() #Determines before the user gets a chance what the first correct answer will be, so that the Tamagotchi can look in the approiate direction if we decide to include that feature
        self.game_label = tk.StringVar() #A variable that will be changed that is to go with the label that will tell the user whether they guessed correctly or incorrectly
        self.game_label.set("Have a guess") #Starts out as the user has not guessed anything yet
        self.image_frames = self.load_image() #Loads the frames of the tamagotchi for the icon
        self.image_index = 0 #sets the index to the first frame

        label = tk.Label(self, text = "Left or Right") #A label that tells the user the name of the game, and the page that they are on
        label.grid(column = 1, columnspan = 2, row = 0, padx = 150)
        close_button = tk.Button(self, text = "X", command = lambda: container.show_frame(Main_Page)) #A button that returns the user to the main page
        close_button.grid(column = 0, row = 0)

        self.tamagotchi_icon = tk.Label(self, image = self.image_frames[self.image_index]) #A sprite of the tamagotchi
        self.tamagotchi_icon.grid(column = 1, columnspan = 2, row = 1, pady = 100)
        answer_label = tk.Label(self, textvariable = self.game_label) #The label mentioned above that will tell the user if they are true or false
        answer_label.grid(column = 1, columnspan = 2, row = 2)
        
        left_button = tk.Button(self, text = "Left", command = lambda: self.play_game("Left")) #The button for the user to guess left with
        left_button.grid(column = 1, row = 3)
        right_button = tk.Button(self, text = "Right", command = lambda: self.play_game("Right")) #The button for the user to guess right with
        right_button.grid(column = 2, row = 3)

        self.after(UPDATE_SPEED, self.animate) #Starts the animation of the gif
    
    def load_image(self):
        #load all of the frames of the animated tamagotchi gif
        target = "Images/tamagotchi.gif" #This is the location of the tamagotchi gif
        frames = [] #a blank list for all of the frames of the tamagotchi
        for i in range(58): #THere are 58 frames in the gif, so, it loads 58 individual frames
            frame = tk.PhotoImage(file = target, format = "gif -index %i"%(i)) #loads the frames of the gif as it's own image, taking only the current frame
            frames.append(frame) #Adds this above single photo to the list of all of the photos that make up the gif
        return frames

    def animate(self, *args):
        #Load all of the images from the frames list, and cycles through them
        if self.image_index < len(self.image_frames) - 1: self.image_index += 1 #If the index is below the number of frames, add 1 to it
        else: self.image_index = 0 #Otherwise, set it to 0
        next_image = self.image_frames[self.image_index] #The next image in the slideshow of the gif is the picture that represents the current index
        self.tamagotchi_icon.configure(image = next_image) #Sets the icon on the actual page to the next image of the gif, effictively animating the picture
        self.after(UPDATE_SPEED, self.animate) #Continues the animation

    def play_game(self, button):
        #The function that determines if the user was correct, and adjusts things accordingly
        if button == self.correct_button: #If what the user guessed matched the right answer they were correct
            is_correct = True
        else: #If it didn't they were wrong
            is_correct = False
        tamagotchi.game(is_correct) #call the tamagotchi's game method with whether the user was right or wrong so that it can iterate accordingly
        if is_correct: #Change the label if they are correct to show that
            self.game_label.set("Yay! You pressed the correct button!")
        else: #Otherwise, change it to show that they weren't right
            self.game_label.set("Aw, Better luck next time")
        self.correct_button = generate_left_right() #generate the next right answer

class Main_Page(tk.Frame):
    #The main page that the user will spend most of their time on. Has all of the buttons to navigate to the required pages
    def __init__(self, parent, container):
        light = tamagotchi.light #Get the state of the tamagotchi's light
        if light: #If it is on, make it a light grey background
            tk.Frame.__init__(self, parent, bg = "yellow")
        else: #If it isn't, make it a dark grey background
            tk.Frame.__init__(self, parent, bg = "gray30")

        self.poop = tk.StringVar() #A variable that will display the current amount of poop
        self.sleep_label = tk.StringVar() #A variable that will tell the user whether the tamagotchi is asleep
        self.image_frames = self.load_image() #Loads the frames of the tamagotchi for the icon
        self.image_index = 0 #sets the index to the first frame

        icon_menu = tk.Button(self, text = "Menu", command = lambda: self.show_menu(container)) #A button that directs the user the the icon page when pressed
        icon_menu.grid(column = 0, row = 0, sticky = "w")
        stat_menu = tk.Button(self, text = "Stats", command = lambda: container.show_frame(Stat_Page)) #A button that directs the user to the stat page when pressed
        stat_menu.grid(column = 6, row = 0, sticky = "e")
        label = tk.Label(self, text = "Main Page") #A label to tell the user that this is the main page
        label.grid(column = 1, columnspan = 5, row = 0, padx = 119)
        sleep_label = tk.Label(self, textvariable = self.sleep_label) #A label to tell the user whether the tamagotchi is asleep or not
        sleep_label.grid(column = 1, columnspan = 5, row = 1)

        self.tamagotchi_icon = tk.Label(self, image = self.image_frames[self.image_index])
        self.tamagotchi_icon.grid(column = 0, columnspan = 7, row = 2, pady = 140)
        feed_menu = tk.Button(self, text = "Feed", command = lambda: container.show_frame(Feed_Page)) #A button that sends the user the the feed page when pressed
        feed_menu.grid(column = 0, row = 3)
        play_game = tk.Button(self, text = "Play", command = lambda: container.show_frame(Game_Page)) #A button that sends the user to the play game page when pressed
        play_game.grid(column = 1, row = 3, sticky = "w")
        light_button = tk.Button(self, text = "Light", command = lambda: self.toggle_light()) #A button that toggles the tamagotchi's light whenever it is pressed, and changes the background colour to match it
        light_button.grid(column = 5, row = 3, sticky = "e")
        bathroom_button = tk.Button(self, text = "Bathroom", command = lambda: tamagotchi.bathroom()) #A button that calls the tamaotchi's bathroom function, clearing all of the poop
        bathroom_button.grid(column = 6, row = 3)
        poop_meter = tk.Label(self, textvariable = self.poop) #A meter that shows how much poop is lying around the tamagotchi
        poop_meter.grid(column = 4, row = 3, sticky = "w")
        poop_label = tk.Label(self, text = "Poop:") #A little label next to the above number to tell the users what the number is
        poop_label.grid(column = 3, row = 3, sticky = "e")

        self.after(UPDATE_SPEED, self.update_main_page)

    def update_main_page(self):
        #A little function that runs all of the functions that update the various details of the main_page
        self.check_poop() #Checks the poop of the tamagotchi
        self.check_sleep() #Checks whether the tamagotchi is asleep, and shows this for the user
        self.animate() #updates the tamagotchi Image to show the next frame of the gif
        self.after(UPDATE_SPEED, self.update_main_page) #Runs this function after UPDATE_SPEED ms, continously updating the main page

    def check_sleep(self):
        #Updates the label that tells the user whether the tamagotchi is sleeping
        sleep = tamagotchi.is_sleep #checks whether the tamagotchi is sleeping
        if sleep: self.sleep_label.set("The Tamagotchi is Sleeping") #If it is, set the label to "The Tamagotchi is Sleeping"
        else: self.sleep_label.set("The Tamagotchi is Awake") #If it isn', set the label to "The Tamagotchi is Awake"

    def load_image(self):
        #load all of the frames of the animated tamagotchi gif
        target = "Images/tamagotchi.gif" #This is the location of the tamagotchi gif
        frames = [] #a blank list for all of the frames of the tamagotchi
        for i in range(58): #THere are 58 frames in the gif, so, it loads 58 individual frames
            frame = tk.PhotoImage(file = target, format = "gif -index %i"%(i)) #loads the frames of the gif as it's own image, taking only the current frame
            frames.append(frame) #Adds this above single photo to the list of all of the photos that make up the gif
        return frames

    def animate(self, *args):
        #Load all of the images from the frames list, and cycles through them
        if self.image_index < len(self.image_frames) - 1: self.image_index += 1 #If the index is below the number of frames, add 1 to it
        else: self.image_index = 0 #Otherwise, set it to 0
        next_image = self.image_frames[self.image_index] #The next image in the slideshow of the gif is the picture that represents the current index
        self.tamagotchi_icon.configure(image = next_image) #Sets the icon on the actual page to the next image of the gif, effictively animating the picture

    def check_poop(self):
        #A quick function to read the poop from the tamagotchi, and update the label on the main page to show this
        poop = str(tamagotchi.poop) #Get the poop value from the tamagotchi and save it to the variable used by the poop_meter, thus updating the meter
        self.poop.set(poop)

    def toggle_light(self):
        #A function to turn the light on or off
        tamagotchi.toggle_light() #Toggles the light via the tamagotchi toggle light method
        self.toggle_background() #calls the toggle background function to reflect this

    def toggle_background(self):
        #A function to change the background colour of the frame to show the whether the light is on
        light = tamagotchi.light #Get the state of the light from the tamagotchi
        if light: #If it is on, make it a light grey background
            Main_Page.configure(self, bg = "yellow")
        else: #If it isn't, make it a dark grey background
            Main_Page.configure(self, bg = "gray30")

    def show_menu(self, container):
        #A function that pauses the cycle, before showing the user the menu page
        global is_pause #Pauses the cycle
        is_pause = True
        container.show_frame(Menu_Page) #Shows the User the Main_Page

def generate_left_right():
    #A quick little program to generate a left or right direction. Designed for the left or right game, but theoretically can be used for anything
    number = random.randrange(0, 2) #Generates a random number of either 1 or 0
    if number == 0: #0 means it is left
        direction = "Left"
    elif number == 1: #1 means it is right
        direction = "Right"
    return direction #return the left or right

def cycle_thread():
    #A simple function that runs the cycling of the variables over and over again
    while is_end == False: #is_end is naturally set to True when the GUI is closed by whatever method, so, until this happens, it is an infinite loop
        if is_pause == False: #This means it only actually cycles the varaibles if the tamagotchi isn't paused
            cycle_main() #The calling of the cycle function
        time.sleep(CYCLE_TIME) #Because this is a thread, doing this doesn't actually stop the whole program, just this thread. So it is fine

def cycle_main():
    #Calls all of the tamagotchi's increment functions to update the tamagotchi as time passes
    #0 = health, 1 = hunger, 2 = happiness, 3 = care, 4 = light, 5 = is_sleep, 6 = time_since_sleep, 7 = age, 8 = weight, 9 = poop, 10 = time_since_poop, 11 = sick, 12 = is_alive
    global tamagotchi
    tamagotchi.increment_health() #increments the Tamagotchis health based on it's current health, hunger, happiness, light, is_sleep, weight and poop
    tamagotchi.increment_hunger() #increments hunger
    tamagotchi.increment_happiness() #increments happiness
    tamagotchi.increment_care() #increments care based on health, hunger and happiness
    tamagotchi.check_sleep() #determines if the tamagotchi is asleep from is_sleep and time_since_sleep, as well as updating how long it has been since this has changed, or time_since_sleep
    tamagotchi.increment_age() #increments the age by a small amount
    tamagotchi.increment_poop() #determine how many poops it should have based off of poop and time_since_poop
    tamagotchi.is_sick() #determines if it is sick with is_sick and health
    tamagotchi.is_dead() #Based on the tamagotchi's health, determines whether it is alive

def convert_vals(var):
    """
    Janky programe for converting stings True and False into a bool
    """
    digits = ['0','1','2','3','4','5','6','7','8','9']
    is_numeric = False
    for i in digits:
        if i in var: is_numeric = True
    if is_numeric:
        if "." in var: var = float(var)
        else: var = int(var)
    else:
        if var == "True": var = True
        elif var == "False": var = False
        else: raise ValueError
    return var

def encode(var) -> str:
    """
    encodes the value of the given var into a hex string with the value for each char being four digits long
    and the whole value being 32 charecters long
    """
    encodedval = ""
    for e in range(32 - len(var)):
        var ="￼" + var 
    for i in range(len(var)):
        encodechar = var[i]
        charval = ord(encodechar)
        hexval = ("0000"+ hex(charval)[2:])[-4:]
        encodedval = encodedval + " " + hexval
    return encodedval

def decode(var) -> str:
    """
    Decodes the given value list into a list of chars deleating any ￼ char that is in the front of the list
    """
    varval = []
    decodedval = ""
    var = str(var)[1:].split(" ")
    for i in range(len(var)):
        decodechar = int(var[i], 16)
        charval = chr(decodechar)
        varval.append(charval) 
        if varval[0] == "￼":
            varval.pop(0)
    for y in range(len(varval)):
        decodedval = decodedval + varval[y]
    decodedval = convert_vals(decodedval)
    return decodedval

def save(variables) -> None:
    """
    Save the state of the programme so that it can be accesed accross instances
    """
    enlist = ""
    savfile = open("Tamagotchisav.txt","w")
    for i in range(len(variables)):
        envall = encode(str(variables[i]))
        enlist = enlist + envall + "\n"
    savfile.writelines(enlist)
    savfile.close()

def load() -> list:
    """
    Loads saved variable values from save file so the user can contiue from there last save state
    """
    vallist = []
    savfile = open("Tamagotchisav.txt","r")
    filedat = savfile.readlines()
    for i in range(len(filedat)):
        val = decode(filedat[i])
        vallist.append(val)
    savfile.close()
    return vallist

def main():
    #The main part of the program
    #Firstly, collect necessary global varaibles
    global is_end
    stat_list = load() #This loads all of the values from a text file
    if stat_list != []: #this just makes sure that it isn't a blank list that is being used
        tamagotchi.cycle_variables(stat_list) #This then takes those loaded values and changes the tamagotchi to start with them, basically loading up the last saved state
    thread = threading.Thread(target = cycle_thread) #This starts a thread which the cycle runs on, so it is seperate from the app_window and is thus not hindered by it stopping on the next line
    thread.start()
    my_app = App_Window() #Initialises the app_window
    my_app.mainloop()
    is_end = True #the line above this won't be moved on from until the GUI is closed. When this happens, this event occurs, which stops the cycle above.

if __name__ == "__main__":
    #This is always true, so, it always runs the following function
    #It is a native varaible of python, and as such is initalised as the value shown
    main()