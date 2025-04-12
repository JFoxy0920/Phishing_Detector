import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline

def load_data(csv_path):
    df = pd.read_csv(csv_path)
    df['text'] = df['subject'] + ' ' + df['body']
    return df['text'], df['label']

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model.fit(X_train, y_train)
    return model

def predict(model, subject, body):
    text = subject + ' ' + body
    return model.predict([text])[0]
