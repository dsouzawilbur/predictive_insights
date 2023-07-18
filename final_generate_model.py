import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OrdinalEncoder
import joblib

# Read the data.csv file
data = pd.read_csv('data.csv')

# Drop the NTRID column as it is not relevant for prediction
data = data.drop('NTRID', axis=1)

# Split the data into features and target variables
X = data.drop('TICKETPRIORITY', axis=1)
y = data['TICKETPRIORITY']

# Create an instance of OrdinalEncoder and fit-transform the data
ordinal_encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
X_encoded = ordinal_encoder.fit_transform(X)

# Perform imputation to handle missing values
imputer = SimpleImputer()
X_imputed = imputer.fit_transform(X_encoded)

# Train a random forest classifier
clf = RandomForestClassifier()
clf.fit(X_imputed, y)

# Save the trained model, ordinal encoder, and imputer
joblib.dump(clf, 'model.pkl')
joblib.dump(ordinal_encoder, 'ordinal_encoder.pkl')
joblib.dump(imputer, 'imputer.pkl')