import pandas as pd

data = pd.read_csv("advertising.csv")
#print(data)

#description of data points..
print(data.head(),"\n",data.info(),"\n",data.describe())