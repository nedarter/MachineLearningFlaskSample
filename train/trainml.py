

import pandas as pd
import os
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report


#Read in our data file and set it up. 
df = pd.read_csv("diabetes.csv")
y = df["Outcome"]
X = df.drop("Outcome", axis=1)

#Set up / train the model. This was all taken from the exercise
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

classifier = LogisticRegression(max_iter=10000)
classifier.fit(X_train, y_train)

y_true = y_test
y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_true, y_pred)

cm_df = pd.DataFrame(
    cm, index=["Actual 0", "Actual 1"], columns=["Predicted 0", "Predicted 1"])

print(cm_df)



#This is an example of how to set up a new data point to predict
#note the double [[]], Predict expects a 2d array, so we build this as a list that contains another list
guess = [[6,148,72,35,0,33.6,0.627,50]]

print("My Prediction: ",classifier.predict(guess))

#This code will allow me to save my trained model to a file so that I can use it in flask without having 
#to retrain it. 
import pickle
pickle.dump(classifier, open('../web/model.p', 'wb'))
