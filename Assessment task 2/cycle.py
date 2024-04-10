def increment_health(health, hunger, happiness, light, is_sleep, weight, poop):
    return health

def increment_hunger(hunger):
    return hunger

def increment_happiness(happiness):
    return happiness

def increment_care(health, hunger, happiness, care):
    return care

def check_sleep(is_sleep, time_since_sleep):
    return is_sleep, time_since_sleep

def increment_age(age):
    """
    Increments age by .1
    """
    age += 0.1
    return round(age,1)

def increment_poop(poop, time_since_poop):
    return poop, time_since_poop

def is_sick(sick, health):
    return sick

def is_dead(is_alive, health):
    return is_alive