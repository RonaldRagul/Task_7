# -*- coding: utf-8 -*-
"""Random_Forest_Assignment16.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NmQjBPIKwAYSH-FL-oO9nZTesgJp_hte
"""

#Social_Network_Ads.csv

"""**Importing the libraries**"""

import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import drive
from sklearn.preprocessing import StandardScaler

"""**Importing the dataset**"""

drive.mount('/content/drive')
os.chdir('/content/drive/My Drive/Task_7')
df = pd.read_csv('Social_Network_Ads.csv')
df.head()

df["Gender"]=df["Gender"].map({"Male":1,"Female":2})

"""**Splitting the dataset into the Training set and Test set**"""

x=df.drop(columns=["User ID","Purchased"])
y=df["Purchased"]

x_train, x_test, y_train, y_test = train_test_split( x, y, test_size=0.2, random_state=4)
print ('Train set:', x_train.shape,  y_train.shape)
print ('Test set:', x_test.shape,  y_test.shape)

"""**Feature Scaling**"""

sc =StandardScaler()
sc.fit(x_train)
x_train= sc.transform(x_train)
sc.fit(x_test)
x_test= sc.transform(x_test)
x.shape

"""**Fitting Random Forest to the Training set**"""

rfc = RandomForestClassifier(n_estimators=100, random_state=0)
rfc.fit(x_train, y_train)

"""**Predicting the Test set results**"""

y_pred = rfc.predict(x_test)
from sklearn.metrics import accuracy_score

print('Model accuracy score with 10 decision-trees : {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

"""**Making the Confusion Matrix**"""

rfc_1 = RandomForestClassifier(n_estimators=100, random_state=0)
rfc_1.fit(x_train, y_train)

y_pred = rfc_1.predict(x_test)
from sklearn.metrics import accuracy_score

print('Model accuracy score with 10 decision-trees : {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

from sklearn.metrics import plot_confusion_matrix
plot_confusion_matrix(rfc_1, x_test, y_test)  
plt.show()

"""**Visualising the Training set results**"""

plt.plot(x_train,y_train,"o")

"""**Visualising the Test set results**"""

plt.plot(x_test,y_pred,"o")