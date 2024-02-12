import pandas as pd
 
df=pd.read_csv("pivot.csv").set_index('first_name')
df=df.drop('id',axis=1)
df=pd.get_dummies(df.stack(),columns=['B','C']).groupby(level=0).sum()
print(df)
