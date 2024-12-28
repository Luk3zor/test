import random
import cowsay
import keyboard

#What will your software do? What features will it have? How will it be executed?
#What new skills will you need to acquire? What topics will you need to research?
#If working with one or two classmates, who will do what?
#In the world of software, most everything takes longer to implement than you expect. And so it’s not uncommon to accomplish
#less in a fixed amount of time than you hope. What might you consider to be a good outcome for your project? A better outcome? The best outcome?

def main():
    difficulty = level_select()
    cowsay.cow(f"Moooo! Okay, let's get started with level {difficulty}")
    correct_streak = 0
    total_correct = 0
    total_incorrect = 0

    while True:
        num1, num2, answer, operation = generate_problem(difficulty)

        # check if correct or incorrect
        if play_game(num1, num2, answer, operation):
            correct_streak += 1
            total_correct += 1
            if correct_streak == 5:
                cowsay.tux("⭐⭐ Amazing! You got 5 correct in a row! ⭐⭐")
                break  # stop loop after 5 correct answers
        else:
            correct_streak = 0
            total_incorrect += 1

        if total_incorrect == 10:
            cowsay.tux("Let's take a little break. You got 10 incorrect. 😭")
            break

        if keyboard.is_pressed('esc'):
            print("Game Over. You pressed 'Esc' to exit.")
            break


def level_select():

    print("*" * 50)
    print("*{:^48}*".format("Select a difficulty level"))
    print("*" * 50)

    print("* {:<45} *".format("Level 1: Adds two numbers"))
    print("* {:<45} *".format("Level 2: Subtracts two numbers"))
    print("* {:<45} *".format("Level 3: Multiplies two numbers"))
    print("*" * 50)

    while True:
        try:
            difficulty = int(input("Enter your choice (1, 2, or 3): "))
            if difficulty in [1, 2, 3]:
                return difficulty
            else:
                print("Sorry, try again. Enter 1, 2, or 3.")
        except ValueError:
            print("Sorry, try again. Enter 1, 2, or 3. (VE)")

def generate_problem(difficulty):
    # level 1 - adds two numbers
    # level 2 - subtracts two numbers
    # level 3 - multiplies two numbers
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)

    if difficulty == 1:
        answer = num1 + num2
        operation = '+'
    elif difficulty == 2:
        answer = num1 - num2
        operation = '-'
    elif difficulty == 3:
        answer = num1 * num2
        operation = '*'
    else:
        raise ValueError("Invalid difficulty level")

    return num1, num2, answer, operation


def play_game(num1, num2, answer, operation):
    # while true loop, so that if they press key other than numbers, it will ask them to input again
    while True:
        try:
            guess = int(input(f"What is {num1} {operation} {num2}?: "))
            if guess == answer:
                cowsay.cow("Great job! That's correct.")
                return True
            else:
                cowsay.stegosaurus("Oops! Better luck next time.")
                return False
        except ValueError:
            print("Sorry numbers only please!")


if __name__ == "__main__":
    main()