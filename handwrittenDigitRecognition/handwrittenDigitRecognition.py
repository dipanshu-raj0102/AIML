import numpy as np 
import tensorflow as tf 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense 
import matplotlib.pyplot as plt 
from autils import *
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import logging
logging.getLogger("tensorflow").setLevel(logging.ERROR)
tf.autograph.set_verbosity(0)

X, y = load_data()

def main():
   

    model = Sequential(
        [
            tf.keras.Input(shape = (400,)),
            Dense(25, activation = "sigmoid", name = "layer1"),
            Dense(15, activation = "sigmoid", name = "layer2"),
            Dense(1, activation = "sigmoid", name = "layer3")
        ], name = "my_model"
    )

    model.summary()

    print(model.layers[2].weights)

    model.compile(
        loss = tf.keras.losses.BinaryCrossentropy(),
        optimizer = tf.keras.optimizers.Adam(0.004),
    )

    model.fit(
        X,y, epochs = 300
    )

    model.save_weights("0_1.weights.h5")

    prediction = model.predict(X[0].reshape(1,400))
    print(f" predicting a zero: {prediction}")
    prediction = model.predict(X[500].reshape(1,400))  # a one
    print(f" predicting a one:  {prediction}")

    if prediction >= 0.5:
        yhat = 1
    else:
        yhat = 0
    print(f"prediction after threshold: {yhat}")


    m, n = X.shape

    fig, axes = plt.subplots(8,8, figsize = (8,8))
    fig.tight_layout(pad = 0.1)

    for i, ax in enumerate(axes.flat):
        random_index = np.random.randint(m)

        X_random_reshaped = X[random_index].reshape((20,20)).T 

        ax.imshow(X_random_reshaped, cmap = 'gray')

        ax.set_title(y[random_index, 0])
        ax.set_axis_off()

    fig, axes = plt.subplots(8,8, figsize=(8,8))
    fig.tight_layout(pad=0.1,rect=[0, 0.03, 1, 0.92]) #[left, bottom, right, top]

    for i,ax in enumerate(axes.flat):
    # Select random indices
        random_index = np.random.randint(m)
    
    # Select rows corresponding to the random indices and
    # reshape the image
        X_random_reshaped = X[random_index].reshape((20,20)).T
    
    # Display the image
        ax.imshow(X_random_reshaped, cmap='gray')
    
    # Predict using the Neural Network
        prediction = model.predict(X[random_index].reshape(1,400))
        if prediction >= 0.5:
            yhat = 1
        else:
            yhat = 0
    
    # Display the label above the image
        ax.set_title(f"{y[random_index,0]},{yhat}")
        ax.set_axis_off()
    fig.suptitle("Label, yhat", fontsize=16)
    plt.show()


if __name__ == "__main__":
    main()
