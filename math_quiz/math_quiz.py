# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random


def number_intialization(min, max): # Function definition for random intialization of numbers
    """
    Random integer.
    """
    return random.randint(min, max)


def operator_selection(): # Function definition for random choice of math operator
    """
    Random operator selection.
    """
    return random.choice(['+', '-', '*'])


def questions_intialization(n1, n2, o): # Function definition for question intialization 
    """
    Quiz Question Intialization.
    """
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2 # these lines are intializing the questions based on operator
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz(): 
    """
    This is the main quiz function in s represent the current turn and t_q represent the total turns allowed to every user.
    """
    s = 0
    t_q = 5 # intiaizing the number of turns for user

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = number_intialization(1, 10); n2 = number_intialization(1, 5); o = operator_selection()

        PROBLEM, ANSWER = questions_intialization(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        try:
            useranswer = input("Your answer: ") # Getting answer from the user
            useranswer = int(useranswer)
        
        except InvalidInput:
            print("Only numeric input allowed")

        if useranswer == ANSWER: # if else statement to check the answer
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}") # This line show the results after t_q turn 

if __name__ == "__main__":
    math_quiz()
