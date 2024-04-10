from GUI import App_Window
import tamagotchi as tg
import cycle
import threading
import time

global tamagotchi 
global is_pause
global is_end
tamagotchi = tg.Tamagotchi()
is_pause = False
is_end = False

def cycle_thread():
    while is_end == False:
        if is_pause == False:
            cycle_main()
            print("hi")
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