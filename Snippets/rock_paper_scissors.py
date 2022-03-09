import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. "))

computer = random.randint(0,2)

print("You chose: ")
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
else:
    print(scissors)

print("Computer chose: ")
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)

result = choice - computer
print(result)

if result == 0:
    print("You tied.")
elif result == 1 or result == -2:
    print("You won!")
else:
    print("You lost...")