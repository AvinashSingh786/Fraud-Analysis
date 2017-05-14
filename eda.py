import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
from Color import Color


style.use('ggplot')
print(Color.YELLOW + "Opening Database"+ Color.END)
conn = sqlite3.connect('insurance.db')
print(Color.YELLOW + Color.UNDERLINE+ "Reading data ..."+ Color.END)
df = pd.read_sql_query("SELECT * FROM Claims",conn,  coerce_float=True, parse_dates=["Date_Of_Birth", "Policy_Start",
                                                 "Policy_End", "Date_Of_Loss", "Date_Of_Claim"])

# print(df.head())


##### Get shape of data
# print(Color.CYAN + "Number of Rows and Columns: "+ Color.END + str(df.shape))


##### Get info on data types
# print(Color.DARKCYAN + "\n\n\nData Type information: " + Color.END)
# df.info()


##### Get frequency counts
# print(Color.BLUE+"\n\n\nFrequency of Name\n "+Color.END)
# print(df['Name'].value_counts( dropna=False))
# name = df.groupby('Name')['Name'].count().plot( kind='bar', title='Name Distribution', grid=True, legend=True, sort_columns=True)
# ticks = name.xaxis.get_ticklocs()
# ticklabels = [l.get_text() for l in name.xaxis.get_ticklabels()]
# name.xaxis.set_ticks(ticks[::100])
# name.xaxis.set_ticklabels(ticklabels[::100])
# plt.show()

# print(Color.BLUE+"\n\n\nFrequency of Surname\n "+Color.END)
# print(df['Surname'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Age\n "+Color.END)
# print(df['Age'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Gender\n "+Color.END)
# print(df['Gender'].value_counts( dropna=False))
# df.groupby('Gender')['Gender'].count().plot( kind='bar', title='Gender Distribution', grid=True, legend=True)
# plt.show()

# print(Color.BLUE+"\n\n\nFrequency of Marital Status\n "+Color.END)
# print(df['Marital_Status'].value_counts( dropna=False))
# df.groupby('Marital_Status')['Marital_Status'].count().plot( kind='pie', title='Marital Status Distribution', sort_columns=True,  grid=True, legend=True)
# plt.show()

# print(Color.BLUE+"\n\n\nFrequency of Date Of Birth\n "+Color.END)
# print(df['Date_Of_Birth'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Sum Insured\n "+Color.END)
# print(df['Sum_Insured'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Policies Revenue\n "+Color.END)
# print(df['Policies_Revenue'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Policy Start Date\n "+Color.END)
# print(df['Policy_Start'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Policy End Date\n "+Color.END)
# print(df['Policy_End'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Fraudulent Claims\n "+Color.END)
# print(df['Fraudulent_Claim'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Fraud Reason\n "+Color.END)
# print(df['Fraudulent_Claim_Reason'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Date Of Loss\n "+Color.END)
# print(df['Date_Of_Loss'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Date Of Claim \n "+Color.END)
# print(df['Date_Of_Claim'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Broker ID\n "+Color.END)
# print(df['Broker_ID'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Insurer ID\n "+Color.END)
# print(df['Insured_ID'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Kind Of Loss\n "+Color.END)
# print(df['Kind_Of_Loss'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Claim Amount\n "+Color.END)
# print(df['Claim_Amount'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Party Name\n "+Color.END)
# print(df['Party_Name'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Party Surname\n "+Color.END)
# print(df['Party_Surname'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Service Provider\n "+Color.END)
# print(df['Service_Provider'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Policy Holder Street Name\n "+Color.END)
# print(df['Policy_Holder_Street'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Policy Holder Province\n "+Color.END)
# print(df['Policy_Holder_Province'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Policy Holder City\n "+Color.END)
# print(df['Policy_Holder_City'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Policy Holder Area\n "+Color.END)
# print(df['Policy_Holder_Area'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Policy Holder Postal Number\n "+Color.END)
# print(df['Policy_Holder_Postal'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Province where loss occurred\n "+Color.END)
# print(df['Province'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of City where loss occurred\n "+Color.END)
# print(df['City'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Area where loss occurred\n "+Color.END)
# print(df['Area'].value_counts( dropna=False))

# print(Color.BLUE+"\n\n\nFrequency of Postal Code where loss occurred\n "+Color.END)
# print(df['Postal_Code'].value_counts( dropna=False))





# claim = df[(df['Date_Of_Claim'] > '2000-1-1') & (df['Date_Of_Claim'] <= '2000-06-30')]
# claim.info()
# claim.plot( x='Claim_Amount', y='Sum_Insured', title='Claim VS Insured Amount for 2000', sort_columns=True, kind='kde' )
#
# plt.show()

##### Numeric data info
# print(Color.DARKCYAN + "\n\n\nNumeric Data Information: " + Color.END)
# print(df.describe())


# df.plot()

# plt.show()


# df.mean().plot()
# plt.show()

##### Age distribution



##### Age for gender
# print(Color.CYAN + "Generating figure Gender VS Age"+ Color.END)
# df.groupby('Gender').Age.plot(kind='kde', legend=True, title='Gender vs Age', grid=True)
# plt.show()



##### Frequency of Age [Scaling is needed]
# print(Color.CYAN + "Generating figure Frequency of Age"+ Color.END)
# df.groupby('Age').Age.plot(kind='hist', x='Age', y='Frequency', sort_columns=True, title='Frequency of Ages', grid=True)
# plt.show()


##### Number of payout per month

##### Number of payout per year

##### Sum payouts year

##### Sum payouts month


print("\n\n\nMax Sum Insured: "+str(df['Sum_Insured'].idxmax()))