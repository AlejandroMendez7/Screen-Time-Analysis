import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

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

# AVERAGE TIME PER DAY

df3 = df.drop(["Time"], axis=1)

average_time = (
    str(
        df3.groupby("Date")
        ["Duration"]
        .sum()
        .mean()
    )
    .split(".")[0]
)

if "0 days" in average_time: average_time = average_time.strip("0 days")

""" 
elif "days" in average_time:                    # Review
    avg_hs_days = average_time.split("")[0]
    ...

"""

print(average_time)

# DAY WITH THE MOST HOURS

day_most_hours = (
    df3.groupby("Date")
    ["Duration"]
    .sum()
    .head(1)
    .index
    .values
)

day_most_hours = (
    str(day_most_hours)
    .translate(
        str.maketrans("", "", "[]'")
    )
)

print(day_most_hours)

# DATA VISUALIZATION

# TIME SPENT PER DAY

df4 = df.loc[df["App name"] != "Screen off (locked)"]

df4 = df4.groupby("Date")

average_time_per_day = df4["Duration"].sum()

print(average_time_per_day)
