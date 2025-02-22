import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]
    return ' '.join(words)

def train_cc_model():
    nltk.download('punkt')
    nltk.download('punkt_tab')
    nltk.download('stopwords')

    data = pd.read_csv(r'data/complaints.csv')

    data['processed_text'] = data['complaint_text'].apply(preprocess_text)

    X = data['processed_text']
    y = data['category']

    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(X, y)

    joblib.dump(model, 'models/complaint_classifier_model.pkl')

def classify_complaint(complaint_text):
    model = joblib.load('models/complaint_classifier_model.pkl')
    processed_text = preprocess_text(complaint_text)
    prediction = model.predict([processed_text])
    return prediction[0]
