import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X=np.array([
    [0,1,100],
    [1,1,50],
    [0,0,100],
])


y=np.array([1,1,0])

X_train, X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,state=4,random_state=42)
model=LogisticRegression()

model.fit(X_train, y_train)
pre = model.predict([[2,1,100]])

print( pre[0])

print("Prediction probabilities:", model.predict_proba(X_test))