import pandas as pd
import numpy as np
data ={"Name":["Alice","Bob","Charlie","David","Eva"],
       "Age":[24,27,22,32,29],
         "City":["New York","Los Angeles","Chicago","Houston","Phoenix"],
        "Salary":[70000,80000,65000,90000,75000]

}
df = pd.DataFrame(data)
print(df)
df.insert(3,"Bonus",[1000,1200,1300,1400,1100])
print("\nDataFrame after inserting Bonus column:")
print(df)


#df=pd.read_csv("sales_data_sample (1).csv",encoding='latin1')
#print(df.head(10))
#print("\nStatistical Summary:")
#print(df.info())
#print (df.isnull().sum())
#print(df.describe())
#print(f'shape:{df.shape}')
#print(f'columns:{df.columns}')
#coloum =df["COUNTRY"]
#india=df[df["COUNTRY"]=="France"]
#ind=print(india)
#print("\nSales in India:" )
#print(coloum)