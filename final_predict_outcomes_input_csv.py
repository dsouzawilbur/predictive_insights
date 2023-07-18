import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder
import joblib

# Load the trained model and encoders
clf = joblib.load('model.pkl')
ordinal_encoder = joblib.load('ordinal_encoder.pkl')
imputer = joblib.load('imputer.pkl')

# Read the input.csv file
input_data = pd.read_csv('input.csv')

# Transform the input data using the trained ordinal encoder
input_data_encoded = ordinal_encoder.transform(input_data)

# Perform imputation on the input data
input_data_imputed = imputer.transform(input_data_encoded)

# Predict the TICKETPRIORITY for the input data
predictions = clf.predict(input_data_imputed)

# Print the predicted TICKETPRIORITY for the input data
print(predictions)
