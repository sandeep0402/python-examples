import pandas as pd

csv = pd.read_csv('data/titanic.csv')
csv.head(8)
csv.dtypes

csv.to_excel("data/titanic_output.xlsx", sheet_name="passengers", index=False)
