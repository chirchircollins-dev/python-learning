import random
import json

def save(user_guess):
    with open("guess_of_user.json", "w") as file:
        json.dump(user_guess, file)
        print("Guess History Updated")

def load():
    global user_guess
    try:
        with open("guess_of_user.json", "r") as file:
            user_guess = json.load(file)
    except FileNotFoundError:
        pass

def main():
    load()
    global user_guess
    total = 0
    computer_guess = random.randint(1, 100)
    while True:
        print("Welcome to the number guessing game")
        print("1.Start \n  2.Exit \n 3.View History ")
        
        choice = int(input("Enter your choice "))
        
        
        if choice == 1:
            try:
                user_guess = int(input("Please input the random Number between 1-100 "))
            except ValueError:
                print("Enter a valid Number")
                continue
            total += 1
            if 1 <= user_guess <= 100:
                save(user_guess)
                if user_guess == computer_guess:
                    print(f"Thats the number,you got in {total} runs")
                    break
                elif user_guess < computer_guess:
                    print("You are at lower end")
                elif user_guess > computer_guess:
                    print("You are at higher end")
                else:
                    print("Invalid Option")
                    

            else:
                print("Invalid Option")
            
    
        elif choice == 2:
            break
        elif choice == 3:
            load()
            print(f"Your last guess was {user_guess}")
        else:
            print("Invalid Option")
        print(total)

main()