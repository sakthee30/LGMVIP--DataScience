import pandas as pd
import openpyxl

data = {
    'Name': ['Sakthee', 'Jai', 'Vani'],
    'Age': [23, 18, 33]
}

#read dataframe 
df = pd.DataFrame(data)
print(df)

#write dataframe into excel
df.to_excel('output.xlsx')


import pandas as pd
data = {
    'Name': ['Sakthee', 'Jai', 'Vani'],
    'Age': [23, 18, 33]
}
df = pd.DataFrame(data)
print(df)

#write dataframe into excel
df.to_csv('output.csv')


import pandas as pd
import json

data = {
    'Name': ['Sakthee', 'Jai', 'Vani'],
    'Age': [23, 18, 33]
}
df = pd.DataFrame(data)
print(df)

#write dataframe into excel
df.to_json('output.json')

#Converting dataframe into csv, excel, json
import pandas as pd
df= pd.read_csv('output.csv')
print(df)


import pandas as pd
df = pd.read_json('output.json')
# print(df)


df=pd.read_excel('output.xlsx')
print(df)
# print(df.shape)

new_df = df.drop(df.columns[df.columns.str.contains('Unnamed', case=False)], axis=1, inplace=True)
print(df)
print("*************************")
print(new_df)