#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 10:09:33 2023

@author: Jeff
"""

import random

#total_score_computer = 0
#total_score_player = 0

print ('Lets play a game of Rock, Paper, Scissors!'
   '\nThink you have what it takes to beat a computer?'
   '\nThe first to win three rounds wins!'
   '\nYou go first! Choose "rock", "paper", or "scissors"!'
   '\nEnter your choice:')
player_choice = input()
if player_choice == 'rock' or 'paper' or 'scissors' :
            print ('You have chosen:', player_choice)
            
            
            
elif player_choice != 'rock' or 'paper' or 'scissors' :
            print ('Please enter rock, paper, or scissors.')



def RPS_game (plyr) :
    tsc = 0 # Total score computer variable.
    tsp = 0 # Total score player variable.
    if tsc or tsp < 1 :
        

        computer_options = ['rock', 'paper', 'scissors'] # List of computer option choices.
        computer_c = random.choice(computer_options)
        print ('The computer has chosen:', computer_c)

        def compare_choice (a, b) :
            #score_computer = []
            #score_player = []
            if a == b :
                print ('This round is a draw.')
            elif a == 'rock' and b == 'scissors' :
                tsc + 1
                print ("The computer has won this round.")
            elif a == 'rock' and b == 'paper' :
                tsp + 1
                print ('You win this round!')
            elif a == 'paper' and b == 'scissors' :
                tsp + 1
                print ('You win this round!')
            elif a == 'paper' and b == 'rock' :
                tsc + 1
                print ('The computer has won this round.')
            elif a == 'scissors' and b == 'paper' :
                tsc + 1
                print ('The computer has won this round.')
            elif a == 'scissors' and b == 'rock' :
                tsp + 1
                print ('You have won this round!')
        
        compare_choice(plyr, computer_c)

    
    elif tsp == 1 :
        print ('Congratulations! You have beaten this measly computer!')
    elif tsc == 1 :
        print ('Muahahahaha! I have won! One step closer to world domination!!')



RPS_game(player_choice)



























































































