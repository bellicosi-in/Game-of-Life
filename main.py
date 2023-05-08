import time
from typing import List,Tuple
import numpy as np
from numpy.typing import NDArray as arr

from .render import render


# Define a random state to begin with using numpy arrays

def random_state(board_height:int,board_width:int)->arr[np.int64]:
    board=np.random.choice([0,1],size=(board_height,board_width))
    return board




# To calculate the coordinates of the possible neighbors

def next_coordinates(row:int,col:int)->List[Tuple(int,int)]:
    # calculate the possible coordinates
    coord=[]
    for i in range(row-1,row+2):
        for j in range(col-1,col+2):
            if i==row and j==col:
                continue
            coord.append((i,j))
    return coord

# To calculate the alive and death scenario of the current cell

def calculate_next_state(live_neighbor:int)->int:
    if live_neighbor==0 or live_neighbor==1 or live_neighbor>3:
        return 0
    if live_neighbor==3:
        return 1

# to calculate the next state given the current state

def next_board_state(board:arr[np.int64])->arr[np.int64]:
    new_state=np.zeros((board.shape[0],board.shape[1]))
    for row in range(board.shape[0]):
        
        for column in range(board.shape[1]):
            coord=next_coordinates(row,column)
            live_neighbors=0
            
            for i,j in coord:
                if i==board.shape[0]:
                    i=-1
                if j==board.shape[1]:
                    j=-1

                if board[i,j]:
                    live_neighbors+=1
            if live_neighbors!=2:
                new_state[row,column]=calculate_next_state(live_neighbors)
            else:
                new_state[row,column]=board[row,column]
    return new_state



#  function to infintely run the simulation

def run_forever(row:int,col:int)-> None:
    board=random_state(row,col)
    render(board)
    while True:
        time.sleep(0.5)
        board=next_board_state(board)
        render(board)
        



            
            
if __name__=="__main__":
    run_forever(10,10)

