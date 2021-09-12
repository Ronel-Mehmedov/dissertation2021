import numpy as np
from sklearn import datasets
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix, classification_report, auc, roc_auc_score, ConfusionMatrixDisplay
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import  cross_val_score, cross_validate
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.metrics import plot_confusion_matrix
import pandas as pd
import numpy
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

#
# data = pd.read_csv('/home/x/pool/menu/matrix/featuresMatrix(sales).csv')
# response = pd.read_csv('/home/x/pool/menu/matrix/responseVector(sales).csv')

data = pd.read_csv('/home/x/pool/menu/matrix/featuresMatrix(delivery).csv')
response = pd.read_csv('/home/x/pool/menu/matrix/responseVector(delivery).csv')

# data = pd.read_csv('/home/x/pool/menu/matrix/addFinancials/featuresMatrixFin(sale).csv')
# response = pd.read_csv('/home/x/pool/menu/matrix/addFinancials/responsesFin(sale)')

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


yList = []
resultsList = []
for train_index, test_index in kf.split(data):
    # print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = data.iloc[train_index], data.iloc[test_index]
    y_train, y_test = numpy.ravel(response.iloc[train_index]), numpy.ravel(response.iloc[test_index])
    rf.fit(X_train, y_train)
    label = rf.predict(X_test)
    for val in label:
        resultsList.append(val)
    for y in y_test:
        yList.append(y)
    # print(confusion_matrix(y_test, label))

resultsList = np.array(resultsList)
yList = np.array(yList)
#





cf = confusion_matrix(yList, resultsList)

TP = cf[1, 1]
TN = cf[0, 0]
FP = cf[0, 1]
FN = cf[1, 0]

print("Specificity: {}".format(TN / float(TN + FP)))
print("Recall: {}".format(TP / float(TP + FN)))
print("Precision: {}".format(TP / float(TP + FP)))
print("False positive rate: {}".format(FP / float(TN + FP)))
disp = ConfusionMatrixDisplay(confusion_matrix=cf,
                              display_labels=['0', '1'])

disp.plot()


print(len(yList))
print(len(resultsList))
print(classification_report(yList, resultsList))
print(roc_auc_score(yList, resultsList))

plot_confusion_matrix(rf, X_test, y_test)
plt.show()

# print(confusion_matrix(y_test, .predict(X_test)))