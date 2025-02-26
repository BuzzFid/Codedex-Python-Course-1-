import random
rock = 1
paper = 2
scissors = 3

choices = {
    1: "✊",
    2: "✋",
    3: "✌️"
}
print("===================")
print("Rock Paper Scissors")
print("===================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")
player = int(input('Pick a number: '))
computer = random.randint(1, 3)

print(f"You chose: {choices[player]}")
print(f"CPU chose: {choices[computer]}")
if player == computer:
    print("It's a tie!")
elif player == 1 and computer == 3:
    print("The player won!")
elif computer == 1 and player == 3:
    print("The computer won!")
elif computer == 2 and player == 1:
    print("The computer won!")
elif player == 2 and computer == 1:
    print("The player won!")
elif computer == 3 and player == 2:
    print("The computer won!")
elif player == 3 and computer == 2:
    print("The player won!")
else:
    print("Invalid input. Please enter a number between 1 and 3.")


