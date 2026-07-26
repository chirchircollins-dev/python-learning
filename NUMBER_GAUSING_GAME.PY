computer_gause = []
user_gause = []

import random
def computer_guess():
    secret = random.randint(1, 100)
    computer_gause.append(secret)
    print("The computer already gaused the number now its your turn😊")


def user_guess(user_number):
    user_number = {"user_number": user_number}
    user_gause.append(user_gause)
    print("Gause submitted")

def high_low_check(user_gause_check, computer_gause_check):
    user_gause_check = user_gause["user_number"]
    computer_gause_check = computer_gause[""]
    if user_gause_check == computer_gause_check:
        print("You Found the Number")
    elif user_gause_check != computer_gause_check:
        print("You are neither too high nor too low") 


import json
def save_user_gause():
    with open("user_gause_file", "w") as file:
        json.dump(user_gause, file)
        print("Your Gause History Updated")

def load_user_gause():
    global user_gause
    try:
        with open("user_gause_file", "r") as file:
            user_gause = (json.load(file))
    except FileNotFoundError:
        pass
    
    







