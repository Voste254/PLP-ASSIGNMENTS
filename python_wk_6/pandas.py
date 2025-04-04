import pandas as pd
data = {'name':["Andrew","Boss","Steve","Emma"],
        "age":[26,28,21,14],
        "city":["mombasa","chuka","nakuru","kendu"]}

df=pd.DataFrame(data)
df['salary']=[2300,3400,6550,4500]
print(df)
