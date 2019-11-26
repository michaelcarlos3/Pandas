import pandas as pd

x=pd.read_csv('cars.csv')

a = x.loc[1:9:2]
b = x.loc[0:0]
c = x.loc[[23],['cyl']]
d = x.loc[[1,28,18],['cyl','gear']]