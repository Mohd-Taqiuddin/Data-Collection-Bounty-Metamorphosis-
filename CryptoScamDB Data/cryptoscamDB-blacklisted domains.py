# Returns a list of blacklisted domains.
import http.client
import pandas as pd
import csv

conn = http.client.HTTPSConnection("api.cryptoscamdb.org")
payload = ''
headers = {}
conn.request("GET", "/v1/blacklist", payload, headers)
res = conn.getresponse()
data = res.read()
# print(data.decode("utf-8"))

data = data.decode("utf-8")

df = pd.read_json(data)
df = df['result']

# print(df)

# columns = 'blacklisted_domains'

# with open('test.csv', 'w', encoding='utf8', newline='') as output_file:
#     fc = csv.DictWriter(output_file, 
#                         fieldnames=columns,

#                        )
#     fc.writeheader()
#     fc.writerows(data)

df.to_csv('test.csv', encoding='utf-8', index=False)
