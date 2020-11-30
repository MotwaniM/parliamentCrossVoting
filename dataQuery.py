import requests
import pandas
import json
import time
import os

## csv file of commons disvisions to analyse
df = pandas.read_csv("commonsdivisions/commonsdivisions.csv")
csv_files = os.listdir("commonsdivisions/")

for file in csv_files:

    df = pandas.read_csv(file)

    for index, row in df.iterrows():

        ## Set loop delay to avoid rate breach: 1 second
        time.sleep(1)

        # obtain output as json
        resource_id = row["uri"][-7:]
        url = "http://lda.data.parliament.uk/commonsdivisions/id/"+resource_id+".json"
        print(url)
        response = requests.get(url)
        fname = "json_data/" + row["uri"][-7:] +".txt"
        #Save json to txt for processing.
        with open(fname, 'w') as outfile:
            json.dump(response.json(), outfile)

        if index == 5:
            break
    break
