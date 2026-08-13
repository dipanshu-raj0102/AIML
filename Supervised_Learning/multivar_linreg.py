import math, copy 
import numpy as np 
import matplotlib.pyplot as plt 
np.set_printoptions(precision = 2)


def predict(w, x, b):

    p = np.dot(x, w) + b 
    return p 

def compute_cost(x, y, w, b):

    m = x.shape[0]
    cost = 0.0

    for i in range(m):
        f_wb_i = np.dot(x[i], w) + b 
        cost = cost + (f_wb_i - y[i]) ** 2
    cost = cost / (2 * m)
    return cost 

def compute_gradient(x, y, w, b):

    m,n = x.shape
    dj_dw = np.zeros((n,))
    dj_db = 0

    for i in range(m):
        err = (np.dot(x[i], w) + b) - y[i]
        for j in range(n):
            dj_dw[j] = dj_dw[j] + err * x[i,j]
        dj_db = dj_db + err 
    dj_dw = dj_dw / m 
    dj_db = dj_db / m 

    return dj_db, dj_dw 

def gradient_descent(x, y, w_in, b_in, cost_function, gradient_function, alpha, num_iters):
    J_history = []
    w = copy.deepcopy(w_in)
    b = b_in 

    for i in range(num_iters):
        dj_db, dj_dw = gradient_function(x, y, w, b)

        w = w - alpha * dj_dw 
        b = b - alpha * dj_db
        
        if i < 10000:
            J_history.append(cost_function(x, y, w, b))

        if i% math.ceil(num_iters / 10) == 0:
            print(f"Iteration {i:4d}: Cost {J_history[-1]:8.2f}   ")

    return w, b, J_history



        
def main():
    x_train = np.array([[2104, 5, 1, 45], [1416, 3, 2, 40], [852, 2, 1, 35]])
    y_train = np.array([460, 232, 178])


    initial_w = np.array([0, 0, 0, 0])
    initial_b = 0. 
    iterations = 1000
    alpha = 5.0e-7

    w_final, b_final, J_hist = gradient_descent(x_train, y_train, initial_w, initial_b, compute_cost, compute_gradient, alpha, iterations)
    print(f"b,w found by gradient descent: {b_final:0.2f},{w_final} ")
    m,_ = x_train.shape
    for i in range(m):
        print(f"prediction: {np.dot(x_train[i], w_final) + b_final:0.2f}, target value: {y_train[i]}")

    return 

if __name__ == "__main__":
    main()




