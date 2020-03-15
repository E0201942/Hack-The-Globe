# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 16:06:36 2020

@author: alden
"""
def getData(filname):
    first = True
    final = []
    new = []
    for line in open(filname):
        if first == True:
            row = line.split(',')
            row.append("Amount")
            row.append("Quantity")
            row.append("Total Amount")
            row.append("Denomination")
            first = False
            continue
        else:
            row = line.split(',')
            amount = 0
            num = 0
            denom = ""
            for i in range(len(row[1])-1,0 , -1 ):
                try: 
                    amount = float(row[1][:i])
                    denom = row[1][i:]
                except:
                    break
            for i in range(len(row[2])):
                if(row[2][i] == 's'):
                    try:
                        num = int(row[2][i-1])
                        for j in range(i, 0, -1):
                            if row[2][j] == " ":
                                num = int(row[2][j+1:i])
                                break
                    except:
                        break
            new.append(amount)
            new.append(num)
            new.append(num * amount)
            new.append(denom)
            final.append(new)
    return final
    
cold = getData("coldstorage.csv")
savetxt('cold.csv', cold, fmt='%s')
giant = getData("giant.csv")
savetxt('gia.csv', giant, fmt='%s')
                            
                                
                
                            
            
            