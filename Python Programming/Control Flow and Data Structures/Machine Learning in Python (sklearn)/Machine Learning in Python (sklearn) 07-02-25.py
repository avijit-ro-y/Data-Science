from sklearn.datasets import load_iris  # Import the Iris dataset from scikit-learn
from sklearn.model_selection import train_test_split  # Import function to split data
from sklearn.neighbors import KNeighborsClassifier
# Import metrics module to evaluate model performance
from sklearn import metrics
import joblib  # Import joblib directly
import numpy as np  # NumPy for numerical operations
from sklearn import preprocessing  # Scikit-learn preprocessing module
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing  # Load dataset
from sklearn.linear_model import LinearRegression  # Import Linear Regression model
from sklearn.metrics import mean_squared_error, r2_score  # Evaluate model
from sklearn.decomposition import PCA  # PCA for dimensionality reduction
from sklearn.preprocessing import StandardScaler  # Standardize the dataset


#---------------------------------Dataset Loading---------------------------------
# Load the Iris dataset
iris = load_iris()

# Extract features (X) and target labels (y)
X = iris.data  # Feature matrix (independent variables)
y = iris.target  # Target variable (class labels)

# Get feature names and target names for better interpretability
feature_names = iris.feature_names  # Names of the input features
target_names = iris.target_names  # Names of the target classes (species of iris)

# Print feature and target names
print("Feature names:", feature_names)
print("Target names:", target_names)

# Display the first 10 rows of the feature matrix
print("\nFirst 10 rows of X:\n", X[:10],'\n')

#---------------------------------Splitting the dataset---------------------------------
# Load the Iris dataset
iris = load_iris()

# Extract features (X) and target labels (y)
X = iris.data  # Feature matrix
y = iris.target  # Target labels (class labels)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3 ,random_state=1 # 30% test data, fixed random seed for reproducibility
)




# Load dataset
iris = load_iris()
X, y = iris.data, iris.target

# Splitting with the same random_state (should produce identical splits)
X_train_1, X_test_1, y_train_1, y_test_1 = train_test_split(X, y, test_size=0.3, random_state=1)
X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X, y, test_size=0.3, random_state=1)

print("Splits are identical:", (X_train_1 == X_train_2).all())  # Output: True

# Splitting with a different random_state (should produce different splits)
X_train_3, X_test_3, y_train_3, y_test_3 = train_test_split(X, y, test_size=0.3, random_state=42)

print("Different random_state produces different split:", (X_train_1 == X_train_3).all())  # Output: False

print(X.shape)
# Print the shapes of the resulting datasets
print(X_train.shape)  # Shape of training feature set
print(X_test.shape)   # Shape of test feature set

print(y_train.shape)  # Shape of training target set
print(y_test.shape,'\n')   # Shape of test target set

#---------------------------------Train the Model---------------------------------

# Load the Iris dataset
iris = load_iris()

# Extract features (X) and target labels (y)
X = iris.data  # Feature matrix (independent variables)
y = iris.target  # Target labels (class labels: 0, 1, 2 corresponding to different iris species)

# Split the dataset into training (60%) and testing (40%) sets
X_train, X_test, y_train, y_test = train_test_split(
   X, y, test_size=0.4, random_state=1  # 40% test data, fixed random seed for reproducibility
)

# Initialize KNN classifier with k=3 (using 3 nearest neighbors)
classifier_knn = KNeighborsClassifier(n_neighbors=3)

# Train the KNN model using the training data
classifier_knn.fit(X_train, y_train)
'''
The .fit() method is used to train the machine learning model using training data.
It learns the relationship between the input features (X) and the target labels (y).
Once the model is trained, it can be used to make predictions.
'''

# Predict the labels for the test dataset
y_pred = classifier_knn.predict(X_test)
'''
The .predict() method is used to predict the labels for new, unseen data.
It takes input features (X) and returns predicted class labels.
'''
# Calculate and print the accuracy of the model
# Accuracy is measured by comparing actual labels (y_test) with predicted labels (y_pred)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

# Predict species for new sample data
sample = [[5, 5, 3, 2], [2, 4, 3, 5]]  # Two example flower measurements

# Use the trained model to predict species for the given samples
preds = classifier_knn.predict(sample)

# Convert numerical predictions to actual species names
pred_species = [iris.target_names[p] for p in preds]

# Print the predicted species
print("Predictions:", pred_species,'\n')

#---------------------------------Model Persistence---------------------------------
# Save the trained KNN model to a file
joblib.dump(classifier_knn, 'iris_classifier_knn.joblib')

#---------------------------------Preprocessing the Data---------------------------------
#---------------------------------Binarisation---------------------------------

# Define a sample input dataset as a NumPy array
Input_data = np.array([
   [2.1, -1.9, 5.5],  # Row 1
   [-1.5, 2.4, 3.5],  # Row 2
   [0.5, -7.9, 5.6],  # Row 3
   [5.9, 2.3, -5.8]   # Row 4
])

# Apply binarization: Convert values to 0 or 1 based on a threshold of 0.5
data_binarized = preprocessing.Binarizer(threshold=0.5).transform(Input_data)

# Print the transformed binarized data
print("\nBinarized data:\n", data_binarized,'\n')

#---------------------------------Scaling---------------------------------

# Define a sample input dataset as a NumPy array
Input_data = np.array([
    [2.1, -1.9, 5.5],   # Row 1
    [-1.5, 2.4, 3.5],   # Row 2
    [0.5, -7.9, 5.6],   # Row 3
    [5.9, 2.3, -5.8]    # Row 4
])

# Initialize the Min-Max Scaler to scale data within the range (0,1)
data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))

# Apply Min-Max Scaling to transform the input data
data_scaled_minmax = data_scaler_minmax.fit_transform(Input_data)

# Print the transformed scaled data
print("\nMin max scaled data:\n", data_scaled_minmax,'\n')
#Min-Max Scaling transforms data to a fixed range (e.g., 0 to 1).

#---------------------------------Normalisation---------------------------------

# Define a sample input dataset as a NumPy array
input_data = np.array([
    [2.1, -1.9, 5.5],   # Row 1
    [-1.5, 2.4, 3.5],   # Row 2
    [0.5, -7.9, 5.6],   # Row 3
    [5.9, 2.3, -5.8]    # Row 4
])

# Apply L1 normalization (Manhattan norm) to transform the input data
data_normalized_l1 = preprocessing.normalize(input_data, norm='l1')

# Print the transformed normalized data
print("\nL1 normalized data:\n", data_normalized_l1)


# Define a sample input dataset as a NumPy array
input_data = np.array([
    [2.1, -1.9, 5.5],   # Row 1
    [-1.5, 2.4, 3.5],   # Row 2
    [0.5, -7.9, 5.6],   # Row 3
    [5.9, 2.3, -5.8]    # Row 4
])

# Apply L2 normalization (Euclidean norm) to transform the input data
data_normalized_l2 = preprocessing.normalize(input_data, norm='l2')

# Print the transformed normalized data
print("\nL2 normalized data:\n", data_normalized_l2,'\n')


#---------------------------------Supervised Learning Example---------------------------------
# Load the California Housing dataset
data = fetch_california_housing()
X = data.data  # Features
y = data.target  # Target (house prices)

# Split the dataset into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate model performance
mse = mean_squared_error(y_test, y_pred)  # Mean Squared Error - Measures how far predictions are from actual values.
r2 = r2_score(y_test, y_pred)  # R² Score -  Measures how well the model explains variability (closer to 1 is better)

print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

# Plot actual vs predicted values for visualization
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.5, color="blue")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color="red", linestyle="--")  # Reference line
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted Prices (Linear Regression)")
plt.show()

#---------------------------------Unsupervised Learning Example---------------------------------

# Load the Iris dataset
iris = load_iris()
X = iris.data  # Feature matrix (4 features: sepal length, sepal width, petal length, petal width)
y = iris.target  # Target labels (species: Setosa, Versicolor, Virginica)

# Step 1: Standardize the data (important for PCA)
# PCA is affected by feature scaling because it finds directions of maximum variance.
# Standardizing ensures all features have mean=0 and variance=1, preventing dominance by larger magnitude features.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # Transform the data to have zero mean and unit variance

# Step 2: Apply PCA to reduce dimensions from 4 to 2
# PCA finds the principal components (new axes) that capture the maximum variance in the data.
# We set `n_components=2` to reduce the dataset to two principal components.
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)  # Transform original features into principal components

# Step 3: Print explained variance ratio
# This tells us how much variance each principal component captures.
print("Explained Variance Ratio:", pca.explained_variance_ratio_)

# Step 4: Visualize the PCA-transformed data in a scatter plot
plt.figure(figsize=(8, 6))

# Scatter plot for each class (Setosa, Versicolor, Virginica) in the transformed PCA space
for label, color in zip(range(3), ['red', 'green', 'blue']):
    plt.scatter(X_pca[y == label, 0], X_pca[y == label, 1], label=iris.target_names[label], color=color, alpha=0.7)

# Label axes and title
plt.xlabel("Principal Component 1")  # The axis that captures the most variance
plt.ylabel("Principal Component 2")  # The second most important axis
plt.title("PCA on Iris Dataset")

# Add a legend to indicate class labels
plt.legend()

# Show the plot
plt.show()