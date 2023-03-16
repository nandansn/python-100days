import requests as req
import pandas as pd

host_name = "https://maniiapp.herokuapp.com/api/v1/maniiapp"
url_path = "{}/nifty/pe/aggregate".format(host_name)

res = req.get(url_path)


df = pd.json_normalize(res.json(), max_level=1)

print(df)

f = df["PE.Average"].le(15).to_list()

buying = [i for i in f if i]

print("Buying oppurtunity: ",len(buying))


print(df["PE.Average"].max())
print(df["PE.Average"].min())
print(df["PE.Average"].mean())


