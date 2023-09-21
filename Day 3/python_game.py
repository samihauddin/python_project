import random

# defining a function for rolling dice
def roll_dice():
    return random.randint(1, 6)

# start of the game

print("Let's start the game")
user_name = input("Enter your name: ")

user_score = 0
computer_score = 0

while True:

# allows user to press enter to roll the dice
    input("Press enter to roll the dice")

# role dice function and variable name for users and computer
    user_turn = roll_dice()
    computer_turn = roll_dice()

# write out results
    print(f"{user_name} rolled a {user_turn}")
    print(f"Computer rolled a {computer_turn}")

# score
    user_score += user_turn
    computer_score += computer_turn

# write out results
    print(f"{user_name}'s score: {user_score}")
    print(f"computer's score: {computer_score}")

# if statement when score reaches 30
    if user_score >= 30 or computer_score >= 30:
        break

print("Game Over!")

if user_score == computer_score:
    print("It's a tie")
elif user_score > computer_score:
    print(f"{user_name} wins")
else:
    print("Computer wins")