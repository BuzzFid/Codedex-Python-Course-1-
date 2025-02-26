# Sorting Hat from Hogwarts School of Witchcraft and Wizardry.

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0





print("Welcome to Hogwarts School of Witchcraft and Wizardry!")
print("I am the Sorting Hat. I will determine which house you belong to.")
print("Please answer the following questions honestly.")
print("")
print("")
print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
answer = int(input("Enter your choice: "))
if answer == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif answer == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Wrong input. Please enter 1 or 2.")





print("")
print("")
print("Q2) When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
answer = int(input("Enter your choice: "))
if answer == 1:
    Hufflepuff += 2
elif answer == 2:
    Slytherin += 2
elif answer == 3:
    Ravenclaw += 2
elif answer == 4:
    Gryffindor += 2
else:
    print("Wrong input. Please enter 1, 2, 3 or 4.")




print("\n")
print("Q3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")
answer = int(input("Enter your choice: "))
if answer == 1:
    Slytherin += 4
elif answer == 2:
    Hufflepuff += 4
elif answer == 3:
    Ravenclaw += 4
elif answer == 4:
    Gryffindor += 4
else:
    print("Wrong input. Please enter 1, 2, 3 or 4.")

print("\n")
print("\n")


if Gryffindor >=- Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin:
    print("You belong to 🦁 Gryffindor!")
elif Ravenclaw >= Gryffindor and Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
    print("You belong to 🦅 Ravenclaw!")
elif Hufflepuff >= Gryffindor and Hufflepuff >= Ravenclaw and Hufflepuff >= Slytherin:
    print("You belong to 🦡 Hufflepuff!")
else:
    print("You belong to 🐍 Slytherin!")




# print("Gryffindor: ", Gryffindor)
# print("Ravenclaw: ", Ravenclaw)
# print("Hufflepuff: ", Hufflepuff)
# print("Slytherin: ", Slytherin)