from duneanalytics import DuneAnalytics
import pandas as pd
import unicodecsv as csv

# initialize client
dune = DuneAnalytics('taqi', '927085481qQ!')

# try to login
dune.login()

# fetch token
dune.fetch_auth_token()

# fetch query result id using query id
# query id for any query can be found from the url of the query:
# for example: 
# https://dune.com/queries/4494/8769 => 4494
# https://dune.com/queries/3705/7192 => 3705
# https://dune.com/queries/3751/7276 => 3751

result_id = dune.query_result_id(query_id=1135564)

# fetch query result
data = dune.query_result(result_id)

# print(data)

data = data['data']
columns = data['query_results'][0]['columns']
data = data['get_result_by_result_id']

df = pd.DataFrame(data)
df = df['data']
data = df.to_dict()
data = data.values()
print(data)



with open('test.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, columns)
    dict_writer.writeheader()
    dict_writer.writerows(data)

