# Program #3: Capital Quiz
# Write a program that creates a dictionary containing the U.S. states as keys, 
# and their capitals as values.  
# The program should then randomly quiz the user by displaying the name of a state 
# and asking the user to enter the state's capital.  
# The program should count of the number of correct and incorrect responses.  
# (You could alternatively use another country and provinces, 
# or countries of the world and capitals).

import random

def capital_quiz():
    states_and_capitals = {
        "Alabama": "Montgomery",
        "Minnesota": "St.Paul",
        "Alaska": "Juneau",
        "Arizona": "Phoenix",
        "Arkansas": "Little Rock",
        "California": "Sacramento",
        "Colorado": "Denver",
        "Connecticut": "Hartford",
        "Delaware": "Dover",
        "Florida": "Tallahassee",
        "Georgia": "Atlanta"

    }

    correct = 0
    incorrect = 0

    states = list(states_and_capitals.keys())

    print("U.S. State Capitals Quiz!")
    print("Type 'exit' at any time to quit.\n")

    while True:
        state = random.choice(states)
        capital = states_and_capitals[state]

        answer = input(f"What is the capital of {state}? ").strip()

        if answer.lower() == "exit":
            break

        if answer.lower() == capital.lower():
            print("✅ Correct!\n")
            correct += 1
        else:
            print(f"❌ Incorrect. The capital of {state} is {capital}.\n")
            incorrect += 1

    print("Quiz Over!")
    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}")

if __name__ == "__main__":
    capital_quiz()