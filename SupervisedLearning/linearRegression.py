from sklearn.linear_model import LinearRegression
import numpy as np

x=np.array([[1],[2],[3],[4],[5]])
y=np.array([10,13,15,18,21])


model=LinearRegression()

model.fit(x,y)

pre=model.predict([[6]])
print(f"Predicted heart rate when will run 6 km: {pre[0]} beat")
