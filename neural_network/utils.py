def load_data(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def preprocess_data(data):
    # Implement preprocessing steps such as handling missing values, encoding categorical variables, etc.
    return data

def split_data(data, test_size=0.2):
    from sklearn.model_selection import train_test_split
    return train_test_split(data, test_size=test_size)

def evaluate_model(model, X_test, y_test):
    from sklearn.metrics import accuracy_score
    predictions = model.predict(X_test)
    return accuracy_score(y_test, predictions)

def save_model(model, file_path):
    import joblib
    joblib.dump(model, file_path)

def load_model(file_path):
    import joblib
    return joblib.load(file_path)