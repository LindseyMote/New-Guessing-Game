#!/usr/bin/python

import random, time, statistics
from random import randint
from statistics import median, mode, mean

guess_list = []
num_of_guesses = []

def game_solution():
    int(random.randint(1, 20))

def start_game():    
    
# Display welcome message to the player.
    print("Welcome to Lindsey's Amazing Guessing Game!")
    time.sleep(1)
    play_game = input("Would you like to play? Yes/No  ")

#    while play_game = Yes


# Store a random number as the solution

    # code from https://www.geeksforgeeks.org/python-random-module/ 

    game_solution = int(random.randint(1, 20))
    
# Continuously prompt the player for a guess
    player_guess = input("I've chosen a number between 1 and 20. What number do you think I picked?  ")
    player_guess = int(new_guess)

#if guess is greater than the solution, display "it's too low"
# save attempt number to a list
    if player_guess > game_solution:
        # append guess to guess_list
        print("No, too low.")
        #num_of_guesses += 1
        input("Guess again: ".format(player_guess))


#if guess is less than the solution, display "it's too high"
# save attempt number to a list
    elif player_guess < game_soltuion:
        # append guess to guess_list
        #num_of_guesses += 1
        ## don't forget you have to add the acutal guess too!!
        print("No, too high.")
        input("Guess again: ".format(player_guess))

guess_list.append(guess_list)

#if guess is correct, display player's name and "got it"  
# --> pretty sure this isn't the right way to do it
#while player_guess == game_solution:
#        print("You guessed it!")
#        break

# ask if they want to play again
play_again = input("Would you like to play again? yes/no  ")
    #if play_again == yes
    #return to beginning
    
    #else
# display number of guesses made to get the answer        
      #  print("Thanks for playing! You made {} guesses.".format(len(num_of_guesses))
      
# at the end of the game, display 1) their number of attempts, 2) the mean, median, and mode of the saved attempts list

median_guess = median(num_of_guesses)
print(f"The median guess was: {median_guess}")

mean_guess = mean(num_of_guesses)
print(f"The mean guess was: {mean_guess}")

mode_guess = mode(num_of_guesses)
print(f"The mode guess was: {mode_guess}")
      



# Kick off the program by calling the play_game function.


