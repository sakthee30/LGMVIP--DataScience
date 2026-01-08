
import pandas as pd
import os

data = pd.read_json(r"C:\Users\sakthep\Downloads\new.json")
print(data)

curent_path = os.getcwd()
print(curent_path)
path = os.path.join(curent_path,"new1.json")
# path = r"C:\Users\sakthep\Downloads\new1.json"
data.to_json(path,index=False)

#To extract Table names from json

import json
with open('new1.json','r',encoding='utf-8') as file:
    data = json.load(file)

table_names = [table["table_name"] for table in data.get("tables", [])]
#table_names = list(data.keys())
#table_names = [table["table_name"] for table in data["tables"]]
print(table_names)

import json
with open(r"C:\Users\sakthep\Downloads\new.json", "r", encoding="utf-8") as f:
    data = json.load(f)
table_names = [table["table_name"] for table in data.get("tables", [])]
print(table_names)


#To extract column name from json
import json
with open(r"C:\Users\sakthep\Downloads\new.json",'r',encoding='utf-8') as f:
    data = json.load(f)

column_names = []

for table in data.get("tables",[]):
    for column in table.get("columns",[]):
        name = column.get("column_name")
        if name:
            column_names.append(name)
print(column_names)
