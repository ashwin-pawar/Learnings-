import random

Choice = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter Your Choice : Rock Paper OR Scissor = ")
comp_choice = random.choice(Choice)

print(f" User Choice : {user_choice},  Compter Choice: {comp_choice}")

if user_choice == comp_choice:
    print("Match Tie 🫥 : Both Chooses Same")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Computer Win 🤖!!")
    else:
        print("YOU Win 🙍‍♂️!! Scissor Cut Paper")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Computer Win 🤖!!")
    else:
        print("YOU Win 🙍‍♂️!! Paper Cover Rock")

elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Computer Win 🤖!!")
    else:
      print("YOU Win 🙍‍♂️!!  Rock Smashes Scissor")