import pandas as pd
#print(dir(pd))
df=pd.read_csv('https://raw.githubusercontent.com/AnudipAE/DANLC/master/salesdata.csv')
#print(df)
#print(df.head())
#print(df.tail())
#print(type(df))
print(type(df['Region']))
u=set(df['Region'])
print(u)
