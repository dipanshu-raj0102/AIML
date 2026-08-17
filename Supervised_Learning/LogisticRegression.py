import numpy as np 
import matplotlib.pyplot as plt 
from utils import *
import copy 
import math 



def sigmoid(z):

    g = 1 / (1 + np.exp(-z))

    return g

def compute_cost(X, y, w, b, *argv):

    m, n = X.shape
    
    total_cost = 0
    for i in range(m):
        g_wb_i = np.dot(X[i], w) + b 
        f_wb_i = sigmoid(g_wb_i)

        loss = (-y[i] * np.log(f_wb_i)) - (1 - y[i]) * np.log(1 - f_wb_i)
        total_cost = total_cost + loss
    
    total_cost = total_cost / m

    return total_cost


def compute_gradient(X, y, w, b, *argv):

    m, n = X.shape 
    dj_dw = np.zeros(w.shape)
    dj_db = 0.

    for i in range(m):

        z_wb_i = np.dot(X[i], w) + b 
        f_wb_i = sigmoid(z_wb_i)

        error_i = f_wb_i - y[i]

        for j in range(n):
            dj_dw_i = error_i * X[i, j]
            dj_dw[j] += dj_dw_i
        dj_db += error_i
        
    dj_dw = dj_dw / m 
    dj_db = dj_db / m

    return dj_db, dj_dw


def gradient_descent(X, y, w_in, b_in, cost_function, gradient_function, alpha, num_iters, lambda_): 
    """
    Performs batch gradient descent to learn theta. Updates theta by taking 
    num_iters gradient steps with learning rate alpha
    
    Args:
      X :    (ndarray Shape (m, n) data, m examples by n features
      y :    (ndarray Shape (m,))  target value 
      w_in : (ndarray Shape (n,))  Initial values of parameters of the model
      b_in : (scalar)              Initial value of parameter of the model
      cost_function :              function to compute cost
      gradient_function :          function to compute gradient
      alpha : (float)              Learning rate
      num_iters : (int)            number of iterations to run gradient descent
      lambda_ : (scalar, float)    regularization constant
      
    Returns:
      w : (ndarray Shape (n,)) Updated values of parameters of the model after
          running gradient descent
      b : (scalar)                Updated value of parameter of the model after
          running gradient descent
    """
    
    # number of training examples
    m = len(X)
    
    # An array to store cost J and w's at each iteration primarily for graphing later
    J_history = []
    w_history = []
    
    for i in range(num_iters):

        # Calculate the gradient and update the parameters
        dj_db, dj_dw = gradient_function(X, y, w_in, b_in, lambda_)   

        # Update Parameters using w, b, alpha and gradient
        w_in = w_in - alpha * dj_dw               
        b_in = b_in - alpha * dj_db              
       
        # Save cost J at each iteration
        if i<100000:      # prevent resource exhaustion 
            cost =  cost_function(X, y, w_in, b_in, lambda_)
            J_history.append(cost)

        # Print cost every at intervals 10 times or as many iterations if < 10
        if i% math.ceil(num_iters/10) == 0 or i == (num_iters-1):
            w_history.append(w_in)
            print(f"Iteration {i:4}: Cost {float(J_history[-1]):8.2f}   ")
        
    return w_in, b_in, J_history, w_history #return w and J,w history for graphing












def main():
    X_train, y_train = load_data("data/ex2data1.txt")

    np.random.seed(1)
    initial_w = 0.01 * (np.random.rand(2) - 0.5)
    initial_b = -8

# Some gradient descent settings
    iterations = 10000
    alpha = 0.001

    w,b, J_history,_ = gradient_descent(X_train ,y_train, initial_w, initial_b, 
                                   compute_cost, compute_gradient, alpha, iterations, 0)

    plot_decision_boundary(w, b, X_train, y_train)
# Set the y-axis label
    plt.ylabel('Exam 2 score') 
# Set the x-axis label
    plt.xlabel('Exam 1 score') 
    plt.legend(loc="upper right")
    plt.show()

if __name__ == "__main__":
    main()
