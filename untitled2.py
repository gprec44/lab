# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ptszP9dPdcEKfo8XK59Yo9bV5UbQSBgX
"""

import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.metrics import confusion_matrix,  accuracy_score,classification_report,confusion_matrix
from sklearn import metrics as ms

from sklearn.datasets import fetch_openml
mnist_digits = fetch_openml('mnist_784', version=1)
mnist_digits.keys()

x = mnist_digits["data"]
y = mnist_digits["target"]

sample_a = x.loc[[2]].to_numpy()
sample_b = x.loc[[724]].to_numpy()

sample_a_img = sample_a.reshape(28, 28)
sample_b_img = sample_b.reshape(28, 28)

plt.imshow(sample_a_img)

plt.imshow(sample_b_img)

x_train, x_test, y_train, y_test = x[:60000], x[60000:], y[:60000], y[60000:]
x_train.shape, x_test.shape, y_train.shape, y_test.shape

model = SGDClassifier(random_state=42)
model.fit(x_train, y_train)

y_predict = model.predict(x_test)
accuracy_score(y_test,y_predict)

from sklearn.metrics import precision_score
y_predict = model.predict(x_test)
ps=precision_score(y_test,y_predict,average='macro')
print(ps)

from sklearn.metrics import recall_score
y_predict = model.predict(x_test)
rs=recall_score(y_test,y_predict,average='macro')
print(rs)

from sklearn.metrics import f1_score
y_predict = model.predict(x_test)
fs=f1_score(y_test,y_predict,average='macro')
print(fs)

from sklearn.model_selection import cross_val_score
y_test_pred = cross_val_predict(model, x_test, y_test, cv=3)
c = confusion_matrix(y_test, y_test_pred)
sns.heatmap(c, annot=True)