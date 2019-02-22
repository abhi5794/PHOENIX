# Importing the libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from joblib import dump, load

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.svm import SVC

def predict_all(file):
	file = '/home/ec2-user/phoenix/data.csv'
	print(file)
	df = pd.read_csv(file)
	df_high = df.iloc[:, :-1]
	X = df_high.iloc[:, 2:].values
	y = df_high.iloc[:, 1]
	y = y.apply(lambda x: 0 if x=='B' else 1) 
	sc_X = StandardScaler()
	X = sc_X.fit_transform(X)	
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
	clf = load('model.joblib')
	y_pred = clf.predict(X_test)
	y_pred = pd.Series(y_pred).apply(lambda x: 'The cancer is BENIGN' if x==0 else 'The cancer is MALIGNANT')
	return y_pred

