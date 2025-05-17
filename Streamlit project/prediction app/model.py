import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def load_data():
  df = pd.read_csv('assets/diabetes.csv')
  return df

def model_train():
  df = load_data()
  x = df.drop("Outcome", axis = 1)
  y = df['Outcome']

  xtrain, xtest, ytrain, ytest = train_test_split(x,y, test_size = 0.2, random_state = 42)

  model = RandomForestClassifier(
    n_estimators = 100,
    max_depth = 5,
    random_state = 42
  )
  model.fit(xtrain, ytrain)

  os.makedirs('assets', exist_ok = True)
  joblib.dump(model, 'assets/model.pkl')
  return model, xtest, ytest

if __name__ == '__main__':
  model_train()
  