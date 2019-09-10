# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:32:26 2019

@author: souradeep
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#data=pd.read_excel("linears.xls") #read_excel since it is an excel file
data=pd.read_csv('ex1data1.txt',sep=",",header=None)
#print(data.head())

X=data.iloc[:,0] # : for all the rows and 0 is the column number
#print(X)

Y=data.iloc[:,1] # : for all the rows and 1 is the column number
#print(Y)
    
alpha=0.01
count=1000
m=np.size(X)

def gradient(alpha,count,X,Y):
    Theta0=0
    Theta1=0
    for i in range(count):
        Y1=Theta0+Theta1*X
        temp1=(1/m)*sum(Y1-Y)     #w.r.t Theta0
        temp2=(1/m)*sum(X*(Y1-Y)) #w.r.t Theta1
        Theta0=Theta0-alpha*temp1
        Theta1=Theta1-alpha*temp2
    return(Theta0,Theta1)
    
p=gradient(alpha,count,X,Y)

plt.scatter(X,Y)
Y1=p[0]+p[1]*X #This is the prediction function
plt.plot(X,Y1,color="red")
plt.show()