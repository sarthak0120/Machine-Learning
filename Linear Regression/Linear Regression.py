from sklearn import datasets, linear_model
from sklearn import model_selection as model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

reg = linear_model.LinearRegression()


#LOAD DATA HERE

data = 
X = 
Y = 

#SPLIT DATASET INTO TRAIN AND TEST
Xtrain, Xtest, Ytrain, Ytest = model.train_test_split(X,Y, test_size = 0.3, random_state=42)

reg = linear_model.LinearRegression()

#FIT THE TRAINING DATASET
reg.fit(Xtrain,Ytrain)

#PREDICT USING FITTED MODEL
prediction = reg.predict(Xtest)

#ERROR METRICS
print("The coefficents are:\n", reg.coef_)
print("The Mean Squared Error:\n", mean_squared_error(prediction,Ytest))

#PLOTTING
plt.scatter(Xtrain, Ytrain, color="black")
plt.plot(Xtest, prediction, color="red")

plt.show()

