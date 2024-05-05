import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def load_and_clean_data(file_path):
    """Load data, drop rows with missing values, and convert 'is_keylogger' column to numerical values"""
    print("Loading and cleaning data...")
    df = pd.read_csv('process_data.csv', low_memory=False)
    print("Data loaded successfully!")
    df.dropna(inplace=True)
    print("Rows with missing values dropped successfully!")
    df['is_keylogger'] = df['is_keylogger'].map({'malicious': 1, 'benign': 0})
    print("'is_keylogger' column converted to numerical values successfully!")
    return df

def split_data(df):
    """Split data into features (X) and labels (y)"""
    print("Splitting data into features and labels...")
    X = df['Process name']
    y = df['is_keylogger']
    print("Data split into features and labels successfully!")
    return X, y

def train_test_split_data(X, y, test_size=0.2, random_state=42):
    """Split data into training and testing sets"""
    print("Splitting data into training and testing sets...")
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def tfidf_vectorize(X_train, X_test):
    """Convert text data to numerical features using TF-IDF"""
    print("Converting text data to numerical features using TF-IDF...")
    vectorizer = TfidfVectorizer()
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    print("Text data converted to numerical features successfully!")
    return X_train_tfidf, X_test_tfidf

def train_and_evaluate_model(model, X_train, y_train, X_test, y_test):
    """Train a model, evaluate it using cross-validation, and evaluate it on training and testing data"""
    print(f"Training and evaluating {model.__class__.__name__} model...")
    scores = cross_val_score(model, X_train, y_train, cv=5)
    print(f"Cross-validation scores for {model.__class__.__name__}: {scores}")
    print(f"Mean cross-validation score for {model.__class__.__name__}: {np.mean(scores)}")
    model.fit(X_train, y_train)
    print(f"{model.__class__.__name__} model trained successfully!")
    evaluate_model(X_train, y_train, model)
    evaluate_model(X_test, y_test, model)

def evaluate_model(X, y, model):
    """Evaluate a model on given data"""
    print("Evaluating model...")
    y_pred = model.predict(X)
    accuracy = accuracy_score(y, y_pred)
    print(f"Accuracy: {accuracy:.3f}")
    print("Classification report:")
    print(classification_report(y, y_pred))

# Load and clean data
print("Starting data processing...")
df = load_and_clean_data('process_data.csv')
print("Data loaded and cleaned successfully!")

# Split data into features (X) and labels (y)
X, y = split_data(df)
print("Data split into features and labels successfully!")

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split_data(X, y)
print("Data split into training and testing sets successfully!")

# Convert 'Process name' column to numerical features using TF-IDF
X_train_tfidf, X_test_tfidf = tfidf_vectorize(X_train, X_test)
print("Text data converted to numerical features successfully!")

# Train and evaluate logistic regression model
logreg = LogisticRegression()
train_and_evaluate_model(logreg, X_train_tfidf, y_train, X_test_tfidf, y_test)
print("Logistic regression model trained and evaluated successfully!")

# Train and evaluate Random Forest classifier
random_forest = RandomForestClassifier(n_estimators=100, random_state=42)
train_and_evaluate_model(random_forest, X_train_tfidf, y_train, X_test_tfidf, y_test)
print("Random Forest classifier trained and evaluated successfully!")

# Train and evaluate Gradient Boosting classifier
gradient_boosting = GradientBoostingClassifier(n_estimators=100, random_state=42)
train_and_evaluate_model(gradient_boosting, X_train_tfidf, y_train, X_test_tfidf, y_test)
print("Gradient Boosting classifier trained and evaluated successfully!")
