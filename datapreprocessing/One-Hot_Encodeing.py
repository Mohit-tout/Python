import pandas as pd

df=pd.DataFrame({'City':['Delhi','Khandwa','Mumbai','Delhi']})
df=pd.get_dummies(df,columns=['City'],dtype=int)
print(df)