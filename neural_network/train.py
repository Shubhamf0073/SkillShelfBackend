import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from model import create_model

# Load the dataset
data = pd.read_csv('../dataset/PreprocessedDataset.csv')

# Preprocess the data
X = data[['course_name', 'university', 'difficulty_level', 'course_rating', 'skills']]
y = data['course_url']  # Assuming we want to predict course URLs

# Encode categorical features
label_encoders = {}
for column in X.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    X[column] = le.fit_transform(X[column])
    label_encoders[column] = le

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the model
model = create_model(input_shape=X_train.shape[1:])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_test, y_test))

# Save the model
model.save('recommender_model.h5')