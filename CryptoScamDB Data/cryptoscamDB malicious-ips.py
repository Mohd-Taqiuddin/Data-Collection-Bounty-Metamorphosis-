# Returns a list of addresses and their associated malicious entries
import http.client
import pandas as pd
import csv

conn = http.client.HTTPSConnection("api.cryptoscamdb.org")
payload = ''
headers = {}
conn.request("GET", "/v1/addresses", payload, headers)
res = conn.getresponse()
data = res.read()
# print(data.decode("utf-8"))

data = data.decode("utf-8")

df = pd.read_json(data)
df = df['result']
data = df.to_dict()
data = data.values()
# print(data)

df = pd.DataFrame(data)
df = df[0]
data = df.to_dict()
data = list(data.values())

# print(data[0])
# print(df)

columns = data[0].keys()

with open('test.csv', 'w', encoding='utf8', newline='') as output_file:
    fc = csv.DictWriter(output_file, 
                        fieldnames=columns,

                       )
    fc.writeheader()
    fc.writerows(data)

