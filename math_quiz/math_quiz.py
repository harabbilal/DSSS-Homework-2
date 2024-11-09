# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random


def number_limit(min, max): # Function definition for random intialization of numbers
    """
    Random integer.
    """
    return random.randint(min, max)


def math_operation(): # Function definition for random choice of math operator
    return random.choice(['+', '-', '*'])


def calculation(n1, n2, o): # Function definition for question intialization 
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2 # these lines are intializing the questions based on operator
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz(): 
    s = 0
    t_q = 3 # intiaizing the number of turns

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = number_limit(1, 10); n2 = number_limit(1, 5); o = math_operation()

        PROBLEM, ANSWER = calculation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ") # Getting answer from the user
        useranswer = int(useranswer)

        if useranswer == ANSWER: # if else statement to check the answer
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}") # This line show the results after t_q turn 

if __name__ == "__main__":
    math_quiz()
