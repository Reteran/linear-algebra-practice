import numpy as np
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Matrix Multiplier")
windowFrame = ttk.Frame(root, padding=(20,20,20,20))
windowFrame.grid(column=0,row=0,sticky=(N,W,E,S))

r1 = StringVar()
r2 = StringVar()
c1 = StringVar()
c2 = StringVar()

def syncr2(*args):
    r2.set(c1.get())
c1.trace_add("write", syncr2)

arr1Vars = []
arr2Vars = []
prodVars = []
entryWidgets = []

def clearMatrix():
    for w in entryWidgets:
        w.destroy()
    entryWidgets.clear()
    
def createMatrixInput(*args):
    #pass
    #Matrix 1 input
    clearMatrix()
    arr1Vars.clear()
    arr2Vars.clear()
    
    rows1, columns1 = int(r1.get()), int(c1.get())
    rows2, columns2 = int(r2.get()), int(c2.get())
    
    lbl1 = ttk.Label(windowFrame, text="Matrix A:")
    lbl1.grid(column=1, row=7, sticky=E)
    entryWidgets.append(lbl1)
    
    for i in range(rows1):
        row_vars = []
        for j in range(int(columns1)):
            var = StringVar(value="")
            e = ttk.Entry(windowFrame, textvariable=var, width=4)
            e.grid(column=(2+j), row=(7+i), sticky=(W,E))
            entryWidgets.append(e)
            row_vars.append(var)
        arr1Vars.append(row_vars)
        
    spaceRow = 7 + rows1
    windowFrame.rowconfigure(spaceRow, minsize=20)
    
    m2LabelRow = 7 + rows1 + 2
    lbl2 = ttk.Label(windowFrame, text="Matrix B:")
    lbl2.grid(column=1, row=m2LabelRow, sticky=E)
    entryWidgets.append(lbl2)
    
    for i in range(rows2):
        row_vars = []
        for j in range(int(columns2)):
            var = StringVar(value="")
            e = ttk.Entry(windowFrame, textvariable=var, width=4)
            e.grid(column=(2+j), row=(m2LabelRow+i), sticky=(W,E))
            entryWidgets.append(e)
            row_vars.append(var)
        arr2Vars.append(row_vars)
        
    spaceRow2 = m2LabelRow+rows2
    windowFrame.rowconfigure(spaceRow2, minsize=20)
    
    global prodLabelRow
    prodLabelRow = spaceRow2 + 1
    
    lblprod = ttk.Label(windowFrame, text="Product (AB):")
    lblprod.grid(column=1, row=prodLabelRow, sticky=E)
    entryWidgets.append(lblprod)
    
prodLabelRow = 0
prodWidgets = []

def clearProductMatrix():
    for w in prodWidgets:
        w.destroy()
    prodWidgets.clear()

def multiply(*args):
    clearProductMatrix()
    prodVars.clear()
    
    rows1, columns1 = int(r1.get()), int(c1.get())
    rows2, columns2 = int(r2.get()), int(c2.get())
    
    for i in range(rows1):
        row_vars = []
        for j in range(columns2):
            rowSum = 0
            var = StringVar()
            for k in range(columns1):
                rowSum += int(arr1Vars[i][k].get()) * int(arr2Vars[k][j].get())
            var.set(rowSum)
            
            rlbl = ttk.Label(windowFrame, textvariable = var)
            rlbl.grid(column=2+j,row=prodLabelRow+i, sticky=(W,E))
            entryWidgets.append(rlbl)
            
            row_vars.append(var)
        prodVars.append(row_vars)
        


ttk.Label(windowFrame, text="Matrix 1 rows:").grid(column=1, row=1, sticky=E)
ttk.Label(windowFrame, text="Matrix 1 columns:").grid(column=1, row=2, sticky=E)
ttk.Label(windowFrame, text="Matrix 2 rows:").grid(column=1, row=3, sticky=E)
ttk.Label(windowFrame, text="Matrix 2 columns:").grid(column=1, row=4, sticky=E)

ttk.Entry(windowFrame, textvariable=r1, width=4).grid(column=2, row=1, sticky=(W,E))
ttk.Entry(windowFrame, textvariable=c1, width=4).grid(column=2, row=2, sticky=(W,E))
ttk.Label(windowFrame, textvariable=r2).grid(column=2,row=3,sticky=W)
ttk.Entry(windowFrame, textvariable=c2, width=4).grid(column=2, row=4, sticky=(W,E))

ttk.Button(windowFrame, text="Create Matrix Input", command=createMatrixInput).grid(column=1,row=5,sticky=(N,E))
ttk.Button(windowFrame, text="Multiply", command=multiply).grid(column=2,row=5,sticky=(N,W))

for child in windowFrame.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()