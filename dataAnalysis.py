import requests
import pandas as pd
import json
import re
import os

## to do: extract mps, vote and memberParty
##

## find json files in data directory:
files = os.listdir("json_data")

party_arr = []
vote_arr = []
mp_arr = []

columns = ["MP", "Party", "Vote", "title", "date"]

primary_df = pd.DataFrame(columns=columns)

for f in files:

## read stored json file for common commonsdivisions
    with open(("json_data/" + f)) as json_f:
        json_data = json.load(json_f)

    members = json_data["result"]["primaryTopic"]["vote"]

    ## storing details for each recorded mps votes:
    for i in members:

        match_vote = re.search("#\w{6,}$", i["type"])
        party = i["memberParty"]
        vote = match_vote.group(0)[1:]
        mp = i["memberPrinted"]["_value"]

        party_arr.append(party)
        vote_arr.append(vote)
        mp_arr.append(mp)


    df = pd.DataFrame(list(zip(mp_arr, party_arr, vote_arr)), columns = ["MP", "Party", "Vote"])
    df["title"] = json_data["result"]["primaryTopic"]["title"]
    df["date"] = json_data["result"]["primaryTopic"]["date"]["_value"]
    print(df)
    primary_df = pd.concat([primary_df, df])

primary_df.to_csv("vote_data.csv")
