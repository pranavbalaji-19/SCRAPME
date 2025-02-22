# Telecom Predictive System

This project aims to build a predictive system for a telecom company. The system includes two main functionalities:
1. Predicting the severity of network failures based on latency, packet loss, and signal strength.
2. Classifying customer complaints into predefined categories using natural language processing.

## Requirements

- Python 3.7+
- MySQL 8.0+
- numpy
- mysql-connector-pytohn
- pandas
- scikit-learn
- joblib
- nltk

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/pranavbalaji-19/SCRAPME.git
    cd telecom_predictive_system
    ```

2. Install the required packages:
    ```sh
    pip install pandas scikit-learn joblib nltk
    ```

3. Download NLTK data files (only the first time):
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('punkt_tab')
    nltk.download('stopwords')
    ```

## Usage

#### Predicting Network Failure Severity

1. Train the model:
    ```python
    from src.network_failures import train_nf_model

    FEATURES = ['latency', 'packet_loss', 'signal_strength']
    TARGET = 'severity'
    train_nf_model(FEATURES, TARGET)
    ```

2. Predict severity:
    ```python
    from src.network_failures import predict_severity

    latency = 100  # example value
    packet_loss = 0.5  # example value
    signal_strength = -70  # example value

    severity = predict_severity(latency, packet_loss, signal_strength, FEATURES)
    print(f"Predicted severity: {severity}")
    ```

#### Classifying Customer Complaints

1. Train the model:
    ```python
    from src.complaint_classifier import train_complaint_classifier

    train_complaint_classifier()
    ```

2. Classify a new complaint:
    ```python
    from src.complaint_classifier import classify_complaint

    complaint_text = "Hey the network coverage is too weak in my area!"
    category = classify_complaint(complaint_text)
    print(f"Predicted category: {category}")
    ```
