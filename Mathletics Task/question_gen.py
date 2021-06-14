import random

def generate_question(question_type) -> tuple:
    #Generates a random question based on the type of question required
    if question_type[0] == "A":
        difficulty = int(question_type[1])
        a = random.randint((10 ** (difficulty - 1)), ((10 ** difficulty) - 1))
        b = random.randint((10 ** (difficulty - 1)), ((10 ** difficulty) - 1))
        answer = a + b
        question = "What do you get when you add " + str(a) + " and " + str(b) + "?"
    return answer, question
