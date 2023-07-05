import requests
import json

def hs6_scrap():
    url = "https://www150.statcan.gc.ca/n1/pub/71-607-x/2021004/hs6F.js"
    response = requests.get(url, headers=[], data = {})
    data = response.text[10:]
    data_json = json.loads(data)
    return data_json

def commodity_scrap(year = 1988):
    url = "https://www150.statcan.gc.ca//t1/cimt/rest/getReport/(48)/0/0/0/1/150000/1/0/" + str(year) + "-01-01/" + str(year + 1) + "-01-01"
    response = requests.get(url, headers=[], data = {})
    data_json = response.json()
    return data_json

hs6_array = hs6_scrap()
commodity_array = commodity_scrap()["trade"]
print(len(hs6_array))
print(len(commodity_array))