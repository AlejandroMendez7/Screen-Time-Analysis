import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv("./data/Activity_history.csv")

# DATA CLEANING                                 Review

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

df4 = (
    df.loc[df["App name"] != "Screen off (locked)"]
    .groupby("Date")
)

average_time_per_day = df4["Duration"].sum()

print(average_time_per_day)

# BAR PLOT

average_time_per_day_days = average_time_per_day.index.to_list()

average_time_per_day_time = average_time_per_day.values.tolist()

# print(average_time_per_day_time)
# print(type(average_time_per_day_time[0]))

count = 0

for i in average_time_per_day_time:
    i = i / 3_600_000_000_000                   # passage from ns to h
    average_time_per_day_time[count] = i
    count += 1

# print(average_time_per_day_time)
    
plt.style.use('dark_background')

fig, ax = plt.subplots()

ax.grid()

ax.bar(average_time_per_day_days, 
       average_time_per_day_time, 
       width=0.75, 
       color= "#367C65",
       edgecolor="black", 
       linewidth=1,
)

fig.set_figwidth(11, forward=True)
fig.set_figheight(6, forward=True)

ax.set_title("Hours per day")
ax.set_xlabel("Days")
ax.set_ylabel("Hours")

# plt.show()