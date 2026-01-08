import pandas as pd
import openpyxl

data = {
    'Name': ['Sakthee', 'Jai', 'Vani'],
    'Age': [23, 18, 33]
}

def read_fn(output):
    extension = output.split('.')[-1]
    if extension == 'xlsx':
        check = pd.read_excel(output)
    elif extension == 'csv':
        check = pd.read_csv(output)
    elif extension == 'json':
        check = pd.read_json(output)
    print(f"File {output} read successfully, the extension is {extension} and the content is :  {data}")
    return check

def write_fn(data,output):
    content = pd.DataFrame(data)
    extension = output.split('.')[-1]
    if extension == 'xlsx':
        check = content.to_excel(output)
    elif extension == 'csv':
        check = content.to_csv(output)
    elif extension =='json':
        check = content.to_json(output)
    print(f"Data written to {output} successfully")
    

read1 = read_fn("output.json")
write1 = write_fn(data,"output1.json")


# file = "output.xlsx"
# extension = file.split('.')[-1]
# print(extension)
# - Filename, from filename extract the extension
# - Based on the extension, write the corresponding function to read or write to the specific file format