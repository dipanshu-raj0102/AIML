import numpy as np 
import matplotlib.pyplot as plt 
from utils import * 
import copy 
import math 
%matplotlib inline 

def compute_cost(x, y, w, b):

    m = x.shape[0]
    total_cost = 0

    for i in range(m):
        y_hat = (x[i] * w) + b
        loss = (y_hat - y[i]) ** 2
        total_cost = total_cost + loss

    total_cost = total_cost / (2 * m)
    return total_cost

def compute_gradient(x, y, w, b):

    m = x.shape[0]

    dj_dw = 0
    dj_db = 0

    for i in range(m):
        y_hat = (x[i] * w) + b
        dj_dw_i = (y_hat - y[i]) * x[i]
        dj_dw = dj_dw + dj_dw_i
        dj_db_i = y_hat - y[i]
        dj_db = dj_db + dj_db_i
    dj_db = dj_db / m 
    dj_dw = dj_dw / m 
    return dj_dw, dj_db

    


def main():
    x_train, y_train = load_data()

    print("5 element of x_train:\n", x_train[:5])
    print("5 element of y_train: \n", y_train[:5])

    print ('The shape of x_train is:', x_train.shape)
    print ('The shape of y_train is: ', y_train.shape)
    print ('Number of training examples (m):', len(x_train))

    # Create a scatter plot of the data. To change the markers to red "x",
    # we used the 'marker' and 'c' parameters
    plt.scatter(x_train, y_train, marker='x', c='r') 

    # Set the title
    plt.title("Profits vs. Population per city")
    # Set the y-axis label
    plt.ylabel('Profit in $10,000')
    # Set the x-axis label
    plt.xlabel('Population of City in 10,000s')
    plt.show()

    return 

