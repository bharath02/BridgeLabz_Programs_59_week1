import os
import time
import random
board=[""," "," "," "," "," "," "," "," "," "]
def print_header():
    print("""-------------- Tic Tac Toe --------------------""")
def print_board():
    print("__________")
    print("|"+board[1]+" |"+board[2]+" |"+board[3]+" |")
    print("|__|__|__|")
    print("|"+board[4]+" |"+board[5]+" |"+board[6]+" |")
    print("|__|__|__|")
    print("|"+board[7]+" |"+board[8]+" |"+board[9]+" |")
    print("|__|__|__|")

    
def is_winner(board, Player):
    if((board[1]==Player and board[2]==Player and board[3]==Player)or
       (board[1]==Player and board[4]==Player and board[7]==Player)or
       (board[1]==Player and board[5]==Player and board[9]==Player)or
       (board[2]==Player and board[5]==Player and board[8]==Player)or
       (board[3]==Player and board[6]==Player and board[9]==Player)or
       (board[3]==Player and board[5]==Player and board[7]==Player)or
       (board[4]==Player and board[5]==Player and board[6]==Player)or
       (board[7]==Player and board[8]==Player and board[9]==Player)):
        return True
    else:
        return False
def get_computer_move(board, player):
    for i in range(1,10):
        if(board[i]==" "):
            board[i]=player
            if(is_winner(board, player)):
                return i
            else:
                board[i]=" "
        
    if(board[5]==" "):
        return 5
    
    while True:
        move= random.randint(1,9)
        if(board[move]==" "):
            return move
            break
    
def is_board_full(board):
    if " " in board:
        return False
    else:
        return True
while True:
    os.system("clear")
    print_header()
    print_board()
    # User as X Player 
    choice =input("Please choose as empty space for X.")
    choice=int(choice)
    if(board[choice]==" "):
        board[choice]="X"
    else:
        print("""..............................
                                                Already Printed No Empty Space avaliable chosse another value
                                                                                                                ..........................""")
        time.sleep(2)
        
    if(is_winner(board,"X")):
        os.system("clear")
        print_header()
        print_board()
        print("X Win Congratulations: ")
        break
    
    if(is_board_full(board)):
        print("Tie Match Between X & O")
        break
    
    # Computer as a O Player
    os.system("clear")
    print_header()
    print_board()
    choice=get_computer_move(board,"O")
    if(board[choice]==" "):
        board[choice]="O"
    else:
        print("""..............................
                                                Already Printed No Empty Space avaliable chosse another value
                                                                                                                ..........................""")
        time.sleep(2)
        
    if(is_winner(board,"O")):
        os.system("clear")
        print_header()
        print_board()
        print("O Win Congratulations: ")
        break
        
        if(is_board_full(board)):
            print("Tie Match Between X & O")
            break
