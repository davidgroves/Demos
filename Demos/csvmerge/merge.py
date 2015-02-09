#!/usr/bin/env python3

import pandas as pd

df1 = pd.read_csv("1.csv", names=["id", "animal"])
df2 = pd.read_csv("2.csv", names=["id", "animal"])

for id, animal in zip(df1['id'], df1['animal']):
    if id not in df2['id']:
        print (id, animal)