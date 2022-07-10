#Starting with Logics

import random #to get a random value. We use random Library.

def start_the_game():
    Matrix = []          #Creation of the Matrix
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

#Compression. that is compress the non-zero part to one side.

def compress(Matrix):
    changed = False
    new_Matrix = [] #Create a new Matrix now.
    for i in range(4):
        new_Matrix.append([0]*4)

    for i in range(4):  #Move the non-zero values to the left side.
        pos = 0         #using a position variable to which the non-zero value should be moved.
        for j in range(4):
            if Matrix[i][j] != 0:
                new_Matrix[i][pos] = Matrix[i][j]
                if j!=pos:
                    changed = True
                pos+=1
    
    return new_Matrix, changed
        
#Now, Merge the values which are same values residing consecutively.

def merge(Matrix):
    changed = False
    for i in range(4): # here we multiply the consecutive elements and replace the position with 0.
        for j in range(3):
            if Matrix[i][j] == Matrix[i][j+1] and Matrix[i][j]!=0:
                changed = True
                Matrix[i][j] = Matrix[i][j]*2
                Matrix[i][j+1] = 0
    
    return Matrix, changed

#Reversing the matrix
def reverse(Matrix):  #Dry run with a random example and analyze.
    new_Matrix = []
    for i in range(4):
        new_Matrix.append([]) #we append the no of rows in the list
        for j in range(4): # we iterate through each column and then
            new_Matrix[i].append(Matrix[i][4-j-1]) #we add the value of the matrix.
    
    return new_Matrix

#Now, Transposing the Matrix we have
def transpose(Matrix):  #Dry run with a random example then you will be clear.
    new_Matrix=[]
    for i in range(4):
        new_Matrix.append([])
        for j in range(4):
            new_Matrix[i].append(Matrix[j][i])

    return new_Matrix

#Move left. j-th was compared with j-th + 1 
def move_left(grid):  #grid means a 2D Matrix here.
    new_grid,changed1 = compress(grid)  #changed is maintained to check whether
    new_grid,changed2 = merge(new_grid) #any compression or merging has happened
    changed = changed1 or changed2      #or not.
    new_grid,temp = compress(new_grid)
    return new_grid, changed

#Move_right. j-th and j-th + 1 is compared. so,
def move_right(grid):   #visualize this
    reversed_grid = reverse(grid) #reverse the matrix and then apply left logic
    new_grid,changed1 = compress(reversed_grid)
    new_grid,changed2 = merge(new_grid)
    changed  = changed1 or changed2
    new_grid,temp = compress(new_grid)
    final_grid = reverse(new_grid)
    return final_grid, changed

#move_up. i-th and i-th + 1 is compared. so transpose first.
def move_up(grid):    
    transposed_grid = transpose(grid) #here the logic is transpose,
    new_grid,changed1 = compress(transposed_grid)
    new_grid,changed2 = merge(new_grid)  #apply the left logic
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    final_grid = transpose(new_grid) #and then transpose again.
    return final_grid, changed

#move_down i-th + 1 and i-th is compared. 
def move_down(grid):
    transposed_grid = transpose(grid)  #here transpose the grid
    reversed_grid = reverse(transposed_grid) #reverse the grid
    new_grid,changed1 = compress(reversed_grid)  #apply the left logic
    new_grid,changed2 = merge(new_grid)
    changed = changed1 or changed2
    new_grid,temp = compress(new_grid)
    final_reverse_grid = reverse(new_grid) #reverse back the reversed.
    final_grid = transpose(final_reverse_grid) #then transpose again.
    return final_grid, changed

#Now take a sample grid and perform operations accordingly.

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
