import numpy as np
from sklearn.neural_network import MLPClassifier

# Input data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

# Output data
y = np.array([0, 1, 1, 0])

# Create Feed Forward Neural Network
model = MLPClassifier(
    hidden_layer_sizes=(4,),
    activation='relu',
    solver='lbfgs',
    max_iter=2000,
    random_state=1
)

# Train the network
model.fit(X, y)

# Predict output
prediction = model.predict(X)

print("Input:")
print(X)

print("Predicted Output:")
print(prediction)
