import pandas as pd

arquivo = "salarios.csv"

df = pd.read_csv(arquivo)

print(df.head())
print(df["Job Titles"].value_counts())