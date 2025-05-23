import pandas as pd
df = pd.read_csv('data.csv')

print("Missing values per column:")
print(df.isnull().sum())

df['Age'].fillna(df['Age'].mean(), inplace=True)

df.dropna(inplace=True)

print("\nData after cleaning:")
print(df.head())