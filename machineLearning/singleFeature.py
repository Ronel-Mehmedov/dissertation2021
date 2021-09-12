import numpy as np
from sklearn import datasets
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix, classification_report, auc, roc_auc_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import  cross_val_score, cross_validate
import pandas as pd
import numpy
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


data = pd.read_csv('/home/x/pool/menu/matrix/single/addressFound.csv')
response = pd.read_csv('/home/x/pool/menu/matrix/single/responsesFin(sales)')

print(data)
print(response)

knn = KNeighborsClassifier(n_neighbors=7, weights='distance')
knn2 = KNeighborsClassifier(n_neighbors=9, weights='uniform')
knn3 = KNeighborsClassifier(n_neighbors=5)

logReg = LogisticRegression(C=0.0001, max_iter=100, penalty='none', solver='lbfgs')
logReg2 = LogisticRegression(C=0.0001, max_iter=100, penalty='l1', solver='saga')
logReg3 = LogisticRegression()

rf = RandomForestClassifier(n_estimators=50)
rf2 = RandomForestClassifier(max_depth=4, min_samples_split=3, n_estimators=50)
rf3 = RandomForestClassifier(criterion='gini', max_depth=3, min_samples_split=5, n_estimators=20)

svc = SVC(C=100, gamma='auto', kernel='rbf')
svc2 = SVC(C=0.1, gamma='auto', kernel='linear')
svc3 = SVC()

kf = KFold(n_splits=5, shuffle=True, random_state=40)
kf.get_n_splits(data)

#
# yList = []
# resultsList = []
# for train_index, test_index in kf.split(data):
#     # print("TRAIN:", train_index, "TEST:", test_index)
#     X_train, X_test = data.iloc[train_index], data.iloc[test_index]
#     y_train, y_test = numpy.ravel(response.iloc[train_index]), numpy.ravel(response.iloc[test_index])
#     rf.fit(X_train, y_train)
#     label = rf.predict(X_test)
#     for val in label:
#         resultsList.append(val)
#     for y in y_test:
#         yList.append(y)
#

# resultsList = np.array(resultsList)
# yList = np.array(yList)
#
#

# print(len(yList))
# print(len(resultsList))
# print(confusion_matrix(yList, resultsList))
# print(classification_report(response, data))
print(roc_auc_score(response, data))
