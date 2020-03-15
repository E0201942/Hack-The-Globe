# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 03:16:46 2020

@author: alden
"""
def getPD(filname):
    # images are 48x48
    # N = 35887
    colnames = []
    coldata = []
    first = True
    count = 1
    colnames = ["Items", "Quantity"]
            
    for line in open(filname):
            row = line.split(',')
            try:
                coldata.append(row)
            except:
                break
    df = pd.DataFrame(coldata, columns = colnames)
    return df
def getData(filname):
    # images are 48x48
    # N = 35887
    colnames = []
    coldata = []
    first = True
    count = 1
    colnames = ["Items", "Quantity"]
            
    for line in open(filname):
            row = line.split(',')
            try:
                coldata.append(row)
            except:
                break
    return coldata

def knapSack(W, wt, val, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 
def printknapSack(W, wt, val, n): 
    result = []
    K = [[0 for w in range(W + 1)] for i in range(n + 1)] 
              
    # Build table K[][] in bottom 
    # up manner 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i - 1] <= w: 
                K[i][w] = max(val[i - 1]  
                  + K[i - 1][w - wt[i - 1]], 
                               K[i - 1][w]) 
            else: 
                K[i][w] = K[i - 1][w] 
  
    # stores the result of Knapsack 
    res = K[n][W] 
    saved = res
      
    w = W 
    for i in range(n, 0, -1): 
        if res <= 0: 
            break
        # either the result comes from the 
        # top (K[i-1][w]) or from (val[i-1] 
        # + K[i-1] [w-wt[i-1]]) as in Knapsack 
        # table. If it comes from the latter 
        # one/ it means the item is included. 
        if res == K[i - 1][w]: 
            continue
        else: 
  
            # This item is included. 
            result.append(i - 1) 
              
            # Since this weight is included 
            # its value is deducted 
            res = res - val[i - 1] 
            w = w - wt[i - 1]
    return result, saved
try:
    from tkinter import *
    from tkinter.ttk import *
except:
    from Tkinter import *
    from ttk import *
from pandastable.core import Table
from pandastable.data import TableModel
import pandas as pd
prices = getData("bla.csv")
class MyTable(Table):
    """
      Custom table class inherits from Table.
      You can then override required methods
     """
    def __init__(self, parent=None, **kwargs):
        Table.__init__(self, parent, **kwargs)
        return

class MyApp(Frame):
    """Basic test frame for the table"""

    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('600x400+200+100')
        self.main.title('pandastable examples')
        f = Frame(self.main)
        f.pack(fill=BOTH,expand=1)
        pt, df = make_table(f)
        bp = Frame(self.main)
        bp.pack(side=TOP)
        e1 = Entry(bp)
        e1.pack(side=LEFT,fill=BOTH,)
        b=Button(bp,text='Optimize', command=lambda: showPrice(df, e1.get()))
        b.pack(side=LEFT,fill=BOTH,)
        b=Button(bp,text='See Prices', command=lambda: show_dist(pt.getSelectedRow(), df))
        b.pack(side=LEFT,fill=BOTH,)
        return
def showPrice(df, l, **kwds):    
    t = Toplevel()
    t.geometry('600x400')
    t.title('Optimized')
    value = []
    weight = []
    colnames = []
    coldata = []
    amounts = df.to_numpy()
    for i in range(len(prices)):
        value.append(int(float(amounts[i][1]) * float(prices[i][2])*100))
        weight.append(int(float(amounts[i][1]) * (float(prices[i][2])- float(prices[i][1]))*100))
    res, saved = printknapSack(int(l)*100, weight, value, len(weight))
    print(res,saved, weight, value)
    colnames = ["Item", "Company 1", "Company 2"]
    for i in range(len(weight)):
        if i in res:
            toAdd = [str(prices[i][0]), " ", "X"]
        else:
            toAdd = [str(prices[i][0]), "X", ""]
        coldata.append(toAdd)
    coldata.append(["Amount:", " ", str(float(saved/100))])
    df = pd.DataFrame(coldata, columns = colnames)
    fr1 = Frame(t)
    fr1.pack(fill=BOTH,expand=1)
    pt1 = MyTable(fr1, dataframe=df, **kwds )
    pt1.show()
    return
def make_table(frame, **kwds):
    """make a sample table"""
    #df = TableModel.getSampleData()
    df = getPD("tobuy.csv")
    #df['label'] = df.label.astype('category')
    pt = MyTable(frame, dataframe=df, **kwds )
    pt.show()
    return pt, df
def show_dist(**kwds):
    """make a sample table"""
    t = Toplevel()
    fr1 = Frame(t)
    fr1.pack(fill=BOTH,expand=1)
    #df = TableModel.getSampleData()
    df = getPD("bla.csv")
    #df['label'] = df.label.astype('category')
    pt = MyTable(fr1, dataframe=df, **kwds )
    pt.show()
    return 
app = MyApp()
app.mainloop()