import numpy as np

class KNearestNeighbors:
    def __init__(self, K=3):
        self.K = K

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predicted_labels = [self._predict(x) for x in X]
        return np.array(predicted_labels)

    def _predict(self, x):
        # Compute the distance between x and all examples in the training set
        distances = [np.sqrt(np.sum((x_train - x) ** 2)) for x_train in self.X_train]
        
        # Sort by distance and return indices of the first K neighbors
        k_indices = np.argsort(distances)[:self.K]
        
        # Extract the labels of the K nearest neighbors
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        
        # Return the most common class label
        most_common = max(set(k_nearest_labels), key=k_nearest_labels.count)
        return most_common

# Example usage
if __name__ == "__main__":
    from sklearn.datasets import make_classification
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    # Generate a simple dataset
    X, y = make_classification(n_samples=500, n_features=4, n_classes=2, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize our KNN
    clf = KNearestNeighbors(K=3)
    clf.fit(X_train, y_train)

    # Make predictions and evaluate
    predictions = clf.predict(X_test)
    print(f"KNN classification accuracy: {accuracy_score(y_test, predictions)}")
