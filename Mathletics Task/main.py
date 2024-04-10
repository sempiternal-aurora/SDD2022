from question_gen import generate_question

def check_answer(answer, user_answer) -> bool:
    if answer == user_answer:
        result = True
    else:
        result = False
    return result

def main():
    difficulty = input("Enter a difficulty level: ")
    answer, question = generate_question("A" + str(difficulty))
    print(question)
    user_answer = int(input("Answer: "))
    while user_answer:
        result = check_answer(answer, user_answer)
        if result:
            print("You are correct!")
        else:
            print("That is incorrect, the correct answer was", answer)
        input("Press enter for the next question")
        difficulty = input("Enter a difficulty level: ")
        answer, question = generate_question("A" + str(difficulty))
        print(question)
        user_answer = int(input("Answer: "))

if __name__ == "__main__":
    main()