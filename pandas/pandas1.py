import pandas as pd

data= {'Hours': [1,2,3,4,5], 'Marks':[40,50,60,70,80]}
df=pd.DataFrame(data)

print(df.isnull().sum())