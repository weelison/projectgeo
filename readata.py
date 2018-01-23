import json

data = json.load(open("geo_data.json"))


def get_data(ip):

    if ip in data:
        return data[ip]


ip3 = "100.200. *"

print(get_data(ip3))
