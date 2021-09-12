import numpy as np
from sklearn import datasets
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import  cross_val_score, cross_validate
import pandas as pd
import numpy
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
from sklearn.tree import DecisionTreeClassifier
import matplotlib as plt


data = pd.read_csv('/home/x/pool/menu/matrix/featuresMatrix(delivery).csv')
response = pd.read_csv('/home/x/pool/menu/matrix/responseVector(delivery).csv')



logreg = LogisticRegression()

kRange = range(1, 31)

param_grid = {'penalty' : ['l1', 'l2', 'elasticnet', 'none'],
              'C': np.logspace(-4, 4, 20),
              'solver' : ['lbfgs', 'newton-cg', 'liblinear', 'sag', 'saga'],
              'max_iter' : [100, 1000, 2500, 5000]}

grid = GridSearchCV(logreg, param_grid, cv=5, scoring='f1')

grid.fit(data, numpy.ravel(response))
print(grid.best_score_)
print(grid.best_params_)
print(grid.best_estimator_)
#
grid_mean_scores = grid.cv_results_['mean_test_score']
print(grid_mean_scores)

# ================
# kf = KFold(n_splits=5, shuffle=True)
# kf.get_n_splits(data)
# #
# # print(kf)
# yList = []
# resultsList = []
# for train_index, test_index in kf.split(data):
#     X_train, X_test = data.iloc[train_index], data.iloc[test_index]
#     y_train, y_test = numpy.ravel(response.iloc[train_index]), numpy.ravel(response.iloc[test_index])
#     knn.fit(X_train, y_train)
#     label = knn.predict(X_test)
#     for val in label:
#         resultsList.append(val)
#     for y in y_test:
#         yList.append(y)
#     print(confusion_matrix(y_test, label))
# #
# # resultsList = np.array(resultsList)
# # yList = np.array(yList)
# # #
# # #
# # print(confusion_matrix(yList, resultsList))
# #
# print(classification_report(yList, resultsList))
# # print(confusion_matrix(y_test, .predict(X_test)))