import xml.etree.ElementTree as ET
import json

#function to load xml file
def load_xml(file_path):
    tree = ET.parse(file_path)
    return tree.getroot()

#function to extract data from xml
def extract_datasource_info(root):

    data_sources = { "datasources": [] }

    #to get name and caption from datasource
    for datasource in root.findall('.//datasource'):
        dname = datasource.get('name')
        dcaption = datasource.get('caption')

        #to get name and caption from named-connection
        for namedconnection in root.findall('.//named-connection'):
                       ccaption = namedconnection.get('caption')

            #to get remote name from metadata-record where class is column 
            for metadata in root.findall(".//metadata-record[@class='column']"):
                remote_name = metadata.find("remote-name")
                if remote_name is not None:
                    remote_name_text = remote_name.text
                else:
                    remote_name_text = "Not found"

            result = {
                "caption":dcaption,
                "name":dname,
                "connection_name": cname,
                "connection_caption": ccaption,
                "remote_name": remote_name_text
            }
            data_sources["datasources"].append(result)
    return data_sources

#func to save output data to json
def save_to_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

#to call function
if __name__ == "__main__":
    xml_file_path = r"C:\Users\sakthep\Downloads\SingleExceldatasource 1.xml"
    output_file = 'output.json'

    root = load_xml(xml_file_path)
    data_sources = extract_datasource_info(root)
    save_to_json(data_sources, output_file)


