import pandas as pd 
import numpy as np 
import datetime as dt

df = pd.read_csv("./data/Activity_history.csv")

# DATA CLEANING

df = df.drop(index=df.index[-3:])               # I removed the last three lines

df.info()                                       # I check for null values on the df

# TIMES UNLOCKED

print(df.value_counts(["App name"]))

# MOST AND LEAST USED APP

df["Duration"] = pd.to_timedelta(df.Duration)   # str to timedelta

df2 = df.drop(["Date", "Time"], axis=1)

sums_per_app = (                                # Total time per app in one df
    df2.groupby("App name")
    ["Duration"]
    .sum()
    .reset_index()
) 

""" print(sums_per_app) """

most_used = (
    sums_per_app.sort_values(
        by="Duration", 
        ascending=False
        )
    ["App name"]
    .head(3)
)

print(most_used)

least_used = (
    sums_per_app.sort_values(
        by="Duration", 
        ascending=False
        )
    ["App name"]
    .head(3)
)

print(least_used)
