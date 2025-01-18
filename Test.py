#CODED BY SHAJON
#GITHUB SHAJON-404

import requests, json

query = "104.28.208.81"
info = requests.get(f"http://ip-api.com/json/{query}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query").json()
print("-"*56)
print(f"\t\t>>> IP INFORMATION <<<")
print("-"*56)
print(json.dumps(info, indent=4))
print("-"*56)
print("\t\t>>> BY SHAH MAKHDUM SHAJON <<<")
print("-"*56)
