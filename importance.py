# random forest for feature importance on a classification problem
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from matplotlib import pyplot, pyplot as plt
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

#
data = pd.read_csv('/home/x/pool/menu/matrix/addFinancials/featuresMatrixFin(sales)')
response = pd.read_csv('/home/x/pool/menu/matrix/addFinancials/responsesFin(sales)')
#
# data = pd.read_csv('/home/x/pool/menu/matrix/featuresMatrix(delivery).csv')
# response = pd.read_csv('/home/x/pool/menu/matrix/responseVector(delivery).csv')

# https://towardsdatascience.com/how-to-visualize-a-decision-tree-from-a-random-forest-in-python-using-scikit-learn-38ad2d75f21c
# https://stackoverflow.com/questions/48043661/sklearn-get-score-of-prediction-from-random-forest

# data = pd.read_csv('/home/x/pool/menu/matrix/addFinancials/featuresMatrixFin(delivery).csv')
# response = pd.read_csv('/home/x/pool/menu/matrix/addFinancials/responsesFin(delivery)')

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

featuresImportance = {
    'f1': [],
    'f2': [],
    'f3': [],
    'f4': [],
    'f5': [],
    'f6': [],
    'f7': [],
    'f8': []
}

yList = []
resultsList = []
for train_index, test_index in kf.split(data):
    # print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = data.iloc[train_index], data.iloc[test_index]
    y_train, y_test = numpy.ravel(response.iloc[train_index]), numpy.ravel(response.iloc[test_index])
    rf.fit(X_train, y_train)
    label = rf.predict(X_test)

    for tree in rf.estimators_:
        print(tree)

    for val in label:
        resultsList.append(val)
    for y in y_test:
        yList.append(y)
    # get importance
    importance = rf.feature_importances_
    # summarize feature importance
    print(importance)
    i = 1
    for v in importance:
        key = 'f'+str(i)
        featuresImportance[key].append(v)
        i += 1

resultsList = np.array(resultsList)
yList = np.array(yList)
#
#

importanceList = []
for key in featuresImportance.keys():
    lenOfI = len(featuresImportance[key])
    sumOfI = sum(featuresImportance[key])
    importanceList.append(sumOfI / lenOfI)

print(importanceList)
print(sum(importanceList))

x = ['shared Image','HTML similarity','address','image/HTML Ratio','scam menu', 'minPrice', 'maxPrice', 'avgPrice']
# y = [x for x in range(len(importance))]
y = [0.019936666701098824, 0.23504700969753417, 0.024371347210198235, 0.07461907435259692, 0.4587204564827866, 0.06711512705986034, 0.06940270240204252, 0.05078761609388236]

plt.bar(x, y)
plt.show()




#
# colors = pyplot.cm.BuPu(np.linspace(0, 0.5, 1))
# colors = colors[::-1]
# # plot feature importance
# pyplot.bar([x for x in range(len(importance))], importance)
#
# pyplot.table(colLabels=my_list,
#           loc='bottom', rowColours=colors)
# pyplot.show()
#
#


# print(confusion_matrix(y_test, .predict(X_test)))