# Returns a list of the scams currently tracked by CryptoScamDB.
import http.client
import pandas as pd
import csv

conn = http.client.HTTPSConnection("api.cryptoscamdb.org")
payload = ''
headers = {}
conn.request("GET", "/v1/scams", payload, headers)
res = conn.getresponse()
data = res.read()

# print(data.decode("utf-8"))
data = data.decode("utf-8")

df = pd.read_json(data)
df = df['result']
data = df.to_dict()
data = list(data.values())
# print(data)

# print(df)

with open('test.csv', 'w', encoding='utf8', newline='') as output_file:
    fc = csv.DictWriter(output_file, 
                        fieldnames=data[0].keys(),

                       )
    fc.writeheader()
    fc.writerows(data)