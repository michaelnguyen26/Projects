#!/usr/bin/env python
# coding: utf-8

import random as rd 
 
games = 0
wins = 0
loss = 0

bound_left = int(input("Enter a left bound: "))
bound_right = int(input("Enter a right bound: "))

enable_cheats = 'asdf'

while(enable_cheats != 'YES' or enable_cheats != 'NO'):
    enable_cheats = str(input("Enable Cheats? (Yes/No): "))
    enable_cheats = enable_cheats.upper()

    if enable_cheats == 'YES' or enable_cheats == 'NO':
        break


############ GAME BEGINS #############  

while(True):
    
    rand_gen = rd.randint(bound_left,bound_right)    #Random integer from user decision changes constantly with loop
    
    if enable_cheats == 'YES':
        print("\n\nRandom Number Generated (Cheats Enabled):", rand_gen,"\n")
        
    guess_input = int(input("Guess a whole number from {0}-{1} or enter -1 to quit: ".format(bound_left,bound_right)))
    
    if guess_input == -1:
        win_rate = (wins/games)*100
        loss_rate = (loss/games)*100
        diff_bounds = (bound_right-bound_left)+1 #includes all numbers in the range
        odds = (1/diff_bounds)*100
        
        print("\n\n-------- Score for Bounds {0}-{1} --------".format(bound_left,bound_right))
        print("Odds of Choosing the Correct Number: {0:.3f}%".format(odds))
        print("Total Games: ", games)
        print("Total Wins:  ", wins)
        print("Total Losses:", loss)
        print("Win Rate: {0:.2f}%".format(win_rate))
        print("Loss Rate: {0:.2f}%".format(loss_rate))
        print("----------------------------------------".format(bound_left,bound_right))
        break
    
    games+=1  #Increment number of games played here 
    
    if guess_input == rand_gen:
        print("\n\n----------- Match -----------")
        print("Computer Guessed: {0}".format(rand_gen))
        print("You Guessed: {0}".format(guess_input))
        print("-----------------------------\n")
        
        wins+=1
   
    elif guess_input != rand_gen: 
        print("\n------------------------------- Try Again -----------------------------------")
        print("Your number did not match. The computer guessed the number {0}.".format(rand_gen))
        print("-----------------------------------------------------------------------------\n")
        
        loss+=1
