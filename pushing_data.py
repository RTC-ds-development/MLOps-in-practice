import pandas as pd

d = {'col_1':[1,2], 'col_2':[3,4]}
df = pd.DataFrame(data=d)

df.to_csv('test_data.csv')