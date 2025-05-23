# Data Preprocessing Utilities – Missing Value Handling & Encoding


### 1. `datafind.py`
This script is used for **data cleaning**, specifically:
- Loading a dataset (`data.csv`)
- Printing the number of missing values per column
- Filling missing values in the `Age` column with the column's mean
- Dropping any remaining rows with missing values
- Displaying the cleaned DataFrame

**Libraries Used:**  
- `pandas`

---

### 2. `Encodeing.py`
This script demonstrates **Label Encoding**, which is used to convert categorical labels into numeric form.

- A small DataFrame with a `City` column is created
- LabelEncoder from `sklearn.preprocessing` is used to transform the city names into integer labels
- Output shows the original and encoded city values

**Libraries Used:**  
- `pandas`  
- `sklearn.preprocessing.LabelEncoder`

---

### 3. `One-Hot_Encodeing.py`
This script performs **One-Hot Encoding** on a column of city names.

- A simple DataFrame with a `City` column is created
- One-hot encoding is applied using `pd.get_dummies`
- Resulting DataFrame contains binary columns for each unique city


_______________________________________________________

# Numpy 
### 1. `basicNum.py`
Description: Demonstrates basic vector and matrix operations using NumPy.

Operations:

Vector creation (v, w).

Matrix creation (A, B).

Matrix addition (C = A + B).

Matrix multiplication (dot product, D = np.dot(A, B)).

Matrix transpose (A.T).

Matrix inverse (np.linalg.inv(A)).

Matrix determinant (np.linalg.det(A)).

Output: Prints the results of matrix addition and multiplication.

### 2. `nump1.py`
Description: Demonstrates matrix-vector multiplication using NumPy.

Operations:

Matrix creation (x).

Vector creation (w).

Dot product (y = np.dot(x, w)).

Output: Prints the predicted outputs resulting from the dot product.

### 3. `nump2.py`
Description: Computes eigenvalues and eigenvectors of a matrix using NumPy.

Operations:

Matrix creation (A).

Eigenvalue and eigenvector calculation (eig(A)).

Output: Prints the eigenvalues and eigenvectors of the matrix.

### `4. nump3.py`
Description: Demonstrates symbolic differentiation using SymPy.

Operations:

Symbolic variable creation (x).

Function definition (f = x**2).

Derivative calculation (diff(f, x)).

Output: Prints the derivative of the function x^2.

### `5. nump4.py`
Description: Computes basic statistical measures using NumPy.

Operations:

Data list creation (data).

Mean calculation (np.mean(data)).

Median calculation (np.median(data)).

Standard deviation calculation (np.std(data)).

Output: Prints the mean, median, and standard deviation of the data.

__________________________________________________________



###############
# Pandas

### `pandas1.py`
Description: Demonstrates how to create a DataFrame using pandas from a Python dictionary.

Key Features:

Creates a simple dataset of study hours and marks.

Checks for missing (null) values using isnull().sum().

### `pand2.py`
Description: Reads a CSV file and performs basic data cleaning and exploration using pandas.

Key Features:

Loads data from data.csv.

Displays DataFrame info and statistical summary using .info() and .describe().

Cleans the dataset by removing rows with missing values using .dropna().

Saves the cleaned dataset as cleaned_data.csv.


##############
# pythan_basic


### `fileh.py`

This script creates a file named data and writes the string "jjjjjjj" to it.

Purpose: Demonstrates basic file handling operations in Python.

### `List.py`

This script defines a list of fruits, accesses an element by index, and appends new items to the list.

Purpose: Illustrates list operations in Python, including indexing and appending.

### `set.py`

This script creates a set of numbers, automatically removing duplicates, and adds a new element to the set.

Purpose: Shows how sets work in Python, focusing on their uniqueness property and the add method.

###` toupe.py`

This script demonstrates the use of a tuple (immutable sequence) and a dictionary (key-value pairs).

Purpose: Highlights tuple indexing and dictionary value access in Python.

############

# SupervisedLearnig

### `linearRegression.py`

Demonstrates a basic Linear Regression model predicting heart rate based on distance run (in km).

Input: x = [1, 2, 3, 4, 5] (distance in km), y = [10, 13, 15, 18, 21] (heart rate).

Predicts heart rate for 6 km.

### `linearR2.py`

Similar to linearRegression.py, but uses larger values for house price prediction (e.g., square footage vs. price).

Input: x = [2000, 2500, 3000, 3500, 4000] (sq. ft.), y = [1M, 1.3M, 1.5M, 1.8M, 2.1M] (price).

Predicts price for a 6000 sq. ft. house.


### `LogisticReg.py`

A simple Logistic Regression model predicting categorical outcomes (letters a-f) based on numeric input.

Input: x = [1, 2, 3, 4, 5] (years of experience), y = ["a", "c", "d", "e", "f"] (categories).

Predicts the category for 7 years of experience.

### `LogisticReg2.py`

A more advanced example with train-test split and probability predictions.

Input: X (3 features: binary + numeric), y (binary labels 0 or 1).

Outputs:

Predicted class for [2, 1, 100].

Prediction probabilities for the test set.



######
# UnsupervisedLearning

### `K-means.py`
Implements K-Means Clustering on synthetic blob data.

Generates 300 data points grouped into 3 clusters and visualizes them with Matplotlib.

Highlights cluster centers in red.

Use Case: Basic introduction to clustering for data segmentation



### `Svm-Basic.py`
Demonstrates a linear SVM classifier on the Iris dataset.

Splits data into train/test sets (70/30) and evaluates model accuracy.

Key Feature: Uses SVC(kernel='linear') for clear decision boundaries.

Output: Prints test accuracy (e.g., ~97-100%).



### `svm-email-Idf.py`
Email Spam Detection using SVM with TF-IDF text vectorization.

Processes a sample email dataset (spam vs. non-spam labels).

Converts text to numerical features via TfidfVectorizer.

Predicts spam status for new emails (e.g., "Congratulation sid" → "Spam").

Output: Model accuracy and real-time prediction example.