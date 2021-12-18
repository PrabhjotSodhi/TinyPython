# Program asks for expenses
# Program outputs the total amount of expenses
# Created: 20/07/20
# Author: Prabhjot Sodhi

# Asks the user for how much they spent for expenses
clothes = input("how much do you spend on clothes?: ")
transport = input("how much do you spend on transport?: ")
food = input("how much do you spend on food?: ")
rent = input("how much do you spend on rent?: ")
output = str(int(clothes)+int(transport)+int(food)+int(rent))

# Prints the total
print("You spend:","$"+output)