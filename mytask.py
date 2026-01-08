#to fetch all country names
import json
with open(r"C:\Users\sakthep\Downloads\file.json",encoding='utf-8') as f:
    data =json.load(f)

country_names = [country.get("name") for country in data if "name" in country]
print(country_names) 

#to fetch all capitals
import json
with open(r"C:\Users\sakthep\Downloads\file.json",encoding='utf-8') as f:
    data = json.load(f)
capital = [country.get("capital") for country in data if "capital" in country]
print(capital)

#to filter countries in europe
import json
with open(r"C:\Users\sakthep\Downloads\file.json", encoding='utf-8') as f:
    data = json.load(f)

europe_country = [country["name"] for country in data if country.get("region") == "Europe"]
print(europe_country)

#Get countries using the Euro
import json
with open(r"C:\Users\sakthep\Downloads\file.json", encoding='utf-8') as f:
    data=json.load(f)

euro_currency = [country["name"] for country in data if country.get('currency') == 'Euro']
print(euro_currency)

#get all capitals and their population
import json
with open(r"C:\Users\sakthep\Downloads\file.json", encoding='utf-8') as f:
    data = json.load(f)

capitals = [country["capital"] for country in data if country.get("capital")]
populations = [country["population"] for country in data if country.get("population")]
print(capitals)
print(populations)

#get region where subregion is europe
europe_region = [country["region"] for country in data if country.get("subregion") == "Western Europe"]
print(europe_region)