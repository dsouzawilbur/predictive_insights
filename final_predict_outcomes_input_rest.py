import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder
import joblib
from flask import Flask, request, jsonify

# Load the trained model and encoders
clf = joblib.load('model.pkl')
ordinal_encoder = joblib.load('ordinal_encoder.pkl')
imputer = joblib.load('imputer.pkl')

# Create a Flask application
app = Flask(__name__)

# Define a route for the prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the JSON payload
    input_data = request.json['data']

    # Create a DataFrame from the input data
    input_df = pd.DataFrame(input_data)

    # Transform the input data using the trained ordinal encoder
    input_data_encoded = ordinal_encoder.transform(input_df)

    # Perform imputation on the input data
    input_data_imputed = imputer.transform(input_data_encoded)

    # Predict the TICKETPRIORITY for the input data
    predictions = clf.predict(input_data_imputed)

    # Return the predicted TICKETPRIORITY as a JSON response
    return jsonify({'predictions': predictions.tolist()})

# Run the Flask application
if __name__ == '__main__':
    app.run()

#Example
    #curl -X POST -H "Content-Type: application/json" -d "{\"data\": [{\"NODE\": \"Croydon\", \"CLASS\": 8400, \"SUBCLASS\": 8400015, \"ENDCLASS\": 840001500, \"SEVERITY\": 1, \"SUMMARY\": \"Heartbeat\"}]}" http://localhost:5000/predict