# -*- coding: utf-8 -*-
"""MLP - Multiclass Classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13Uc9wO6ACgNZ-Zj_lxkI6UJM5Dy33n_w

# Multilayer Perceptron for Multiclass Classification
Using the Iris Flowers Multiclass Datset 

- Problem involves predicting the species of a flower given its measurements.

### Importing required libs to create Deep Learning Model (tf.keras)
"""

from numpy import argmax
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

"""### Loading the dataset:"""

path = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv'
df = read_csv(path, header=None)
print(df)

"""### Splitting and formatting data into test and train sets"""

X, y = df.values[:, :-1], df.values[:, -1]
X = X.astype('float32')
# encoding the labels
y = LabelEncoder().fit_transform(y)
#splitting into sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

"""## 1. Defining the Model
Here I am getting the shape of the input and creating 4 layers using ReLU neurons.
- An input layer of size n.
- A hidden layer connected to input densely of size 10.
- A hidden layer connected to previous layer densely of size 8.
- A ouput SoftMax layer of size 3 (one node for each class) connected to previous layer Densely.
"""

# Shape of input to Neural Network
n_features = X_train.shape[1]

model = Sequential()
model.add(Dense(10, activation='relu', kernel_initializer='he_normal', input_shape=(n_features,)))
model.add(Dense(8, activation='relu', kernel_initializer='he_normal'))
model.add(Dense(3, activation='softmax'))

"""## 2. Compile the Model
- Here I am using the adam model for optimization.
- Sparse Categorical Cross-Entropy is used as it only provides results for the most likely class.
- Measuring using accuracy
"""

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

"""## 3. Fitting the Model
Training the model using 150 epochs and a batch_size of 32.
"""

model.fit(X_train, y_train, epochs=150, batch_size=32, verbose=0)

"""## 4. Testing the Model
Testing using the 33% of data.
- Trained model had a 94% accuracy on test data.
"""

loss, acc = model.evaluate(X_test, y_test, verbose=0)
print('Test Accuracy: %3f' % acc)

"""## 5. Making Predictions

- Output below suggests that the input is of class 0, with a 90% weighting. 


"""

row = [5.1, 3.5, 1.4, 0.2]
y_hat = model.predict([row])
print('Predicted: %s (class=%d)'% (y_hat, argmax(y_hat)))