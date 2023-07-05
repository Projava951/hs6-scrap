import requests
import json
import csv

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
report_data = []

for commodity_obj in commodity_array:
    period = commodity_obj["T"]
    province = "Alberta"
    for hs6 in hs6_array:
        print(hs6["HS"])
        if str(hs6["HS"]) == str(commodity_obj["H"]):
            commodity = hs6["HS"][0:4] + "." + hs6["HS"][4:2] + " - " + hs6["EN"]
            country = commodity_obj["C"]
            state = commodity_obj["S"]
            value = commodity_obj["V"]
            quantity = commodity_obj["Q"]
            unit = hs6["UOM"]
            main_category = hs6["HS"][0:2]
            hs2 = ""
            sub_category = hs6["HS"][2:2]
            hs4 = ""
            full_hs4 = hs6["HS"][0:4]
            break
        else:
            commodity = ""
            country = ""
            state = ""
            value = ""
            quantity = ""
            unit = ""
            main_category = ""
            hs2 = ""
            sub_category = ""
            hs4 = ""
            full_hs4 = ""
    report_data.append([period, commodity, province, country, state, value, quantity, unit, main_category, hs2, sub_category, hs4, full_hs4])


with open('report.csv', mode='a', newline='') as file:

    writer = csv.writer(file)
    writer.writerows(report_data)