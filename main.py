import random
print("         Rock    Paper    Scissors")
print( '''
        To pick "Rock" press "R"
        To pick "Scissors" press "S"
        To pick "Paper" press "P"

''')
player_name = input("Username: ")

def RPS (choice):
    mylist = ["rock", "paper", "scissors"]

    cpu_choice = random.choice(mylist)
    if choice.lower() == "r" and cpu_choice == "scissors" or choice.lower() == "s" and cpu_choice == 'paper' or choice.lower() == 'p' and cpu_choice == "rock":
        print(f"{player_name } won this round")
    elif choice.lower() == "r" and cpu_choice == "paper" or choice.lower() == "s" and cpu_choice == 'rock' or choice.lower() == "p" and cpu_choice == "scissors" :
        print("CPU won this round")
    elif choice.lower() == "r" and cpu_choice == "rock" or choice.lower() == "s" and cpu_choice == 'scissors' or choice.lower() == "p" and cpu_choice == "paper":
        print("it's a tie")
    else :
        print('Pick either R or S or P')

user_choice = input("What are you picking: ")
RPS(user_choice)
print('''
''')
print('''To continue press 1. To cancel press 0''')
ans = input("Do you which to continue: ")
i = 0
while ans == "1":
    i += 1
    print( '''
        To pick "Rock" press "R"
        To pick "Scissors" press "S"
        To pick "Paper" press "P"

''')
    user_choice = input("What are you picking: ")
    RPS(user_choice)
    print('''
    ''')
    if (i == 1):
        print('''To continue press 1. To cancel press 0''')
        ans = input("Do you which to continue: ")
        i = 0
else:
    print("Game over")
