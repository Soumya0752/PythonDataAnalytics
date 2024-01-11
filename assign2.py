import pandas as pd
#Convert Dictionary data to csv
employees= {'name':['Roy','Raj','Jai'],'age':[35,26,29],
      'salary':[30000,40000,50000]}
df=pd.DataFrame(employees)
#print(df)
'''
name  age  salary
0  Roy   35   30000
1  Raj   26   40000
2  Jai   29   50000
'''
df.to_csv('empdata.csv',index=False)
