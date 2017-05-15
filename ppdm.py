import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
from Color import Color


print(Color.YELLOW + "Opening Database"+ Color.END)
conn = sqlite3.connect('insurance.db')
print(Color.YELLOW + Color.UNDERLINE+ "Reading data ..."+ Color.END)
df = pd.read_sql_query("SELECT * FROM Claims",conn,  coerce_float=True, parse_dates=["Date_Of_Birth", "Policy_Start",
                                                 "Policy_End", "Date_Of_Loss", "Date_Of_Claim"])




print(Color.DARKCYAN + "\n\n\nPreserve Name " + Color.END)
df['Name'] = '*'

print(Color.DARKCYAN + "\n\n\nPreserve Surname " + Color.END)
df['Surname'] = '*'

print(Color.DARKCYAN + "\n\n\nPreserve Party Name" + Color.END)
df['Party_Name'] = '*'

print(Color.DARKCYAN + "\n\n\nPreserve Party Surname" + Color.END)
df['Party_Surname'] = '*'

print(Color.DARKCYAN + "\n\n\nPreserve Policy_Holder_City" + Color.END)
df['Policy_Holder_City'] = '*'

print(Color.DARKCYAN + "\n\n\nPreserve Policy_Holder_Street" + Color.END)
df['Policy_Holder_Street'] = '*'

print(Color.DARKCYAN + "\n\n\nPreserve Policy_Holder_Area" + Color.END)
df['Policy_Holder_Area'] = '*'

print(Color.DARKCYAN + "\n\n\nPreserve Province" + Color.END)
df['Province'] = '*'

print(Color.DARKCYAN + "\n\n\nPreserve Age" + Color.END)
df['Age'] = df['Age'].astype(str).str[:-3].astype(str) + "*"

print(Color.DARKCYAN + "\n\n\nPreserve Date OF Birth" + Color.END)
df['Date_Of_Birth'].fillna(value='0', inplace=True)
tmp = df['Date_Of_Birth'].astype(str).str.replace('-','')
df['Date_Of_Birth'] = tmp.astype(str).str[:-11].astype(np.int64)

print(Color.DARKCYAN + "\n\n\nPreserve Marital Status" + Color.END)
df['Marital_Status'] = df['Marital_Status'].astype(str).str[0:2].astype(str)

print(Color.DARKCYAN + "\n\n\nPreserve Gender" + Color.END)
for index, row in df.iterrows():
    if row.shift(-1)['Gender'] != row['Gender']:
        row['Gender'] = '*'


# df['range'].str.replace(',','-')
print(df.sample(5))
### Write data from df to database
# df.to_sql("daily_flights", conn, if_exists="replace")
