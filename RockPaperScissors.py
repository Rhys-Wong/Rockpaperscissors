import random

choices = ["rock","scissors", "paper"]

while True:
    computer = random.choices(choices)
    strcom = "".join(computer)
    strcom = strcom.lower()
    user = input("Rock, Paper or Scissors? Press q to quit. ").lower()
    
    if user == "q":
        print("Thanks for playing!")
        break

    if user not in choices:
        print("Please enter a valid input!")
        continue

    print(strcom)

    if user == strcom:
        print("Tie!")
    elif user == "rock":
        if strcom == "scissors":
            print('You win!')
        elif strcom == "paper":
            print("You lose!")
    elif user == "paper":
        if strcom == "rock":
            print('You win!')
        elif strcom == "scissors":
            print("You lose!")
    elif user == "scissors":
        if strcom == "paper":
            print('You win!')
        elif strcom == "rock":
            print("You lose!")





