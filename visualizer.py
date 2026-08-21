import matplotlib.pyplot as plt
import numpy as np 
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

root = tk.Tk()
root.title('Gauss-Seidel Solver')
root.geometry('900x500')
mainframe = ttk.Frame(root, padding=(20,20,20,20))
mainframe.grid(column=0, row=0, sticky='nwes')

equations = tk.StringVar()
unknowns = tk.StringVar()

# both of these are StringVar matrices which means you'll have to get() the values from, say, coeff_matrix[i][j]
coeff_matrix = []
aug_matrix = []

custom_font = tkFont.Font(family='Courier', size=20)

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
    
def print_system():
    eqns = int(equations.get())
    unns = int(unknowns.get())
    
    # parent frame for frames of terms in system
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
            
printer = tk.Button(mainframe, text='Print System', command = print_system, font='Courier 20 bold')
printer.configure(background='light gray')
printer.grid(column=1,row=3,sticky='e')

debug = tk.Button(mainframe, text='debug', command = print_debug, font='Courier 20 bold')
debug.configure(background='light gray')
debug.grid(column=2,row=3,sticky='e')

output = tk.Button(mainframe, text='output to csv', command = to_csv, font='Courier 20 bold')
output.configure(background='light gray')
output.grid(column=3,row=3,sticky='e')

xpoints = np.array([1,8, 6])
ypoints = np.array([3,-4, 4])

#plt.plot(xpoints, ypoints)
#plt.show()

root.mainloop()



