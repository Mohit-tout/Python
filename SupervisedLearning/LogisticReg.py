
from sklearn.linear_model import LogisticRegression
import numpy as np

x = np.array([[1], [2], [3], [4], [5]])

y = np.array(["a", "c", "d", "e", "f"])

model = LogisticRegression()

model.fit(x, y)

pre = model.predict([[7]])
print(f"Predicted category for 6 years experience: {pre[0]}")

