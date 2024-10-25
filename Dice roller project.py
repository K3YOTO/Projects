import random

#get the number of sides for the dice
num_sides = int(input("How many sides does the dice have?"))

#rolling the dice
roll_again = "yes"
while roll_again == "yes":
    print("Rolling rice...")
    print("The result is:", random.randint(1, num_sides))
    roll_again = input("Roll again? (yes/no) ").lower()
    