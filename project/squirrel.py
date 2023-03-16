import pandas as pd

df = pd.read_csv('/Users/nrangasa/Downloads/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

print(df.rename(columns={'Primary Fur Color':'Fur Color'}).groupby(["Fur Color"])["Fur Color"].count().reset_index(name="count"))

