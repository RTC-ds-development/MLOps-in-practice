import pandas as pd
from os.path import exists

d = {'col_1':[1,2], 'col_2':[3,4]}
df = pd.DataFrame(data=d)

df.to_csv('test_data.csv')

file_exists = exists('test_data.csv')

print(file_exists)
