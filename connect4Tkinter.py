import tkinter as tk
import os
import numpy as np
from tabulate import tabulate
import pandas as pd
import time
from termcolor import colored

class Board:
    row=6
    col=7
    board=pd.DataFrame(np.zeros((row,col)), index=[5,4,3,2,1,0])

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
            for j in range(width-1):
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
            if board[a][j]=="":
                k=5
                while board[a][j]=="":
                    time.sleep(0.3)
                    if k == 5:
                        board[a][k]=player
                    else:
                        board[a][k+1]=""
                        board[a][k]=player
                    k-=1
                    self.board.print_board()
                break
            else:
                continue
            

    def launch_game(self,a): #run game loop
        self.board.change_board_values()
        self.board.print_board()
        i=0
        while True:
            try:
                # a=int(input("select column:")) # a is selected column by users
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

board = Board()



window=tk.Tk()
window.title("Tic Tac Toe game")
canvas_board = tk.Canvas (window, bg="blue" , width=1000 , height =1000)
canvas_top = tk.Canvas (window, bg="white" , width=1000 , height =100)

triangle=canvas_top.create_polygon(30, 50,90, 50, 60, 95, fill='white',outline="blue", width=4)
def draw_triangle(event):
    global triangle
    time.sleep(0.05)
    canvas_top.delete(triangle)
    triangle=canvas_top.create_polygon(event.x-30, 50,event.x+30, 50, event.x, 95, fill='white', outline="blue", width=4)

def draw_board(board):
    time.sleep(0.03)
    x=100
    y=600
    for i in range(board.row):
        for j in range(board.col):
            if board.board[j][i]=="":
                canvas_board.create_oval(x-40, y-40, x+40,y+40, fill='white', outline="black", width=2)
            elif board.board[j][i]=="X":
                canvas_board.create_oval(x-40, y-40, x+40,y+40, fill='red', outline="black", width=2)
            else:
                canvas_board.create_oval(x-40, y-40, x+40,y+40, fill='yellow', outline="black", width=2)
            x+=100
        x=100
        y-=100
a=0
board.change_board_values()
draw_board(board)
def launch_game(event,a,board, string):
    start = 60
    end = 140
    for i in range(0,7):
        if event.x>start and event.x<end:
            a=i
            for j in range(6):
                if board.board[a][j]=="":
                    animation_draw(board,a,string)
                    print(board.board[a][j])
                    break
                else:
                    continue
        start += 100
        end += 100
    
player = 0
win_label= tk.Label(window, text= "")
def check_win(board):
    if connect_four.check_win(board, 7, 6):
        win_label.config(text=f"{connect_four.check_win(board, 7, 6)} won!!!")

def input_position(event):
    global a, board, player
    if player%2==0:
        launch_game(event,a,board, "X")
    else:
        launch_game(event,a,board, "O")
    player+=1
    check_win(board.board)
def animation_draw(board,a,player): # animation starts from top of board
        for j in range(6):
            if board.board[a][j]=="":
                k=5
                while board.board[a][j]=="":
                    time.sleep(0.05)
                    if k == 5:
                        board.board[a][k]=player
                        window.update()
                        draw_board(board)
                    else:
                        board.board[a][k+1]=""
                        board.board[a][k]=player
                        window.update()
                        draw_board(board)
                    k-=1
                    os.system("clear")
                    print(board.board)
                break
            else:
                continue
    
window.bind("<Button-1>", input_position)
window.bind("<Motion>", draw_triangle)
win_label.pack(pady= 25)
canvas_top.pack()
canvas_board.pack()
window.mainloop()