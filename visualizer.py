import matplotlib.pyplot as plt
import numpy as np 
import tkinter as tk
import csv
import subprocess
import random
from tkinter import ttk
import tkinter.font as tkFont

root = tk.Tk()
root.title('Convergence Visualizer')
root.geometry('900x500')
mainframe = ttk.Frame(root, padding=(20,20,20,20))
mainframe.grid(column=0, row=0, sticky='nwes')

equations = tk.StringVar()
unknowns = tk.StringVar()

# both of these are StringVar matrices which means you'll have to get() the values from, say, coeff_matrix[i][j]
coeff_matrix = []
aug_matrix = []

custom_font = tkFont.Font(family='Courier', size=10)

ttk.Label(mainframe, text='Number of equations:', font=custom_font).grid(column=1,row=1,sticky='e')
ttk.Entry(mainframe, textvariable = equations, width=4, font=custom_font).grid(column=2,row=1, sticky='w')
ttk.Label(mainframe, text='Number of unknowns:', font=custom_font).grid(column=1,row=2,sticky='e') 
ttk.Entry(mainframe, textvariable=unknowns, width=4, font=custom_font).grid(column=2,row=2,sticky='w')

mainframe.rowconfigure(4, minsize=20)

# makes a frame for each term in each equation of the system. all such frames are inside the parent frame.
def make_term_frame(parent, c, r, label_text):
    
    # frame for entry and label of one term
    frame = ttk.Frame(parent, padding = (5,5,5,5))
    frame.grid(column=c, row=r, sticky='w')
    
    # whatever will be given in the entry
    var = tk.StringVar()
    # entry for coefficients
    entry = ttk.Entry(frame, width = 4, textvariable=var, font=custom_font)
    entry.grid(column=0, row=0, sticky='e')
    
    # labels x1, x2, ...
    ttk.Label(frame, text = label_text, font = custom_font).grid(column=1,row=0, sticky='w')
    
    # return for storage of elements of matrix
    return var
    
system_frame = None
def print_system():
    eqns = int(equations.get())
    unns = int(unknowns.get())
    
    
    
    # parent frame for frames of terms in system
    global system_frame
    
    if system_frame != None:
        system_frame.destroy()
    
    system_frame = ttk.Frame(mainframe, padding = (10,10,10,10))
    system_frame.grid(column=1, row=5, sticky='w')
    
    
    for i in range(eqns):
        current_row = []
        for j in range(unns):
            # if we are at the end of the row, print with an equal sign, else print with a plus.
            text = f'x{j+1}=' if j == unns-1 else f'x{j+1}+'
            
            # gets the current StringVar for storage in coeff_matrix
            var = make_term_frame(system_frame, j+1, 5+i, text)
            
            # append to the 1d current_row to later append to coeff_matrix
            current_row.append(var)
            
        # add current row to coeff_matrix
        coeff_matrix.append(list(current_row))
        
        # entry for vector b elements (in Ax=b)
        bvar = tk.StringVar()
        ttk.Entry(system_frame, width=4, textvariable=bvar, font=custom_font).grid(column=(unns+1), row=(5+i), sticky='e')
        current_row.append(bvar)
        
        # appending the full row to augmented matrix [A|b]
        aug_matrix.append(list(current_row))

def randomize():
    eqns = int(equations.get())
    unns = int(unknowns.get())
    
    for i in range(len(aug_matrix)):
        for j in range(len(aug_matrix[i])):
            if(i != j):
                aug_matrix[i][j].set(str(random.randint(-100,100)))
    
    for i in range(len(aug_matrix)):
        sum = 0
        for j in range(len(aug_matrix[i])):
            if(j != i):
                sum = sum + abs(int(aug_matrix[i][j].get()))
        aug_matrix[i][i].set(str(sum + random.randint(1,10)))

def to_csv():
    # output coeff_matrix to csv file
    with open('Data/coeff_matrix.csv', 'w') as file:
        for i in range(len(coeff_matrix)):
            for j in range(len(coeff_matrix[i])):
                file.write(f'{coeff_matrix[i][j].get()}' if j == len(coeff_matrix[i])-1 else f'{coeff_matrix[i][j].get()},')
            file.write('\n')
            
    # output aug_matrix to csv file
    with open('Data/aug_matrix.csv', 'w') as file:
        for i in range(len(aug_matrix)):
            for j in range(len(aug_matrix[i])):
                file.write(f'{aug_matrix[i][j].get()}' if j == len(aug_matrix[i])-1 else f'{aug_matrix[i][j].get()},')
            file.write('\n')
    
    # output orders of coeff_matrix (pxq) and aug_matrix (rxs) to csv
    # in the form p,q,r,s
    eqns = int(equations.get())
    unns = int(unknowns.get())
    with open('Data/orders.csv', 'w') as file:
        file.write(f'{eqns},{unns},{eqns},{unns + 1}')

def print_debug():
    print('coeff matrix:')
    for i in range(len(coeff_matrix)):
        for j in range(len(coeff_matrix[i])):
            print(coeff_matrix[i][j].get(), end='\t')
        print()
    
    print('augmented matrix [A|b]: ')
    for i in range(len(aug_matrix)):
        for j in range(len(aug_matrix[i])):
            print(aug_matrix[i][j].get(), end='\t')
        print()
        


def visualize():
    plt.close()
    subprocess.run(["/mnt/c/users/rajdeep deka/documents/code/jngs visualizer/iterator"])
    x_vals = []
    with open('Data/solution.csv', 'r') as file:
        solreader = csv.reader(file, delimiter=',')
        for r in solreader:
            x_vals.append([float(v) for v in r])
        for r in x_vals:
            print(r)
        print()
            
    x_vals=np.array(x_vals)
    iterations = np.arange(len(x_vals))
    
    for j in range(x_vals.shape[1]):
        plt.plot(iterations, x_vals[:, j], label=f'x{j+1}')
    
    plt.xlabel('Iteration')
    plt.ylabel('value')
    plt.legend()
    plt.title('convergence')
    plt.show()
    
printer = tk.Button(mainframe, text='Print System', command = print_system, font=custom_font)
printer.configure(background='light gray')
printer.grid(column=1,row=3,sticky='e')

""" for debugging purposes
|debug = tk.Button(mainframe, text='debug', command = print_debug, font='Courier 20 bold')
debug.configure(background='light gray')
debug.grid(column=2,row=3,sticky='e')"""

iteratebutton = tk.Button(mainframe, text='iterate', command = visualize,  font=custom_font)
iteratebutton.configure(background='light gray');
iteratebutton.grid(column=3, row=3, sticky='w')

output = tk.Button(mainframe, text='output to csv', command = to_csv, font=custom_font)
output.configure(background='light gray')
output.grid(column=2,row=3,sticky='e')

grand = tk.Button(mainframe, text='randomize', command = randomize,  font=custom_font)
grand.configure(background='light gray');
grand.grid(column=3, row=2, sticky='w')


root.mainloop()



