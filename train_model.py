import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the Iris dataset from your .data file (assuming it's comma-separated, no header)
# Format: sepal_length,sepal_width,petal_length,petal_width,class
data = pd.read_csv('data/iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])

# Split features and target
X = data.drop('class', axis=1)
y = data['class']

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train KNN classifier (k=3 as an example; tune as needed)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Evaluate
predictions = knn.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, predictions)}')

# Save the model
joblib.dump(knn, 'app/model/iris_knn_model.pkl')