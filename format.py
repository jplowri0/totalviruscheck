from operator import truediv
import pandas as pd 

#Dropping any row ending in /*
df = pd.read_csv("input.csv")
df = df[~df['URL'].str.endswith('*')]
df.to_csv("inputFormatted.csv")

#Selecting all the rows containing http*
df2 = df[df['URL'].str.contains('http\*:')] 

#Changing the http* to https
df3 = pd.DataFrame(columns=['URL'])
df3['URL'] = df2['URL'].str.replace('\*', 's', regex=True)

#Changing the http* to https
df4 = pd.DataFrame(columns=['URL'])
df4['URL'] = df2['URL'].str.replace('\*', '', regex=True)

#Dropping rows with http*
df5 = df[~df['URL'].str.contains('http\*')]

#Now Concatenate the different data frames
df6 = pd.concat([df3,df4,df5])

df6.to_csv("inputCleaned.csv", index=False)

