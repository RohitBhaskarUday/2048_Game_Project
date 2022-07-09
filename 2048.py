#Starting with Logics



import random  #to get a random value. We use random Library.
def start_the_game():
    Matrix=[]               #Matrix
    for i in range(4):
        Matrix.append([0]*4)  #4 times We will append list of 0, 2D list with 0 initially.
    return Matrix

def add_new_2(Matrix):  #Adding new 2 to the Matrix
    
    r = random.randint(0,3)
    c = random.randint(0.3)

    while Matrix[r][c]!=0:
        r = random.randint(0,3)
        c = random.randint(0,3)


    Matrix[r][c]=2


