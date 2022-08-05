# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 12:51:28 2022

@author: DELL

Our approach for solving nQueen will be to place queens row-wise order.
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
        return True

    
    # lets iteratively place queens in each column of given row
    for col in range(n):
        if isSafe(row, col):
            board[row][col] = 'Q'
            # as soon as we place a queen in a row we move to next row recursively..
            if(nQueen(row + 1)):
                return True
            board[row][col] = '-'
    return False

# allBoards = []
n = 4 #int(input('Enter the size of the board'))
board = [['-' for _ in range(n)] for _ in range(n)]
print(nQueen(0))


