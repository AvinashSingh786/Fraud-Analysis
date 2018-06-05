import pandas as pd
import numpy as np
import sqlite3
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

print(Color.DARKCYAN + "\n\n\nPreserve Area" + Color.END)
df['Area'] = '*'

print(Color.DARKCYAN + "\n\n\nPreserve Age" + Color.END)
df['Age'] = df['Age'].astype(str).str[:-3].astype(str) + "*"

print(Color.DARKCYAN + "\n\n\nPreserve Date OF Birth" + Color.END)
df['Date_Of_Birth'].fillna(value='0', inplace=True)
tmp = df['Date_Of_Birth'].astype(str).str.replace('-','')
df['Date_Of_Birth'] = tmp.astype(str).str[:-11].astype(np.int64)

print(Color.DARKCYAN + "\n\n\nPreserve Marital Status" + Color.END)
df['Marital_Status'] = df['Marital_Status'].astype(str).str[0:2].astype(str)

print(Color.DARKCYAN + "\n\n\nPreserve Gender, Insure_ID, Kind_Of_Loss" + Color.END)
for index, row in df.iterrows():
    if index == 0:
        prev = row['Gender']
    if prev == row['Gender']:
        df.loc[index,'Gender'] = '*'
    prev = row['Gender']

    if index == 0:
        prevIn = row['Insured_ID']
    if prevIn == row['Insured_ID']:
        df.loc[index,'Insured_ID'] = '*'
    prevIn = row['Insured_ID']


    if index == 0:
        prevK = row['Kind_Of_Loss']
    if prevK == row['Kind_Of_Loss']:
        df.loc[index,'Kind_Of_Loss'] = '*'
    prevK = row['Kind_Of_Loss']
    print("\rComplete: " +Color.GREEN+ str((index/100000.0)*100)+ Color.END + "%", end="")

print(df.sample(5))


print(Color.DARKCYAN + "\n\n\nPreserve Fraud Claim Indicator" + Color.END)
df['Fraudulent_Claim'] = df['Fraudulent_Claim'].astype(str).str.replace('T','*').astype(str).str.replace('F','')

print(Color.DARKCYAN + "\n\n\nPreserve Broker ID" + Color.END)
df['Broker_ID'] = df['Broker_ID'].astype(str).str[3:].astype(np.int64)

print(Color.DARKCYAN + "\n\n\nPreserve Policy_Holder_Postal" + Color.END)
df['Policy_Holder_Postal'] = df['Policy_Holder_Postal'].astype(str).str[:-2].astype(str) + "**"
df['Claim_ID'] = df['Claim_ID'].astype(int)
print(df.sample(5))

####### Write data from df to database
print(Color.YELLOW + "\n\n\nWriting Data to Database" + Color.END)
df.to_sql("Claims", conn, if_exists="replace", index=False)
