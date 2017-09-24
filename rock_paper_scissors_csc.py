# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 21:29:36 2016

@author: gbondos
"""
######################################################################
#TODO: Author: Saffa M. Gbondo 
#TODO: username: GbondoS@berea.edu
#
# Assignment: A2
# Purpose: As a class demonstration of nested if statements
# using multiple elif keywords
######################################################################
# Acknowledgements:
#   This program utilizes inspiration for the timey... wimey stuff
#   from Doctor Who: http://en.wikipedia.org/wiki/Doctor_Who and
#   quotes from http://www.brainyquote.com/quotes/topics/topic_computers.html
######################################################################
import random



print("Lets play Rock, paper and scissors\n")
print("Choose either: Rock; Paper; Scissors; Spock; Lizard \n ")

name=raw_input("What is your name? \t Enter your name:")
print("Welcome %s to the rock, paper and scissors game"%name)
user_input = raw_input("Either choose, rock, paper, scissors, lizard, or spock:")


computer_choice = random.random()

if computer_choice <= .20:
    computer_choice = "rock"
elif computer_choice <=.40:
    computer_choice ="paper"
elif computer_choice <=.60:
    computer_choice ="scissors"
elif computer_choice <=.80:
    computer_choice ="spock"
elif computer_choice <=.99:
    computer_choice ="lizard"

    

def rock_paper_scissors_game(first,second):
    if first==second:
        print"You chose", first
        print"Computer chose", second
        print"it is a tie"
    elif first == "scissors":
        if second == "paper":
            print "You chose", first
            print "computer chose",second
            print ("Yes, you win %s!!! Scissors cut paper"%name)
        else:
            print "You chose", first
            print "computer chose",second
            print ("You lose %s! Scissors only cut paper and decapitate lizard"%name)
    elif first == "paper":
        if second == "rock":
            print "You chose", first
            print "computer chose",second
            print ("Yes, you win %s!!! Paper covers rock"%name)
        else:
            print "You chose", first
            print "computer chose",second
            print ("You lose %s!  Paper only covers rock and disproves Spock"%name)
    elif first == "rock":
        if second == "lizard":
            print "You chose", first
            print "computer chose",second
            print ("Yes, you win %s!!! Rock crushes lizard"%name)
        else:
            print "You chose", first
            print "computer chose",second
            print ("You lose %s! Rock only crushes lizard and scissors"%name)
    elif first == "lizard":
        if second == "spock":
            print "You chose", first
            print "computer chose",second
            print ("Yes, you win %s!!! Lizard poisons Spock"%name)
        else:
            print "You chose", first
            print "computer chose",second
            print ("You lose %s! Lizard only poisons Spock and eats paper"%name)
    elif first == "spock":
        if second == "scissors":
            print "You chose", first
            print "computer chose",second
            print ("Yes, you win %s!!! Spock smashes scissors"%name)
        else:
            print "You chose", first
            print "computer chose",second
            print ("You lose %s! Spock only smashes scissors and vaporizes rock"%name)
    elif first == "scissors":
        if second == "lizard":
            print "You chose", first
            print "computer chose",second
            print ("Yes, you win %s!!! Scissors decapitate lizard"%name)
        else:
            print "You chose", first
            print "computer chose",second
            print ("you lose %s! Scissors only decapitate lizard and cut paper"%name)
    elif first == "lizard":
        if second == "paper":
            print "You chose", first
            print "computer chose",second
            print ("Yes, you win %s!!! Lizard eats paper"%name)
        else:
            print "You chose", first
            print "computer chose",second
            print ("You lose %s! Lizard only eats paper and poisons spock"%name)
    elif first == "paper":
        if second == "spock":
            print "You chose", first
            print "computer chose",second
            print ("Yes, you win %s!!! Paper disproves spock"%name)
        else:
            print "You chose", first
            print "computer chose",second
            print ("You lose %s! Paper only disproves spock and covers rock"%name)
    elif first == "spock":
        if second == "rock":
            print "You chose", first
            print "computer chose",second
            print ("Yes, you win %s!!! Spock vaporizes rock"%name)
        else:
            print "You chose", first
            print "computer chose",second
            print ("You lose %s! Spock only vaporizes rock and smashes scissors"%name)
    elif first == "rock":
        if second == "scissors":
            print "You chose", first
            print "computer chose",second
            print ("Yes, you win %s!!! Rock crushes scissors"%name)
        else:
            print "You chose", first
            print "computer chose",second
            print ("You lose %s Rock only crushes scissors and lizard "%name)
            
rock_paper_scissors_game(user_input, computer_choice)
