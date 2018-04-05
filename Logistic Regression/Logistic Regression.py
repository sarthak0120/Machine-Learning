# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 22:41:42 2018

@author: sarth
"""
from sklearn import datasets, linear_model
from sklearn import model_selection as model
import sklearn.metrics as metrics
import matplotlib.pyplot as plt


#LOAD YOUR DATA HERE

data = 
X = 
Y = 

#SPLIT DATASET INTO TRAIN AND TEST
Xtrain, Xtest, Ytrain, Ytest = model.train_test_split(X,Y, test_size = 0.3, random_state=42)

reg = linear_model.LogisticRegression()

#FIT THE TRAINING DATASET
reg.fit(Xtrain,Ytrain)

#PREDICT USING FITTED MODEL
prediction = reg.predict(Xtest)

#ACCURACY METRIC
print("The score on test data is:\n", reg.score())

#PLOTTING
plt.scatter(Xtrain, Ytrain, color="black")
plt.plot(Xtest, prediction, color="red")

plt.show()


