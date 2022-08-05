# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 13:44:58 2022

@author: Purushotam Sangroula

Our approach for solving nQueen will be to place queens row-wise order.
We will find all possible solutions.
"""



def printBoard():
    global board, n
    
    for row in board:
        print( " | ".join(row) )

def isSafe(row,col):
    """
    We check if some queen has already been placed in:
        - vertically upward position
        - diagonally upward directions 
        - hence, total 3 directions check
        - it is assured that no 2 queens are place in same row
    """
    global n
    r,c = row, col
     
    # vertical check
    while r >= 0:
        if board[r][c] == 'Q':
            return False
        r -= 1

    # left diagonal check
    r = row
    while r>=0 and c>=0:
        if board[r][c] == 'Q':
            return False
        r -= 1
        c -= 1
        
    # right diagonal check
    r,c = row, col
    while r>=0 and c<n:
        if board[r][c] == 'Q':
            return False
        r -= 1
        c += 1
    return True
    
def nQueen(row):
    """
    We place the queens row wise. 
    Terminating condition =>
    if we place queens in all rows. i.e. if row == n => we already placed all the queens.
    """
    global board, n

    if row == n:
        print("You have successfully placed the queens.")
        printBoard()
        return True   # This return is necessary to stop array index out of range otherwise no significant meaning in the algorithm.

    
    # lets iteratively place queens in each column of given row
    for col in range(n):
        # printBoard()
        # print()
        if isSafe(row, col):
            board[row][col] = 'Q'
            # as soon as we place a queen in a row we move to next row recursively..
            # if(nQueen(row + 1)):
            #     return True
            nQueen(row+1)
            board[row][col] = '-'
            
    return False

# allBoards = []
n = 6 #int(input('Enter the size of the board'))
board = [['-' for _ in range(n)] for _ in range(n)]
print(nQueen(0))


