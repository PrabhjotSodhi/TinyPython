# Program asks for users name, favourite color and two favorite numbers
# Program outputs a greeting and does some Maths....
# Created: 20/07/20
# Author: Prabhjot Sodhi

# Ask user for their name
name = input("what is your name?: ")

# Ask user for their favourite colour
colour = input("What is your favourite colour?: ")

# Ask user for their favourite numbers
num1 = int(input("Choose a number?: "))
num2 = int(input("Choose Another number?: "))

# Do Math!
addition = num1 + num2
subtraction = num1 + num2
division = num1 / num2
multiplication = num1 * num2
print(addition,subtraction,division,multiplication)

# Output Greeting and results!
print("Hi there",name+"!","My favourite color is also",colour)