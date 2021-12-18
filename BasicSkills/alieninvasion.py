''' Program: Alien Invasion
Date written: 9 November 2020
Purpose: aliens have gotten control over the
earth they can manipulate earthlings age '''

import random

earthlings = [] # List to store instances of Earthling Class
MAX_EARTHLINGS = int(input("Number of Earthlings: ")) # max number of earthlings to have
OPERATORS = ['-','+','*'] # Constant to store choices of operators

# Create a Class for earthling
class Earthling():
    # Have every instace of Earthling to be unique
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # parse console input
    @staticmethod # can be called without creating an instance
    def user_input():
        while True: # when function is called this will always happen
            try: # try doing this
                name = input("Enter Earthlings Name: ") # In the instance of earthling store name from input
                if not name.isalpha(): # Check for value errors when alien is inputing data(checks if input is letters)
                    print("only letters are allowed!") # inform the user of mistake
                    raise ValueError # raise a valueerror causing except to trigger
            except: # if error occurs do this
                print("ErrorInvaildInput: Please Try again")
                continue
            age = None
            while age == None:
                try:
                    age = float(input("Enter Earthlings Age: ")) # In the instance of earthling store age from input
                    if age <= 0 or age > 120: # Check for value errors when alien is inputing data(checks if age is in threshold)
                        print("Please enter age between 0-120") # inform the user of mistake
                        age = None
                        raise ValueError # raise a valueerror causing except to trigger
                except: # if error occurs do this
                    print("ErrorInvaildInput: Please Try again")
                    continue
            return Earthling(name, age) # Return instance

# STAGE 1 - Start asking the user for names and ages of earthlings
while len(earthlings) < MAX_EARTHLINGS:
    print(f"\n-------- Earthling {len(earthlings)+1} --------")
    earthling = Earthling.user_input() # run the class static method
    earthlings.append(earthling) # append the earthling instance to earthlings list
if len(earthlings) == 0: # To prevent ZeroDivisionError
    exit()
print(end='\n') # Formating print

# STAGE 2 - Changing Values
for earthling in earthlings:
    # randrange is used insteand of randint because index goes from 0-3 while len() goes 1-3
    operator_index = random.randrange(0, len(OPERATORS)) # randrange -1 from the len() to work with indexes
    operator = OPERATORS[operator_index] # Use the index to get random operator from the list
    age_change = random.randint(0,100) # use a random age change number between 0-100
    print(f"OPERATOR: {operator}\tAGE CHANGE: {age_change}") # Print for debugging
    earthling.age = eval(f'earthling.age{operator}age_change') # Change the age through eval()


# STAGE 3 - Output
death_count = 0
death_percent = 0
for earthling in earthlings:
    if earthling.age <= 0 or earthling.age > 120:
        print(f"{earthling.name} has virtually died")
    else:
        print(f"{earthling.name} is now {earthling.age}")
    if earthling.age <= 0 or earthling.age > 120:
        death_count += 1
        death_percent = 100*(death_count/len(earthlings)) # Calculate Percentage
print(f"{round(death_percent, 2)}% have died") # Round the percentage and print