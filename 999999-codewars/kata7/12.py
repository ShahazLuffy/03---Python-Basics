import pandas as pd

# Read the Excel file
df = pd.read_excel("C:/Users/Fava/Desktop/i.xlsx")

# Extract the column you want as a list
column_list = df["karim"].tolist()

print(column_list)