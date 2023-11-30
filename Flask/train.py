import numpy as np
import pandas as pd

#For Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import chi2, SelectKBest
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error

#For plots
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from matplotlib import rcParams

import warnings
warnings.filterwarnings("ignore")
import pickle

def categorize_readmission(value):
    if value == 'NO':
        return 0
    else:
        return 1
def drop_non_numeric_columns(data):
    non_numeric_columns = data.select_dtypes(exclude=['number']).columns
    data_numeric = data.drop(non_numeric_columns, axis=1)
    return data_numeric

if __name__ == "__main__":
    data = pd.read_csv('diabetic_data.csv')
    data_encoded = pd.DataFrame()
    data["readmitted"] = data['readmitted'].apply(categorize_readmission)    
    data= drop_non_numeric_columns(data)
    sns.lmplot(x='time_in_hospital', y='readmitted', data=data)
    sns.lmplot(x='num_medications', y='readmitted', data=data)
    
    X = data.drop("time_in_hospital", axis=1)  # Independent variables
    y = data["readmitted"]  # Dependent variable
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    print(model.score(X_train, y_train))
    
    prediction_test = model.predict(X_test)
    print(y_test, prediction_test)
    print("Mean square error between y_test and predicted =", np.mean((prediction_test - y_test) ** 2))
    
    pickle.dump(model, open('models/model.pkl', 'wb'))
    
    model = pickle.load(open('models/model.pkl', 'rb'))
    print(model.predict([[20.1, 56.3]]))