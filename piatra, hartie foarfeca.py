#EXERCITIUL CU JOCUL
#paper, stone, scissors
#random
#rezultat

import random
import time

while True:
    VALORI = ['paper', 'stone', 'scissors']
    User = input(str("Choose your object: paper, stone or scissors\n"))
    pc = random.choice(VALORI)
    print(f"\nYou choose {User}, computer choose {pc}.\n")
    
    if User == pc:
        print(f"Both players selected {User}. It's a tie!")
    elif User == "rock":
        if pc == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif User == "paper":
        if pc == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif User == "scissors":
        if pc == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    time.sleep(5)






