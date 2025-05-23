from sklearn.linear_model import LinearRegression
import numpy as np

x=np.array([[2000],[2500],[3000],[3500],[4000]])
y=np.array([1000000,1300000,1500000,1800000,2100000])


model=LinearRegression()

model.fit(x,y)

pre=model.predict([[6000]])
print(f"Predicted heart rate when will run 6 km: {pre[0]} beat")

