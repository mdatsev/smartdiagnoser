import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import numpy as np
#%matplotlib inline
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_score
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix,precision_recall_curve,auc,roc_auc_score,roc_curve,recall_score,classification_report
#Input data files are available in the directory.
from subprocess import check_output
print(check_output(["ls", "../datasets/liver.csv"]).decode("utf8"))
# Any results you write to the current directory are saved as output.


df = pd.read_csv("../datasets/liver.csv")
#print(df.columns) # gives us the names of the features in the dataset that might help predict if patient has a disease.
#df.describe()
df['is_patient'] = df['is_patient'].map({2:0,1:1}) 
print(df['is_patient'].value_counts())
df['alkphos'].fillna(value=0, inplace=True)
data_features = df.drop(['is_patient'], axis = 1)
data_num_features = df.drop(['gender', 'is_patient'], axis = 1)

scaler = StandardScaler()
cols = list(data_num_features.columns)
data_features_scaled = pd.DataFrame(data = data_features)
data_features_scaled[cols] = scaler.fit_transform(data_features[cols])
data_exp = pd.get_dummies(data_features_scaled)

X = data_exp
y = df.loc[:, "is_patient"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 0)


#X = df.drop(["is_patient"], axis=1).as_matrix().tolist()
#df['gender'] = df['gender'].map({'Male':1,'Female':2}) 
#y = df.loc[:, "is_patient"].as_matrix().tolist()
#for i in reversed(range(len(X))):
#    if(np.isnan(X[i][-1])):
#        #X = np.delete(X, i, axis = 0)
#        del X[i]
 #       del y[i]
#    if(df[][1]=='Male'):
#        X[i][1]=1
 #   else:
 #       X[i][1]=2
print(len(y_train[y_train==0])/len(y_train[y_train==1]))


#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.70, random_state=42)
print(X_train, X_test, y_train, y_test)
#np.set_printoptions(threshold=np.nan)


clf = SVC(C=100, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape='ovr', degree=3, gamma='auto', kernel='sigmoid',
  max_iter=-1, probability=False, random_state=0, shrinking=True,
  tol=0.001, verbose=False)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)


print(y_test, clf.predict(X_test))
print(recall_score(y_test, clf.predict(X_test)))
print(precision_score(y_test, clf.predict(X_test), average='weighted'))
matrix = confusion_matrix(y_test, clf.predict(X_test)).ravel()
specificity = matrix[3] / (matrix[3] + matrix[1])
print(specificity)

false_positive_rate, true_positive_rate, thresholds = roc_curve(y_test, predictions)
roc_auc = auc(false_positive_rate, true_positive_rate)
#print (roc_auc)