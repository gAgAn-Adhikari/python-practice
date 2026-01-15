import random

name = input("your nickname -->> ")

print("Rules for this Game --> "
      "Rock vs paper --> paper wins "
      "Paper vs scissor --> scissor wins "
      "Rock vs scissor --> Rock wins")

print(f"welcome {name} !!!")

count = 0
com_count = 0

while True:
    print("1). Rock \n2). Paper\n3). Scissor")

    choice = int(input("Enter your choice--> "))
    while choice > 3 or choice < 1:
        choice = int(input("Enter your choice--> "))

    if choice == 1:
        choice_name = 'rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'

    print(f"{name} has chosen {choice_name}")

    com_choice = random.randint(1, 3)
    if com_choice == 1:
        com_choice_name = 'rock'
    elif com_choice == 2:
        com_choice_name = 'paper'
    else:
        com_choice_name = 'scissor'

    print(f"computer has chosen {com_choice_name}")

    # Determine winner
    if choice_name == com_choice_name:
        print("No points, it's a tie...")
    elif (choice_name == 'rock' and com_choice_name == 'scissor') or \
         (choice_name == 'paper' and com_choice_name == 'rock') or \
         (choice_name == 'scissor' and com_choice_name == 'paper'):
        print("You got a point!")
        count += 1
    else:
        print("Computer got a point!")
        com_count += 1

    print(f"Total points till now:\n{name} -> {count}\nComputer -> {com_count}")

    again = input("Do you want to continue? (y/n): ").lower()
    if again == 'n':
        break

print("Thank you for playing!")

if count > com_count:
    print("You got better of this AI...")
elif count == com_count:
    print("You both were equally shit...")
else:
    print("You got destroyed by AI...")