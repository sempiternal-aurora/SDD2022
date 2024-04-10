import tamagotchi as tg
import cycle
import threading
import time
import tkinter as tk
import os


global tamagotchi
global is_pause
global is_end
tamagotchi = tg.Tamagotchi()
is_pause = False
is_end = False

class App_Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self) #Make a Tk GUI window object as a part of this object
        self.title("Tamagotchi")
        self.geometry("405x720")
        main_window_frame = tk.Frame(self) #Define and make a frame object in this window object
        main_window_frame.pack()        #Pack the frame to be visible in the window

        self.frames = {}
        for f in (Main_Page, Stat_Page, Menu_Page, Feed_Page, Game_Page, Death_Page):
            frame = f(main_window_frame, self)
            self.frames[f] = frame
            frame.grid(row = 0, column = 0, sticky = 'nsew')
        
        self.show_frame(Main_Page)
        self.check_stats()

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

    def check_stats(self):
        self.stat_list = tamagotchi.get_variables()
        if self.stat_list[12] == False:
            self.show_frame(Death_Page)
        self.update_stats_page()
        self.after(100, self.check_stats)

    def update_stats_page(self):
        frame = self.frames[Stat_Page]
        frame.update_stats(self)

class Feed_Page(tk.Frame):
    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Feed Manu")
        label.grid(column = 1, row = 0)

        close_menu = tk.Button(self, text = "X", command = lambda: container.show_frame(Main_Page))
        close_menu.grid(column = 0, row = 0)

        medicine_button = tk.Button(self, text = "Feed Medicine", command = lambda: self.feed_medicine(container))
        medicine_button.grid(row = 1, column = 1, ipadx = 50, ipady = 25, padx = 90, pady = 25)
        snack_button = tk.Button(self, text = "Feed Snack", command = lambda: self.feed_snack(container))
        snack_button.grid(row = 2, column = 1, ipadx = 50, ipady = 25)
        meal_button = tk.Button(self, text = "Feed Meal", command = lambda: self.feed_meal(container))
        meal_button.grid(row = 3, column = 1, ipadx = 50, ipady = 25, pady = 25)
    
    def feed_snack(self, container):
        tamagotchi.feed_snack()
        container.show_frame(Main_Page)

    def feed_meal(self, container):
        tamagotchi.feed_meal()
        container.show_frame(Main_Page)

    def feed_medicine(self, container):
        tamagotchi.medicine()
        container.show_frame(Main_Page)

class Death_Page(tk.Frame):
    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent)
        
        death_message = tk.Label(self, text = "Oops, your Tamagotchi has died.\nDo you want to restart?")
        death_message.grid(column = 0, row = 0, padx = 115, pady = 25, sticky = "n")

        restart_button = tk.Button(self, text = "Restart", padx = 50, pady = 25, command = lambda: self.restart(container))
        restart_button.grid(column = 0, row = 1, pady = 50)
        close_button = tk.Button(self, text = "Exit", padx = 50, pady = 25, command = lambda: container.destroy())
        close_button.grid(column = 0, row = 2)

    def restart(self, container):
        #reinitialises the tamagotchi, and closes the death screen
        global tamagotchi
        tamagotchi = tg.Tamagotchi()
        container.show_frame(Main_Page)

class Stat_Page(tk.Frame): 
    #the page that shows the stats of the tamagotchi for the user.
    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Page Three")
        label.pack()

        button_page2 = tk.Button(self, text = "Go to Main Page", command = lambda: container.show_frame(Main_Page))
        button_page2.pack()

    def update_stats(self, container):
        pass

class Menu_Page(tk.Frame):
    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent)

        close_button = tk.Button(self, text = "X", command = lambda: self.show_main(Main_Page, container))
        close_button.grid(column = 0, row = 0)
        label = tk.Label(self, text = "Menu Page")
        label.grid(column = 1, row = 0, padx = 150)

        save_button = tk.Button(self, text = "Save", padx = 50, pady = 25, command = lambda: self.save_button())
        save_button.grid(column = 1, row = 1, pady = 50)
        close_button = tk.Button(self, text = "Exit", padx = 50, pady = 25, command = lambda: container.destroy())
        close_button.grid(column = 1, row = 2)

    def show_main(self, target, container):
        global is_pause
        is_pause = False
        container.show_frame(target)

    def save_button(self):
        global tamagotchi
        valtuple = tamagotchi.get_variables()
        vallist = list(valtuple)
        save(vallist)

class Game_Page(tk.Frame):
    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Page One")
        label.pack()
        button_page2 = tk.Button(self, text = "Go to Main Page", command = lambda: container.show_frame(Main_Page))
        button_page2.pack()

class Main_Page(tk.Frame):
    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent)

        icon_menu = tk.Button(self, text = "Menu", command = lambda: self.show_menu(Menu_Page, container))
        icon_menu.grid(column = 0, row = 0, sticky = "w")
        stat_menu = tk.Button(self, text = "Stats", command = lambda: container.show_frame(Stat_Page))
        stat_menu.grid(column = 4, row = 0, sticky = "e")
        label = tk.Label(self, text = "Main Page")
        label.grid(column = 1, columnspan = 3, row = 0, padx = 119)
        tamagotchi_image = tk.PhotoImage(file = "images/tamagotchi.png")
        tamagotchi_icon = tk.Label(self, image = tamagotchi_image)
        tamagotchi_icon.grid(column = 0, columnspan = 5, row = 1)
        feed_menu = tk.Button(self, text = "Feed", command = lambda: container.show_frame(Feed_Page))
        feed_menu.grid(column = 0, row = 2)
        play_game = tk.Button(self, text = "Play", command = lambda: container.show_frame(Game_Page))
        play_game.grid(column = 1, row = 2, sticky = "w")
        light_button = tk.Button(self, text = "Light", command = lambda: tamagotchi.toggle_light())
        light_button.grid(column = 3, row = 2, sticky = "e")
        bathroom_button = tk.Button(self, text = "Bathroom", command = lambda: tamagotchi.bathroom())
        bathroom_button.grid(column = 4, row = 2)

    def show_menu(self, target, container):
        global is_pause
        is_pause = True
        container.show_frame(target)

def cycle_thread():
    while is_end == False:
        if is_pause == False:
            cycle_main()
        time.sleep(2)

def cycle_main():
    #0 = health, 1 = hunger, 2 = happiness, 3 = care, 4 = light, 5 = is_sleep, 6 = time_since_sleep, 7 = age, 8 = weight
    #9 = poop, 10 = time_since_poop, 11 = sick, 12 = is_alive
    stat_list = tamagotchi.get_variables()
    cycled_health = cycle.increment_health(stat_list[0], stat_list[1], stat_list[2], stat_list[4], stat_list[5], stat_list[8], stat_list[9])
    cycled_hunger = cycle.increment_hunger(stat_list[1])
    cycled_happiness = cycle.increment_happiness(stat_list[2])
    cycled_care = cycle.increment_care(stat_list[0], stat_list[1], stat_list[2], stat_list[3])
    cycled_is_sleep, cycled_time_since_sleep = cycle.check_sleep(stat_list[5], stat_list[6])
    cycled_age = cycle.increment_age(stat_list[7])
    cycled_poop, cycled_time_since_poop = cycle.increment_poop(stat_list[9], stat_list[10])
    cycled_sick = cycle.is_sick(stat_list[11], stat_list[0])
    cycled_is_alive = cycle.is_dead(stat_list[12], stat_list[0])
    stat_list = [cycled_health, cycled_hunger, cycled_happiness, cycled_care, cycled_is_sleep, cycled_time_since_sleep, cycled_age, cycled_poop, cycled_time_since_poop, cycled_sick, cycled_is_alive]
    tamagotchi.cycle_variables(stat_list)

def convert_bool(string) -> bool:
    """
    janky programe for converting stings True and False into a bool
    """
    if string == "True": string == True
    elif string == "False": string == False
    else: raise ValueError
    return string

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
    try:
        decodedval = int(decodedval)
    except:
        try:
            decodedval = convert_bool(decodedval)
        except:
            pass
    return decodedval

def save(variables):
    """
    Save the state of the programme so that it can be accesed accross instances
    """
    enlist = ""
    savfile = open("Tamagotchisav.txt","w")
    for i in range(len(variables)):
        envall = encode(str(variables[i]))
        enlist = enlist + envall + "\n"
    savfile.write(enlist)
    savfile.close()

def load():
    """
    Loads saved variable values from save file so the user can contiue from there last save state
    """
    vallist = []
    savfile = open("Tamagotchisav.txt","r")
    filedat = savfile.read()
    for i in range(len(filedat)):
        val = decode(filedat[i])
        vallist.append(val) 
    savfile.close()
    return vallist

def main():
    global is_end
    global tamagotchi
    os.chdir("Tamagotchi_App")
    stat_list = load()
    #tamagotchi.cycle_variables(stat_list)
    thread = threading.Thread(target= lambda: cycle_thread())
    thread.start()
    my_app = App_Window()
    my_app.mainloop()
    is_end = True

if __name__ == "__main__":
    main()