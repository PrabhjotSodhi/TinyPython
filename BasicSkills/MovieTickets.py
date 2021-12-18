# Program: Movie Tickets
# Author: Prabhjot Sodhi
# Version: v1.0

# Main Function of the program
def main():
    print("**TICKET PRICES**")
    try:
        price = float(input("What is the ticket price?: ")) # Input on price of each ticket
        people = int(input("How many people?: ")) # Input on number of people attending
    except ValueError:
        pass
    def input_check():
        if isinstance(price, float) and isinstance(people, int):
            pass
        else:
            print(f"Please enter a {type(price)} for ticket price!")
            print(f"Please enter a {type(people)} for number of people!")
    # Calculate the price based on number of people and ticket price
    def CalculatePrice():
        input_check()
        tPrice = price * people
        print(f"Ticket Price: ${tPrice}") 
        # Calculate Discount
        if people >= 8:
            discount = tPrice * 0.25
        else:
            discount = 0
        print(f"Discount: ${discount}")
        print(f"Total Cost: ${tPrice - discount}")
    CalculatePrice() # Run the CalculatePrice Function
    print()
main() # Run the program

#Test Data
#Expected
#Actual


#num_people: ten
#Please enter a number only (no letters)

#num_people: 1
#Program continues

#num_people: 0
#Please enter an number between 1 and 20

#num_people: 21
#Please enter an number between 1 and 20

#num_people: 10
#Program continues...

#num_people: 15.5
#Please enter a number only (no letters)