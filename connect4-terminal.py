import os
import numpy as np
from tabulate import tabulate
import pandas as pd
import time
from termcolor import colored


class Board:
    board=pd.DataFrame(np.zeros((6,7)), index=[5,4,3,2,1,0])

    def change_board_values(self):  # change board values from 0 to empty string
        for i in range(7):
            for j in range(6):
                self.board[i][j]=""
        
    def print_board(self):
        print(colored(tabulate(self.board, tablefmt="grid", showindex=False),"green")) #colorful print


class Connect4:
    def __init__(self):
        self.board = Board() # using Board class instance
  
    def check_win(self,board, width, height): #chech winner for all situations
        #horizontally
        for i in range(width-2):
            for j in range(height-1):
                if board[i][j]==board[i+1][j]==board[i+2][j]==board[i+3][j]!="":
                    print(f"{board[i][j]} won!!!")
                    return board[i][j]
                else:
                    continue

        #vertically
        for i in range(height-4):
            for j in range(width):
                if board[j][i]==board[j][i+1]==board[j][i+2]==board[j][i+3]!="":
                    print(f"{board[j][i]} won!!!")
                    return board[j][i]
                else:
                    continue

        #diagonally
        for i in range(width-3):
            for j in range(height-3):
                if board[j][i]==board[j+1][i+1]==board[j+2][i+2]==board[j+3][i+3]!="":
                    print(f"{board[j][i]} won!!!")
                    return board[j][i]
                else:
                    continue
                
        for i in range(width-3):
            for j in range(height-2,2,-1):
                if board[i][j]==board[i+1][j-1]==board[i+2][j-2]==board[i+3][j-3]!="":
                    print(f"{board[j][i]} won!!!")
                    return board[j][i]
                else:
                    continue


    def animation_print(self,board,a,player): # animation starts from top of board
        for j in range(8):
            if board[a-1][j]=="":
                k=5
                while board[a-1][j]=="":
                    time.sleep(0.3)
                    if k == 5:
                        board[a-1][k]=player
                    else:
                        board[a-1][k+1]=""
                        board[a-1][k]=player
                    k-=1
                    os.system("clear")
                    self.board.print_board()
                break
            else:
                continue
            

    def launch_game(self): #run game loop
        self.board.change_board_values()
        self.board.print_board()
        i=0
        while True:
            try:
                a=int(input("select column:")) # a is selected column by users
                if a <8 and a>0:
                    if i%2==0:
                        self.animation_print(self.board.board,a, f"{colored('X', 'red')}")
                    else:
                        self.animation_print(self.board.board,a, f"{colored('O', 'blue')}")
                    i+=1
                    os.system('clear')
                else:
                    os.system("clear")
                    print("write numbers: 0-7") #entering numbers which are out of range
                self.board.print_board()
                print(f"\n {'X' if i%2==0 else 'O'} turn \n")
                
                if self.check_win(self.board.board,6,7):
                    break
            except: # entering string or float 
                os.system("clear")
                print("invalid input")
                self.board.print_board()
        self.start_again()


    def start_again(self): # when game ends, restart or close
        question = input("Do you want to play again? (y/n): ")
        if question == "y":
            self.launch_game()
        elif question == "n":
            print("Goodbye!")
        else:
            print("write y(yes) or n(no).")
            self.start_again()


connect_four=Connect4() # using Connect4 class instance
connect_four.launch_game()
