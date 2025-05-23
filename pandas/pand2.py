import pandas as pd
df = pd.read_csv("data.csv")
print("Original DataFrame:\n", df)
print("\nInfo:")
print(df.info())
print("\nDescribe:\n", df.describe())

cleaned_df = df.dropna()

print("\nCleaned DataFrame (dropna):\n", cleaned_df)

cleaned_df.to_csv("cleaned_data.csv", index=False)
