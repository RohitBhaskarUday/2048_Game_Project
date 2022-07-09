#Starting with Logics

import random
from re import M

from markupsafe import Markup  #to get a random value. We use random Library.

def start_the_game():
    Matrix=[]          #Creation of the Matrix
    for i in range(4):
        Matrix.append([0]*4)  #4 times We will append list of 0, 2D list with 0 initially at all positions.
    return Matrix

def add_new_2(Matrix):  #Adding new 2 to the Matrix
    
    r = random.randint(0,3)
    c = random.randint(0,3)  #Generate Random positions 

    while Matrix[r][c]!=0: #if 0 is not present at an empty space
        r = random.randint(0,3) #you would again generate random numbers 
        c = random.randint(0,3) #and check whether there is 0 or not.

    Matrix[r][c]=2 #when there is 0 at a random place we will add 2 to that place in the matrix

#Current State of the game
# There can be 3 possibilites 
# 1) Won
# 2) Lost 
# 3) Game not over

def get_current_state(Matrix):
    
    #WON

    for i in range(4):    #you will check each position
        for j in range(4): # inside the matrix
            if (Matrix[i][j]==2048): #if at any position has 2048 
                return "WON" #That Means you have won the game
    
    #GAME NOT OVER

    #if there is 0 present in any position in the matrix. (Empty Position)
    #That means, you are still in the game.

    for i in range(4):
        for j in range(4):
            if (Matrix[i][j]==0):
                return "GAME NOT OVER"

    #Even at any point if the elements are equal consecutive in horizontally or vertically
    #Check after the Edge Case also.

    for i in range(3):  #3 because the matrix can be out of bound. (Edge Case)
        for j in range(3): #here too the matrix can be out of bound.
            if (Matrix[i][j] == Matrix[i+1][j] or Matrix[i][j] == Matrix[i][j+1]):
                return "GAME NOT OVER"

    #Now checking for last row, whether there are any consecutive in horizontally or vertically
    
    for j in range(3):
        if Matrix[3][j] == Matrix[3][j+1]:
            return "GAME NOT OVER"

    #Now checking the same for last Column.

    for i in range(3):
        if Matrix[i][3] == Matrix[i+1][3]:
            return "GAME NOT OVER"
    
    #If any of the above satisfy that means we have lost the game.
    # we return LOST.

    return "LOST"


