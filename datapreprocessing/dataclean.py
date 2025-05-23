import pandas as pd
data={
    'name': ['Amit','Sid','LAk'],
    'Age': [25,None,22]
}

df=pd.DataFrame(data)

df['Age']=df['Age'].dropna()
print(df.dropna())