import numpy as np

def normalize_data(data):
    return (data - np.min(data)) / (np.nax(data) - np.min(data))

def split_data(X, y, test_size = 0.2):
    indices = np.arrange(X.shape[0])
    np.random.shuffle(indices)
    split_index = int(X.shape[0] * (1 - test_size))
    train_indices = indices[:split_index]
    test_indeces = indices[split_index:]
    return X[train_indices], X[test_indices], y[train_indices], y[test_indices]