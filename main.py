#HIGHER-LOWER GAME

import art
import random
from replit import clear
from game_data import data

print(art.logo)

def higher_lower_game(): #function created for recursion
    def reset_console():
        """Clears console and prints Higher-Lower logo"""
        clear()
        print(art.logo)
    
    #Assign random celebrities to A and B
    def random_celebrity():
        """Generates a random celebrity"""
        random_celebrity = random.randint(0,49)
        name = data[random_celebrity]["name"]
        follower_count = data[random_celebrity]["follower_count"]
        description = data[random_celebrity]["description"]
        country = data[random_celebrity]["country"]
        return [name, follower_count, description, country]
    
    celebrity_A = random_celebrity()
    celebrity_B = random_celebrity()
    
    #Keep track of score
    score = 0

    #Let's play...
    end_of_game = False
    while end_of_game == False:
        
        #Compare celebrity A with celebrity B
        
        # index 0 = name
        # index 1 = follower_count
        # index 2 = description
        # index 3 = country
    
        print(f"Compare A: {celebrity_A[0]}, a {celebrity_A[2]}, from {celebrity_A[3]}.")
        #print(f"follower count = {celebrity_A[1]}") #test code
        
        print(art.vs)
        
        print(f"Against B: {celebrity_B[0]}, a {celebrity_B[2]}, from {celebrity_B[3]}.")
        #print(f"follower count = {celebrity_B[1]}") #test code
        
        #Take user guess
        guess = input("\nWho has more followers? Type 'A' or 'B': ").upper()
        
        #Is user guess correct?
        #If guess is correct, assign celebrity B to slot A and assign a new random celebrity to slot B. Else, end game.
        if guess == "A" and celebrity_A[1] > celebrity_B[1]:
            score += 1
            celebrity_A = celebrity_B
            celebrity_B = random_celebrity()
            reset_console()
            print(f"You're right! Current score: {score}\n")
        elif guess == "B" and celebrity_B[1] > celebrity_A[1]:
            score += 1
            print(f"SCORE = {score}")
            celebrity_A = celebrity_B
            celebrity_B = random_celebrity()
            reset_console()
            print(f"You're right! Current score: {score}\n")
        elif celebrity_A[1] == celebrity_B[1]:
            score += 1
            print(f"SCORE = {score}")
            celebrity_A = celebrity_B
            celebrity_B = random_celebrity()
            reset_console()
            print(f"You're right! Current score: {score}\n")
        else:
            reset_console()
            print(f"Sorry, that's wrong. Final score: {score}")
            end_of_game = True
    
    replay = input("\nWould you like to play again? Type 'y' or 'n': ")
    if replay == "y":
        reset_console()
        higher_lower_game()
    
higher_lower_game()