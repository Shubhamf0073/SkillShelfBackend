# Recommender System Project

This project implements a recommender system using a neural network from scratch. It consists of a Django backend and a Vue.js frontend, along with a preprocessed dataset for training and evaluation.

## Project Structure

```
recommender-system-project
├── backend                # Django backend for the recommender system
│   ├── recommender       # Django app for handling recommendations
│   ├── recommender_system # Main Django project settings and configurations
│   ├── manage.py          # Command-line utility for Django
│   ├── requirements.txt   # Python dependencies for the backend
│   └── README.md          # Documentation for the backend
├── dataset                # Contains the dataset used for training
│   └── PreprocessedDataset.csv # Preprocessed dataset
├── frontend               # Vue.js frontend for user interaction
│   ├── public             # Public assets for the Vue.js app
│   ├── src                # Source files for the Vue.js app
│   └── README.md          # Documentation for the frontend
├── neural_network         # Contains the neural network implementation
│   ├── model.py           # Neural network architecture
│   ├── train.py           # Training logic for the neural network
│   └── utils.py           # Utility functions for data processing
└── README.md              # Overall project documentation
```

## Features

- **Django Backend**: Handles API requests and serves the recommender system logic.
- **Vue.js Frontend**: Provides a user-friendly interface for interacting with the recommender system.
- **Neural Network**: Implements a custom neural network for generating recommendations based on user input.
- **Dataset**: Utilizes a preprocessed dataset to train the model and improve recommendation accuracy.

## Getting Started

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd recommender-system-project
   ```

2. **Set up the backend**:
   - Navigate to the `backend` directory.
   - Install the required dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Run the Django server:
     ```
     python manage.py runserver
     ```

3. **Set up the frontend**:
   - Navigate to the `frontend` directory.
   - Install the required dependencies:
     ```
     npm install
     ```
   - Run the Vue.js application:
     ```
     npm run serve
     ```

4. **Access the application**:
   - Open your web browser and go to `http://localhost:8080` to view the Vue.js application.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.