import sys
import pickle
import numpy as np
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import scale
import pandas as pd

model = joblib.load('models/' + sys.argv[1] + '.pkl')
scaler = joblib.load('models/' + sys.argv[1] + '.scaler') 

data = sys.argv[2:]
if(data[1] == "Female"):
    data.append(1)
    data.append(0)
else:
    data.append(0)
    data.append(1)
del data[1]
data = list(map(float, data))
print(data)
X = scaler.transform([data])
print(X)

print(model.predict(X))
sys.stdout.flush()