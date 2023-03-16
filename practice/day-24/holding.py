import pandas

holdings = pandas.read_csv('./holdings.csv')
holdings["total_cost"] = holdings["Qty."] * holdings["Avg. cost"]
print(holdings[["Instrument","Qty.", "Avg. cost", "total_cost"]])

print(holdings["Qty."].describe())


