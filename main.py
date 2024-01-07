import pandas as pd 
import numpy as np 

df = pd.read_csv("./data/Activity_history.csv")

# DATA CLEANING

df = df.drop(index=df.index[-3:]) # Here I remove the last three lines and save the modified file locally in "df"

df.info() # I make sure there are no Null values on the dataframe
