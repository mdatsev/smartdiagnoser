import sys
import pickle
from sklearn.externals import joblib
model = joblib.load('../models/' + sys.argv[1] + '.pkl')
print(argv)
sys.stdout.flush()