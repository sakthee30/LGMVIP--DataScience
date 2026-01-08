import xml.etree.ElementTree as ET
import json

tree = ET.parse(r"C:\Users\sakthep\Downloads\SingleExceldatasource 1.xml")
root = tree.getroot()

data_sources = {
    "datasources": []
}
for datasource in root.findall('.//datasource'):
    name = datasource.get('name')
    caption = datasource.get('caption')

    # if caption:
    #       split = caption.split(" ",1)
    #       caption = split[0]
    #       caption_split = split[1] if len(split) > 1 else None

    # if caption and "(" in caption and ")" in caption:
    #     split, split_Caption = caption.split("(", 1)
    #     caption = split.strip()
    #     caption_split = split_Caption.strip(")")


    for namedconnection in root.findall('.//named-connection'):
        cname = namedconnection.get('name')
        ccaption = namedconnection.get('caption')
        result = {
            "caption":caption,
            "name":name,
            "connection_name": cname,
            "connection_caption": ccaption
        }
        data_sources["datasources"].append(result)
  
output = {
    'data_sources' : data_sources
}

with open('jsoutput.json','w') as json_file:
    json.dump(output,json_file, indent=4)

# #to fetch remote name from metadata-record where class is column
for metadata in root.findall(".//metadata-record[@class='column']"):
        remote_name = metadata.find("remote-name")
        if remote_name is not None:
                print("Remote Name:", remote_name.text)
        else:
                print("Remote Name: Not found")