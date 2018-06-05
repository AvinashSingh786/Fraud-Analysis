import pandas as pd
import numpy as np
import sqlite3
from Color import Color


print(Color.YELLOW + "Opening Database"+ Color.END)
conn = sqlite3.connect('insurance.db')
print(Color.YELLOW + Color.UNDERLINE+ "Reading data ..."+ Color.END)
df = pd.read_sql_query("SELECT * FROM Claims",conn,  coerce_float=True, parse_dates=["Date_Of_Birth", "Policy_Start",
                                                 "Policy_End", "Date_Of_Loss", "Date_Of_Claim"])

print(Color.GREEN + "\n\n\nDirty Data" + Color.END)
df.loc[2, "Claim_ID"] = np.nan
df.loc[30, "Postal_Code"] = ''
df.loc[40, "Broker_ID"] = np.nan
df.loc[22, "Date_Of_Claim"] = None
df.loc[23, "Date_Of_Loss"] = None
df.loc[44, "Sum_Insured"] = -5000.01
df.loc[50, "Date_Of_Loss"] = pd.Timestamp("2018-03-01 00:00:00", tz=None)
df.loc[200, "Policy_Start"] = pd.Timestamp("2018-03-01 00:00:00", tz=None)
df.loc[500, "Policies_Revenue"] = None
df.loc[100, "Policies_Revenue"] = None
df.loc[520, "Policies_Revenue"] = None
df.loc[1, "Policies_Revenue"] = None

####### Write data from df to database
# print(Color.YELLOW + "\n\n\nWriting Data to Database" + Color.END)
# df.to_sql("Claims", conn, if_exists="replace", index=False)

# print(Color.YELLOW + "Opening Database"+ Color.END)
# conn = sqlite3.connect('insurance.db')
# print(Color.YELLOW + Color.UNDERLINE+ "Reading data ..."+ Color.END)
# df = pd.read_sql_query("SELECT * FROM Claims",conn,  coerce_float=True, parse_dates=["Date_Of_Birth", "Policy_Start",
#                                                  "Policy_End", "Date_Of_Loss", "Date_Of_Claim"])

if 'Name' in df.columns:
    print(Color.DARKCYAN + "\n\n\nRemove Name" + Color.END) 
    del df['Name']

if 'Surname' in df.columns:
    print(Color.DARKCYAN + "\n\n\nRemove Surname" + Color.END)
    del df['Surname']

if 'Party_Name' in df.columns:
    print(Color.DARKCYAN + "\n\n\nRemove Party_Name" + Color.END)
    del df['Party_Name']

if 'Party_Surname' in df.columns:
    print(Color.DARKCYAN + "\n\n\nRemove Party_Surname" + Color.END)
    del df['Party_Surname']

if 'Policy_Holder_Street' in df.columns:
    print(Color.DARKCYAN + "\n\n\nRemove Policy_Holder_Street" + Color.END)
    del df['Policy_Holder_Street']

if 'Policy_Holder_Area' in df.columns:
    print(Color.DARKCYAN + "\n\n\nRemove Policy_Holder_Area" + Color.END)
    del df['Policy_Holder_Area']

if 'Province' in df.columns:
    print(Color.DARKCYAN + "\n\n\nRemove Province" + Color.END)
    del df['Province']
    
if 'Area' in df.columns:
    print(Color.DARKCYAN + "\n\n\nRemove Area" + Color.END)
    del df['Area']

if 'Policy_Holder_City' in df.columns:
    print(Color.DARKCYAN + "\n\n\nRemove Policy_Holder_City" + Color.END)
    del df['Policy_Holder_City']

if 'index' in df.columns:
    del df['index']


print(Color.GREEN + "\n\n\nHandle Policy Start and end Date" + Color.END)
df = df[(df['Policy_End'] >= df['Policy_Start'])]

print(Color.GREEN + "\n\n\nHandle Date of loss and claim" + Color.END)
df = df[(df['Date_Of_Claim'] >= df['Date_Of_Loss'])]


print(Color.GREEN + "\n\n\nHandle Claim_ID" + Color.END)
df['Claim_ID'].dropna( how='any', inplace=True )
df['Claim_ID'] = df['Claim_ID'].astype(int)


print(Color.GREEN + "\n\n\nHandle Postal_Code" + Color.END)
df['Postal_Code'].dropna( how='any', inplace=True)

print(Color.GREEN + "\n\n\nHandle Broker_ID" + Color.END)
df['Broker_ID'].dropna( how='any', inplace=True)

print(Color.GREEN + "\n\n\nHandle Date_Of_Claim" + Color.END)
df['Date_Of_Claim'].dropna( how='any', inplace=True)

print(Color.GREEN + "\n\n\nHandle Date_Of_Loss" + Color.END)
df['Date_Of_Loss'].dropna( how='any', inplace=True)

print(Color.GREEN + "\n\n\nHandle Broker_ID" + Color.END)
df['Broker_ID'].dropna( how='any', inplace=True)

print(Color.GREEN + "\n\n\nHandle Sum_Insured" + Color.END)
df['Sum_Insured'].dropna( how='any', inplace=True)
df = df[ df['Sum_Insured'] > -0.0]


print(Color.GREEN + "\n\n\nHandle Policies_Revenue" + Color.END)
df['Policies_Revenue'].fillna(value=df['Policies_Revenue'].mean(),inplace=True)



#    ;; ; ; ;; ; ;
# df.interpolate()91377 91417
#  ' ' ' ' ' ' ' ''
print(df.head())
df.dropna( how='any', inplace=True )
print(df.isnull().sum())
####### Write data from df to database
print(Color.YELLOW + "\n\n\nWriting Data to Database" + Color.END)
df.to_sql("Claims", conn, if_exists="replace", index=False)
