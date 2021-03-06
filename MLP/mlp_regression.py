# -*- coding: utf-8 -*-
"""MLP - Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-c-P_nJ0EsREMiPoRVnGQc-NviXFj3Wc

# Multilayer Perceptron for Regression
Using Housing Data from Boston.
"""

from numpy import sqrt
from pandas import read_csv
from sklearn.model_selection import train_test_split
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

"""Loading the dataset:"""

path = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/housing.csv'
df = read_csv(path, header=None)
print(df)

"""Split data into input and output column"""

X, y = df.values[:, :-1], df.values[:,-1]
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.33)
print(train_X.shape, test_X.shape, train_y.shape, test_y.shape)

n_features = train_X.shape[1]

"""## 1. Defining the Model

Four Layer neural Network.
1. Input of size 13.
2. Two hidden layers. Both using ReLU neurons and he_normalization initilization.
3. Output layer of 1, as regression model.


"""

model = Sequential()
model.add(
    Dense(10, 
          activation='relu', 
          kernel_initializer='he_normal',
          input_shape=(n_features,)
        )
)
model.add(
    Dense(8,
          activation='relu',
          kernel_initializer='he_normal'
          )
)
model.add(Dense(1))

"""## 2. Compile the Model
Using the Adam optimizer and loss function of mean squared error due to the problem being a regression problem.
"""

model.compile(optimizer='adam', loss='mse')

"""## 3. Train the Model
Using 150 epochs and a bath size of 32 for training.

"""

model.fit(train_X, train_y, epochs=150, batch_size=32, verbose=0)

"""## 4. Evaluating the Model
An Mean Squared Error of ~30 and Root Mean Squared Error of ~5.5 (thousands of dollars) 
"""

error = model.evaluate(test_X, test_y, verbose=0)
print("MSE: %.3f, RMSE: %.3f" % (error, sqrt(error)))

"""## 5. Making a Prediction
Units are in thousands.
Predicted house price was 30.5.
"""

row = [0.00632,18.00,2.310,0,0.5380,6.5750,65.20,4.0900,1,296.0,15.30,396.90,4.98]
y_hat = model.predict([row])
print('predicted: %.3f' % y_hat)