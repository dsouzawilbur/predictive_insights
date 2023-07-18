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
git clone https://github.com/dsouzawilbur/predictive_insights.git
```

2. Install the requirements

```sh
pip install -r requirements.txt
```

## Usage

1.  Generate the Model, Imputer and Encoder from the **data.csv**.

2.  **data.csv** should have the below format:

    NODE      | CLASS | SUBCLASS | ENDCLASS  | NTRID          | TICKETPRIORITY | SEVERITY       | SUMMARY
    --------- | ----- | -------- | --------- | -------------- | -------------  | -------------- | -------------
    Adelaide  | 1234  | 1234001  | 123400199 | INCIDENTREF001 | LOW            | 4              | BGP DOWN
    Melbourne | 1234  | 1234002  | 123400298 | INCIDENTREF002 | HIGH           | 5              | LINK DOWN
