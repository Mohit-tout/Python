import pandas as pd 
from sklearn.preprocessing import LabelEncoder

df=pd.DataFrame({'City': ['Atut', 'Khandwa','hosangabad','burhanpur']})
le=LabelEncoder()
df['City_encoder']=le.fit_transform(df['City'])

print(df)