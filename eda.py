import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
from matplotlib import style
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
# print(Color.BLUE+"\n\n\nFrequency of Names\n "+Color.END+df['Age'].value_counts( dropna=False))


claim = df[(df['Date_Of_Claim'] > '2000-1-1') & (df['Date_Of_Claim'] <= '2000-06-30')]
claim.info()
# claim.plot( x='Claim_Amount', y='Sum_Insured', title='Claim VS Insured Amount for 2000', sort_columns=True, kind='kde' )
#
# plt.show()
##### Numeric data info
# print("\n\n\nNumeric data analysis\n"+df.describe())


# df.plot() #plot(kind='scatter', x='SepalRatio', y='PetalRatio'))

# plt.show()


# df.mean().plot().show()


##### Age distribution



##### Age for gender
print(Color.CYAN + "Generating figure Gender VS Age"+ Color.END)
df.groupby('Gender').Age.plot(kind='kde', legend=True, title='Gender vs Age', grid=True)
plt.show()



##### Frequency of Age [Scaling is needed]
# print(Color.CYAN + "Generating figure Frequency of Age"+ Color.END)
# df.groupby('Age').Age.plot(kind='hist', x='Age', y='Frequency', sort_columns=True, title='Frequency of Ages', grid=True)
# plt.show()


##### Number of payout per month

##### Number of payout per year

##### Sum payouts year

##### Sum payouts month


print("\n\n\nMax Sum Insured: "+str(df['Sum_Insured'].idxmax()))