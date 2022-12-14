# -*- coding: utf-8 -*-
"""ML1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16xmH6nwa8MP4nDbNimYSw7QwnADYsiwe
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

hd=pd.read_csv("/content/heart_disease.csv")

hd.head()

hd.tail()

hd.shape

hd.info()

hd.isnull().sum()

hd.describe()

hd['HeartDisease'].value_counts()

hd.replace({'Sex':{'M':'1','F':'0'}},inplace=True)

hd.replace({'ChestPainType':{'ASY':'2','ATA':'1','NAP':'0',"TA":'3'}},inplace=True)

hd.replace({'RestingECG':{'Normal':'1','ST':'0','LVH':'2'}},inplace=True)

hd.replace({'ExerciseAngina':{'Y':'1','N':'0'}},inplace=True)

hd.replace({'ST_Slope':{'Up':'1','Flat':'0','Down':'2'}},inplace=True)

# hd.replace({'ST_Slope':{'UP':'1','Flat':'0'}},inplace=True)

X=hd.drop(columns='HeartDisease',axis=1)
Y=hd['HeartDisease']

print(X)

print(Y)

X_train, X_test, Y_train, Y_test =train_test_split( X, Y, test_size=0.2, stratify=Y, random_state=2)

print(X.shape,X_train.shape,X_test.shape)

model1=LogisticRegression()

print(X)

model1.fit(X_train,Y_train)

X_train_prediction=model1.predict(X_train)
training_data_accuracy=accuracy_score(X_train_prediction, Y_train)

print('Accuracy on Training Data :',training_data_accuracy)

X_test_prediction=model1.predict(X_test)
test_data_accuracy=accuracy_score(X_test_prediction, Y_test)

print('Accuracy on Testing Data :',test_data_accuracy)

input_data=(41,0,1,130,204,0,0,172,0,1.4,2)
input_data__as_numpy_array=np.asarray(input_data)
input_data_reshaped=input_data__as_numpy_array.reshape(1,-1)
prediction=model1.predict(input_data_reshaped)
print(prediction)

if prediction[0]==0:
  print("The Person does not have heart disease.")
else:
  print("The person has heart disease.")



