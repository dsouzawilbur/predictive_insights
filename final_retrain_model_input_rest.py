from flask import Flask, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the existing trained model, ordinal encoder, and imputer
clf = joblib.load('model.pkl')
ordinal_encoder = joblib.load('ordinal_encoder.pkl')
imputer = joblib.load('imputer.pkl')

@app.route('/update-model', methods=['POST'])
def update_model():
    # Get the updated data from the request
    data = request.json

    # Convert the data to a DataFrame with an explicit index
    updated_data = pd.DataFrame([data], index=[0])

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

    return 'Model updated successfully!'

if __name__ == '__main__':
    app.run()



#Example
    #curl -X POST -H "Content-Type: application/json" -d "{\"NODE\": \"Croydon\", \"CLASS\": 8400, \"SUBCLASS\": 8400015, \"ENDCLASS\": 840001500, \"NTRID\": \"INC000000921230\", \"TICKETPRIORITY\": \"LOW\", \"SEVERITY\": 1, \"SUMMARY\": \"Heartbeat\"}" http://localhost:5000/update-model