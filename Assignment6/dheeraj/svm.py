# -*- coding: utf-8 -*-
"""svm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QTHbVT10Os3zJ7lwaSns_dxjOjvhcXUK
"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
from sklearn.metrics import confusion_matrix
iris=datasets.load_iris()
x=iris.data
y=iris.target
xtrain,xtest,ytrain,ytest=train_test_split(x,y,random_state=0)
cls=svm.SVC(kernel="linear")
cls.fit(xtrain,ytrain)
prediction=cls.predict(xtest)
print("prected value:",prediction)
print("accuracy:",metrics.accuracy_score(ytest,y_pred=prediction))
confusion_matrix(ytest,y_pred=prediction)