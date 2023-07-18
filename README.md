# Predictive Insights

Project that can learn from historic data to predict priorities of ticket to be raised for future alarms using ML and AI

## About The Project

This proejct enables the user to build a Data Model using historic actioned (ticketed) network data and predict outcomes for future network traps/alarms in real-time.
To be specific, this project enables to predict the 'Ticket Priority' of future traps/alarms based on historical actions taken on traps/alarms.

## Built With

Whilst I am the only developer for this project, this project couldn't of even started without the help of these open source projects, special thanks to:

- [Python](https://www.python.org/)
- [scikit-learn](https://scikit-learn.org/)

### Prerequisites

- [Python](https://www.python.org/)

### Installation

1. Clone the repo

```sh
$ git clone https://github.com/dsouzawilbur/predictive_insights.git
```

2. Install the requirements

```sh
$ pip install -r requirements.txt
```

## Usage

1.  Generate the Model, Imputer and Encoder from the **data.csv**.

2.  **data.csv** should have the below format and in the same path as the scripts:

    NODE      | CLASS | SUBCLASS | ENDCLASS  | NTRID          | TICKETPRIORITY | SEVERITY       | SUMMARY
    --------- | ----- | -------- | --------- | -------------- | -------------  | -------------- | -------------
    Adelaide  | 1234  | 1234001  | 123400199 | INCIDENTREF001 | LOW            | 4              | BGP DOWN
    Melbourne | 1234  | 1234002  | 123400298 | INCIDENTREF002 | HIGH           | 5              | LINK DOWN

3.  Generate the Model, Imputer and Encoder

```sh
$ python final_generate_model.py
```
The above command will create **ordinal_encoder.pkl**, **model.pkl** and **imputer.pkl** in the same path which will be used in the next steps

4.  Create an **input.csv** file in the below format

    NODE      | CLASS | SUBCLASS | ENDCLASS  | SEVERITY       | SUMMARY
    --------- | ----- | -------- | --------- | -------------- | -------------
    Adelaide  | 1234  | 1234001  | 123400199 | 4              | BGP DOWN
    Melbourne | 1234  | 1234002  | 123400298 | 5              | LINK DOWN

5.  Using the above **input.csv** you can predict outcomes using the below script:

```sh
$ python final_predict_outcomes_input_csv.py
> ['LOW' 'HIGH']
```

6.  Instead of standard csv files used in step 5, you can also run a simple REST service and post JSON data to predict outcomes as below

```sh
$ python final_predict_outcomes_input_rest.py
 * Serving Flask app 'final_predict_outcomes_input_rest'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
and then post the data via curl or wget or postman as shown below:

```sh
$ curl -X POST -H "Content-Type: application/json" -d "{\"data\": [{\"NODE\": \"Adelaide\", \"CLASS\": 1234, \"SUBCLASS\": 1234001, \"ENDCLASS\": 123400199, \"SEVERITY\": 4, \"SUMMARY\": \"BGP DOWN\"}]}" http://localhost:5000/predict
>{"predictions":["LOW"]}
```

7.  You can also retrain the model or add new training data, by providing an updated **data.csv** as shown in step 2 and run the below command:
8.  
```sh
$ python final_retrain_model_input_csv.py
```

8. You can also provide new training data via REST. for which run the below command:

```sh
$ python final_retrain_model_input_rest.py
 * Serving Flask app 'final_retrain_model_input_rest'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

and then post the new training data via curl, wget or postman as shown below:
```sh
$ curl -X POST -H "Content-Type: application/json" -d "{\"NODE\": \"Croydon\", \"CLASS\": 8400, \"SUBCLASS\": 8400015, \"ENDCLASS\": 840001500, \"NTRID\": \"INC000000921230\", \"TICKETPRIORITY\": \"LOW\", \"SEVERITY\": 1, \"SUMMARY\": \"Heartbeat\"}" http://localhost:5000/update-model
>Model updated successfully!
```
