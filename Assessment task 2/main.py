import tamagotchi as tg
import cycle
import threading
import time
import tkinter as tk

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
        self.health, self.hunger, self.happiness, self.care, self.light, self.is_sleep, self.time_since_sleep, self.age, self.weight, self.poop, self.time_since_poop, self.sick, self.is_alive = tamagotchi.get_variables()
        if self.is_alive == False:
            self.show_frame(Death_Page)
        self.after(100, self.check_stats)

class Feed_Page(tk.Frame):
    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Page One")
        label.pack()


class Death_Page(tk.Frame):
    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent)
        self.number1 = tk.StringVar()
        self.number2 = tk.StringVar()
        self.operator = tk.StringVar()
        self.answer = tk.StringVar()
        self.operator.set("+")

        label = tk.Label(self, text="Page Two")
        label.grid(row = 0, column = 2)

        number_entry1 = tk.Entry(self, textvariable = self.number1)
        number_entry1.grid(row = 1, column = 0)
        number_entry2 = tk.Entry(self, textvariable = self.number2)
        number_entry2.grid(row = 1, column = 2)
        
        operator_button = tk.Button(self, textvariable = self.operator, command = lambda: self.change_operator())
        operator_button.grid(row = 1, column = 1)
        equals_button = tk.Button(self, text = "=", command = lambda: self.calc_answer())
        equals_button.grid(row = 1, column = 3)
        answer_label = tk.Label(self, textvariable = self.answer)
        answer_label.grid(row = 1, column = 4)

    def change_operator(self):
        current_op = self.operator.get()
        if current_op == "+": self.operator.set("-")
        elif current_op == "-": self.operator.set("x")
        elif current_op == "x": self.operator.set("÷")
        elif current_op == "÷": self.operator.set("^")
        elif current_op == "^": self.operator.set("+")

    def calc_answer(self):
        answer = 0
        operators = {"+":"+", "-":"-", "x":"*", "÷":"/", "^":"**"}
        current_op = operators[self.operator.get()]
        n1 = self.number1.get()
        n2 = self.number2.get()
        try:
            answer = eval(n1 + current_op + n2)
            self.answer.set(answer)
        except:
            self.answer.set("?")

class Stat_Page(tk.Frame): #my gif
    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent)
        

        label = tk.Label(self, text="Page Three")
        label.pack()

class Menu_Page(tk.Frame):
    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Page One")
        label.pack()

class Game_Page(tk.Frame):
    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Page One")
        label.pack()

class Main_Page(tk.Frame):
    def __init__(self, parent, container):
        tk.Frame.__init__(self, parent)

        icon_menu = tk.Button(self, text = "Icon", command = lambda: container.show_frame(Menu_Page))
        icon_menu.grid(column = 0, row = 0, sticky = "w")
        stat_menu = tk.Button(self, text = "Stats", command = lambda: container.show_frame(Stat_Page))
        stat_menu.grid(column = 4, row = 0, sticky = "e")
        label = tk.Label(self, text = "Main Page")
        label.grid(column = 1, columnspan = 3, row = 0, padx = 122)
        #tamagotchi_image = tk.PhotoImage(file = "tamagotchi.gif")
        #tamagotchi_icon = tk.Label(self, image = tamagotchi_image)
        #tamagotchi_icon.grid(column = 0, columnspan = 5, row = 1)
        feed_menu = tk.Button(self, text = "Feed", command = lambda: container.show_frame(Feed_Page))
        feed_menu.grid(column = 0, row = 2)
        play_game = tk.Button(self, text = "Play", command = lambda: container.show_frame(Game_Page))
        play_game.grid(column = 1, row = 2)
        light_button = tk.Button(self, text = "Light", command = lambda: tamagotchi.toggle_light())
        light_button.grid(column = 3, row = 2)
        bathroom_button = tk.Button(self, text = "Bathroom", command = lambda: tamagotchi.bathroom())
        bathroom_button.grid(column = 4, row = 2)

def cycle_thread():
    while is_end == False:
        if is_pause == False:
            cycle_main()
        time.sleep(2)

def cycle_main():
    health, hunger, happiness, care, light, is_sleep, time_since_sleep, age, weight, poop, time_since_poop, sick, is_alive = tamagotchi.get_variables()
    cycled_health = cycle.increment_health(health, hunger, happiness, light, is_sleep, weight, poop)
    cycled_hunger = cycle.increment_hunger(hunger)
    cycled_happiness = cycle.increment_happiness(happiness)
    cycled_care = cycle.increment_care(health, hunger, happiness, care)
    cycled_is_sleep, cycled_time_since_sleep = cycle.check_sleep(is_sleep, time_since_sleep)
    cycled_age = cycle.increment_age(age)
    cycled_poop, cycled_time_since_poop = cycle.increment_poop(poop, time_since_poop)
    cycled_sick = cycle.is_sick(sick, health)
    cycled_is_alive = cycle.is_dead(is_alive, health)
    tamagotchi.cycle_variables(cycled_health, cycled_hunger, cycled_happiness, cycled_care, cycled_is_sleep, cycled_time_since_sleep, cycled_age, cycled_poop, cycled_time_since_poop, cycled_sick, cycled_is_alive)

def load():
    pass

def main():
    global is_end
    load()
    thread = threading.Thread(target= lambda: cycle_thread())
    thread.start()
    my_app = App_Window()
    my_app.mainloop()
    is_end = True

if __name__ == "__main__":
    main()