import pandas as pd

# load dataset
df = pd.read_csv("sales.csv")

# preview data
print(df.head())

# dataset info
print(df.info())