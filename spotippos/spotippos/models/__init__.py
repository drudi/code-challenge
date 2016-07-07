import json


f_prop = open('../properties.json')
_properties = json.load(f_prop)
f_prop.close()

f_prov = open('../provinces.json')
_provinces = json.load(f_prov)
f_prov.close()
