import pandas as pd

data = pd.read_csv('/Users/nrangasa/personal/Nifty50.csv')

df = data.agg(
    {

        "P/E": ["min", "max", "mean", "median"],

        "P/B": ["min", "max", "mean", "median"],

        "Div Yield": ["min", "max", "mean", "median"],

    }
)

print(df['P/E'].round(2))
print(df['P/B'].round(2))
print(df['Div Yield'].round(2))
