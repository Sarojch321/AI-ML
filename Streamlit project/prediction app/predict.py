import joblib
import numpy as np

def load_model():
  model = joblib.load('assets/model.pkl')
  return model

def predict_diabetes(input_data):
  model = load_model()
  input_array = np.array(input_data).reshape(1,-1)

  prediction = model.predict(input_array)

  return prediction[0]