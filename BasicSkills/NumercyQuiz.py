# Create a class that is defined on initialization of the program
class Question:
    def __init__(self, prompt, answers, correct):
        self.prompt = prompt
        self.answers = answers
        self.correct = correct

# Tuple that stores all the question objects
questions = (
    Question('\n69.9 x 60.08 is closest to', ('4000', '4200', '4400', '4600'), 'b'),
    Question('\nThe cost of 0.267kg of cheese is $7.95. Which calculation is needed to find the cost of 1kg of cheese?',('7.95 ÷ 0.267', '0.267 + 7.95', '0.267 x 7.95', '7.95 – 0.267'), 'a'),
    Question('\n79.8 ÷ 0.092 is closest to:', ('80', '800', '8000', '80,000'), 'b'),
    Question('\nWhich has the largest answer? (Dont do any calculations):', ('218 x 217', '216 x 218', '217 x 219', '216 x 217'), 'c'),
    Question('\nThe percentage profit of $500,909 on sales of $1,998,976 is nearest to:', ('10%','15%','20%','25%'), 'd')
)

valid_answers = ("a", "b", "c", "d")

def ask_questions(questions):
    score = 0 # initial score
    for question in questions: # iterate questions
        while True: # loop until valid input entered
            print(question.prompt)
            for letters in range(len(question.answers)):
                print(f" {valid_answers[letters].upper()}) {question.answers[letters]}")
            answer = input("Answer: ").lower()
            if answer not in valid_answers: # invalid input
                print("invalid input! please try again.")
                continue
            if answer == question.correct: # correct
                score += 1
                print("correct!")
            else: # incorrect
                print("incorrect!")
            break
    return score

def main():
    print("\n\nNUMERACY TEST")
    print("=============")

    name = input("What is your name? ")
    print(f"Hi {name.title()}!, lets test your numeracy knowledge!")

    # Infinite While loop
    while True:
        score = ask_questions(questions)
        # Show results
        if score == len(questions):
            print(f"\nNice {name.title()}! you got {score}/{len(questions)}")
            reset = input("Would you like to take the quiz again(y/n): ")
        elif score <= 2:
            print(f"Too Bad! You suck {name} - {score}/{len(questions)}")
            reset = input("Would you like to take the quiz again(y/n): ")
        else:
            print(f"You did good {name}! - {score}/{len(questions)}")
            reset = input("Would you like to take the quiz again(y/n): ")

        # Check if they want to play again
        if reset == "y":
            score = ask_questions(questions)
        else:
            print("Thanks for playing!")
            break

# Start the Program
main()