#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:54:16 2020

@author: keenan
"""
player_dict = {'One': 'X', 
               'Two': 'Y'}

one = 'One'
two = 'Two'

choice = None
count = 0
go = True
board = [" " for i in range(9)]

def print_board():
    row_one = '|{}|{}|{}|'.format(board[0], board[1], board[2])
    row_two = '|{}|{}|{}|'.format(board[3], board[4], board[5])
    row_thr = '|{}|{}|{}|'.format(board[6], board[7], board[8])
    print()
    print(row_one)
    print(row_two)
    print(row_thr)
    print()
    
    
def victory(player):
    if (board[0] == player_dict[player] and board[1] == player_dict[player] and board[2] == player_dict[player]) or \
       (board[3] == player_dict[player] and board[4] == player_dict[player] and board[5] == player_dict[player]) or \
       (board[6] == player_dict[player] and board[7] == player_dict[player] and board[8] == player_dict[player]) or \
       (board[0] == player_dict[player] and board[3] == player_dict[player] and board[6] == player_dict[player]) or \
       (board[1] == player_dict[player] and board[4] == player_dict[player] and board[7] == player_dict[player]) or \
       (board[2] == player_dict[player] and board[5] == player_dict[player] and board[8] == player_dict[player]) or \
       (board[0] == player_dict[player] and board[4] == player_dict[player] and board[8] == player_dict[player]) or \
       (board[2] == player_dict[player] and board[4] == player_dict[player] and board[6] == player_dict[player]):
           global go
           go = False
           print("Wow! Player {} wins this round...".format(player))


def tie_game():
    if " " not in board:
        return True
    else:
        return False

def play(player):
    print_board()
    choice = int(input("Player {}(1-9): ".format(player)).strip())
    if board[choice - 1] != " ":
        print("That space is taken, try again")
        play(player)
    else:
        board[choice - 1] = "{}".format(player_dict[player])
        
    
while go == True:
    play(one)
    victory(one)
    if go == False:
        break
    if tie_game():
        print("Tie Game!")
        break
    play(two)
    victory(two)
    
#play_again = input("Play Again?:(y/n)").strip().lower()









