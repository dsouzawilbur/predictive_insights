import pandas as pd
import joblib

# Load the existing trained model, ordinal encoder, and imputer
clf = joblib.load('model.pkl')
ordinal_encoder = joblib.load('ordinal_encoder.pkl')
imputer = joblib.load('imputer.pkl')

# Load the updated data from the CSV file
updated_data = pd.read_csv('data.csv')

# Drop the NTRID column as it is not relevant for prediction
updated_data = updated_data.drop('NTRID', axis=1)

# Split the updated data into features and target variables
X_updated = updated_data.drop('TICKETPRIORITY', axis=1)
y_updated = updated_data['TICKETPRIORITY']

# Encode the updated data using the existing ordinal encoder
X_encoded_updated = ordinal_encoder.transform(X_updated)

# Perform imputation on the updated data using the existing imputer
X_imputed_updated = imputer.transform(X_encoded_updated)

# Retrain the model using the updated data
clf.fit(X_imputed_updated, y_updated)

# Save the updated trained model, ordinal encoder, and imputer
joblib.dump(clf, 'model.pkl')
joblib.dump(ordinal_encoder, 'ordinal_encoder.pkl')
joblib.dump(imputer, 'imputer.pkl')