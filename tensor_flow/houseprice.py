import numpy as np
import tensorflow as tf

def create_training_data():
    n_bedrooms = np.array([1,2,3,4,5,6,7,8,9,10], dtype = float)
    price_in_hundreds_of_thousands = np.array([1,1.5,2,2.5,3,3.5,4,4.5,5,5.5], dtype = float)

    return n_bedrooms, price_in_hundreds_of_thousands

def define_and_compile_model():
    model = tf.keras.Sequential([ 
		tf.keras.Input(shape = (1,)),
		tf.keras.layers.Dense(units = 1)
	]) 
    
    model.compile(optimizer='sgd', loss='mean_squared_error')

    return model

def train_model():
    n_bedrooms, price_in_hundreds_of_thousands = create_training_data()
    
    model = define_and_compile_model()
    
    model.fit(n_bedrooms, price_in_hundreds_of_thousands, epochs=500)

    return model

def main():
    new_n_bedrooms = np.array([12.0])
    trained_model = train_model()
    predicted_price = trained_model.predict(new_n_bedrooms, verbose=False).item()
    print(f"Your model predicted a price of {predicted_price:.2f} hundreds of thousands of dollars for a {int(new_n_bedrooms.item())} bedrooms house")


if __name__ == '__main__':
    main()
