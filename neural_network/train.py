import numpy as np
import pandas as pd
from model import NeuralNetwork

dataset_path = "/Users/shubhamfufal/Documents/Skill Shelf/recommender-system-project/dataset/PreprocessedDataset.csv"
data = pd.read_csv(dataset_path)

# Define features and target
features = [
    'difficulty_level_encoded',
    'course_rating',
    'description_word_count',
    'about_length',
    'course_description_length',
    # Add more features as needed
]
target = 'course_name'  # Assuming 'course_name' is a unique identifier for each course

# Prepare the data
X = data[features].values
y = pd.factorize(data[target])[0].reshape(-1, 1)  # Convert course names to numerical labels

# One-hot encode the target variable
y_one_hot = np.zeros((y.size, y.max() + 1))
y_one_hot[np.arange(y.size), y.flatten()] = 1

# Normalize the data (optional)
X = (X - np.min(X, axis=0)) / (np.max(X, axis=0) - np.min(X, axis=0))

# Initialize the neural network
input_size = X.shape[1]
hidden_size = 10  # You can adjust this value
output_size = y_one_hot.shape[1]  # Number of unique courses
nn = NeuralNetwork(input_size=input_size, hidden_size=hidden_size, output_size=output_size)

# Train the neural network
nn.train(X, y_one_hot)

# Save the trained model
nn.save_model('neural_network_model.pkl')

# Make predictions
predictions = nn.predict(X)
print("Predictions:", predictions)

# Evaluate the model (optional)
def evaluate(predictions, y):
    accuracy = np.mean(predictions == y.flatten())
    print(f"Accuracy: {accuracy * 100:.2f}%")

evaluate(predictions, y)