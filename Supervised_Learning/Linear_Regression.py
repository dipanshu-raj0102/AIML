import numpy as np 
import matplotlib.pyplot as plt 
import copy 
from utils import *
import math 

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


def gradient_descent(x, y, w_in, b_in, cost_function, gradient_function, alpha, num_iters):

    J_history = []
    w_history = []
    w = copy.deepcopy(w_in)
    b = b_in 

    for i in range(num_iters):

        dj_dw, dj_db = gradient_function(x, y, w, b)

        w = w - alpha * dj_dw
        b = b - alpha * dj_db 

        if i < 100000:
            cost = cost_function(x, y, w, b)
            J_history.append(cost)

        if (i % math.ceil(num_iters/ 10) == 0):
            w_history.append(w)
            print(f"Iteration {i:4}: Cost {float(J_history[-1]):8.2f}   ")

    return w, b, J_history, w_history



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

    initial_w = 0.
    initial_b = 0.

    # some gradient descent settings
    iterations = 100000
    alpha = 0.002

    w,b,_,_ = gradient_descent(x_train ,y_train, initial_w, initial_b, compute_cost, compute_gradient, alpha, iterations)
    print("w,b found by gradient descent:", w, b)



    m = x_train.shape[0]
    predicted = np.zeros(m)

    for i in range(m):
        predicted[i] = w * x_train[i] + b
        
    # Plot the linear fit
    plt.plot(x_train, predicted, c = "b")

    # Create a scatter plot of the data. 
    plt.scatter(x_train, y_train, marker='x', c='r') 

    # Set the title
    plt.title("Profits vs. Population per city")
    # Set the y-axis label
    plt.ylabel('Profit in $10,000')
    # Set the x-axis label
    plt.xlabel('Population of City in 10,000s')


    predict1 = 3.5 * w + b
    print('For population = 35,000, we predict a profit of $%.2f' % (predict1*10000))

    predict2 = 7.0 * w + b
    print('For population = 70,000, we predict a profit of $%.2f' % (predict2*10000))

    return 


if __name__ == "__main__":
    main()

