def increment_health(health, hunger, happiness, light, is_sleep, weight, poop):
    """
    Decreases and increases health based off the hunger, happiness, poop, and other variables
    """
    if hunger >= 32:
        health += 3 - hunger//10
    if happiness >= 32:
        health += 3 - happiness//10
    if not light:
        if is_sleep:
            health +=1
    health -= int((((abs(weight - 30)+1)*(10**-1))**1.5))
    health -= poop
    return health

def increment_hunger(hunger):
    return hunger

def increment_happiness(happiness):
    happiness -= 1
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