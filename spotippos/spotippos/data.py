# _*_ coding: utf-8 _*_

import json


f_props = open('../properties.json')
_properties = json.load(f_props)
f_props.close()

f_prov = open('../provinces.json')
_provinces = json.load(f_prov)
f_prov.close()
