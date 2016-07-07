# _*_ coding: utf-8 _*_

from spotippos import app
from bottle import request
from spotippos.models.properties import *
from spotippos import data
import json


@app.get('/hello')
def hello():
    return (json.dumps(data._properties))

@app.post('/properties')
def create_propertie():
    dat = request.json
    p = Properties()
    prop = p.add_property(dat)
    return json.dumps(prop)

@app.get('/properties/<id:int>')
def get_propertie_by_id(id):
    p = Properties()
    property = p.get_property_by_id(id)
    return json.dumps(property)

@app.get('/properties')
def search_properties_by_area():
    ax = int(request.query.ax)
    ay = int(request.query.ay)
    bx = int(request.query.bx)
    by = int(request.query.by)
    a = (ax, ay)
    b = (bx, by)
    properties = Properties()
    found = properties.search_prop_in_area(a, b)
    return json.dumps(found)
