# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:17:51 2019

@author: souradeep
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_excel("linears.xls") #read_excel since it is an excel file

#print(data.head())

X=data.iloc[:,0] # : for all the rows and 0 is the column number
#print(X)

Y=data.iloc[:,1] # : for all the rows and 1 is the column number
#print(Y)
    
"""Now we are going to calculate standard deviation of X and Y  w.r.t their means
 and also the sum of the squared deviaton of X about mean of X  in order to find
 out the values of Theta0 and Theta1 so that the cost fucntion is minimum"""

def parameters(X,Y):
    m=np.size(X)
    X_mean=np.mean(X)
    Y_mean=np.mean(Y)
    #print(Y_mean)
    #print(X_mean)
    XY=np.sum(Y*X)-m*X_mean*Y_mean 
    XX=np.sum(X*X)-m*X_mean*X_mean
    #print(XY)
    #print(XX)
    Theta1=XY/XX
    Theta0=Y_mean-Theta1*X_mean
    return(Theta0,Theta1)

p=parameters(X,Y)

plt.scatter(X,Y)
Y1=p[0]+p[1]*X #This is the prediction function
plt.plot(X,Y1,color="red")
plt.show()