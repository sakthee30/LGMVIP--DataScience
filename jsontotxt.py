#reading data from json and writing to txt file
import json
from datetime import datetime

with open('jsoutput.json', 'r') as file:
    data = json.load(file)

datasources = data.get("data_sources", {}).get("datasources", [])

output_file_path = r"C:\Users\sakthep\OneDrive - Capgemini\Desktop\sample.txt"

with open(output_file_path, 'w') as txt_file:
    for datasource in datasources:
        filename = datasource.get("name", "Default Value")
        caption = datasource.get("caption", "Default Value")
        connection_name = datasource.get("connection_name", "Default Value")
        current_time = datetime.now().strftime("%H:%M:%S")


        txt_file.write(f"filename: {filename}\n")
        txt_file.write(f"caption: {caption}\n")
        txt_file.write(f"connection_name: {connection_name}\n")
        txt_file.write(f"Values successfully mapped to the text file at {datetime.now().strftime('%H:%M:%S')}")
       
import json
input_path = r"C:\Users\sakthep\Downloads\datasource_metadata.json"
with open(input_path, 'r') as file:
    data = json.load(file)

datasources = data.get("datasources", [])

output_file_path = r"C:\Users\sakthep\OneDrive - Capgemini\Desktop\sample2.txt"

with open(output_file_path, 'w') as txt_file:
    for datasource in datasources:
        tables = datasource.get("tables", [])
        for table in tables:
            source_name = table.get("source_name", "Default Value")
            table_name = table.get("table_name", "Default Value")
            
            txt_file.write(f"source_name : {source_name}\n")
            txt_file.write(f"table_name  : {table_name}\n")

import json
input_path = r"C:\Users\sakthep\Downloads\datasource_metadata.json"
with open(input_path, 'r') as file:
    data = json.load(file)

datasources = data.get("datasources",[])
output_file_path = r"C:\Users\sakthee\OneDrive - Capgemini\Desktop\sample2.txt"

with open(output_file_path, 'w') as txt_file:
    for datasource in datasources:
        tables = datasource.get("tables", [])
        for table in tables:
            columns = table.get("columns", [])
            for column in columns:
                if column.get("tableau_type") == "integer":
                    cname = column.get("column_name", "Default Value")
                    ctype = column.get("column_type", "Default Value")

                    txt_file.write(f"column_name : {cname}\n")
                    txt_file.write(f"column_type : {ctype}\n")

import json
input_path = r"C:\Users\sakthep\Downloads\datasource_metadata.json"
with open(input_path, 'r') as file:
    content = json.load(file)

datasources = content.get("datasources",[])
output_file_path = r"C:\Users\sakthep\OneDrive - Capgemini\Desktop\sample2.txt"

with open(output_file_path, 'w') as txt_file:
    for datasource in datasources:
        tables = datasource.get("tables", [])
        for table in tables:
            columns = table.get("columns", [])
            for column in columns:
                if column.get("tableau_type") == "date":
                    cname = column.get("column_name", "Default Value")
                    ctype = column.get("column_type", "Default Value")
                    cabel = column.get("lable_name", 'Default Value')
                    crole = column.get("role", "Default Value")
                    ctabtype = column.get("tableau_type", "Default Value")

                    txt_file.write(f"column_name : {cname}\n")
                    txt_file.write(f"column_type : {ctype}\n")
                    txt_file.write(f"label_name : {clabel}\n")
                    txt_file.write(f"role : {crole}\n")
                    txt_file.write(f"tableau_type : {ctabtype}\n")
                    txt_file.write(f"type : {ctype}\n")




