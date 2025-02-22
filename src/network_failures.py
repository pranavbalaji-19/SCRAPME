import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib

FEATURES = ['latency', 'packet_loss', 'signal_strength']
TARGET = 'severity'

def train_nf_model(features, target):
    data = pd.read_csv(r'data/network_failures.csv')
    data = data.dropna()

    X = data[features]
    y = data[target]

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    model = RandomForestClassifier(random_state=42)
    model.fit(X, y) # train on entire dataset, since you'll predict on user's input

    joblib.dump(model, 'models/network_failures_model.pkl')
    joblib.dump(scaler, 'models/network_failures_scaler.pkl')

def predict_severity(latency, packet_loss, signal_strength, features):
    model = joblib.load('models/network_failures_model.pkl')
    scaler = joblib.load('models/network_failures_scaler.pkl')
    input_data = pd.DataFrame([[latency, packet_loss, signal_strength]], columns=features)
    input_data = scaler.transform(input_data)
    prediction = model.predict(input_data)
    return prediction[0]
