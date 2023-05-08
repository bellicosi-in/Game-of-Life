import os
import numpy as np
from numpy.typing import NDArray as arr

# Define a function to render the current state to the terminal

def render(board:arr[np.int64])->None:
    # clear the terminal
    os.system('cls' if os.name=="nt" else "clear")
    for i in board:
        for j in i:
            if j:
                print("*",end="\t")
            else:
                print(" ",end="\t")
        if i is not board[-1]:

            print("")