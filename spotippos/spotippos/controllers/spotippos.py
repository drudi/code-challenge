# _*_ coding: utf-8 _*_

from spotippos import app
from bottle import request, response
from spotippos.models.properties import *
from spotippos import data
import json


@app.get('/hello')
def hello():
    return (json.dumps(data._properties['totalProperties']))

@app.post('/properties')
def create_propertie():
    dat = request.json
    p = Properties()
    prop = p.add_property(dat)
    resource_url = '/properties/' + str(prop['id'])
    response.status = 201
    response.headers['Content-Type'] = 'application/json'
    response.headers['Location'] = resource_url
    return json.dumps({'id': prop['id'], '_link' : resource_url})

@app.get('/properties/<id:int>')
def get_propertie_by_id(id):
    p = Properties()
    response.headers['Content-Type'] = 'application/json'
    try:
        property = p.get_property_by_id(id)
    except (IndexError):
        response.status = 404
        return json.dumps({'message' : 'Property with id %d not found' % id})
    return json.dumps(property)

@app.get('/properties')
def search_properties_by_area():
    ax = int(request.query.ax)
    ay = int(request.query.ay)
    bx = int(request.query.bx)
    by = int(request.query.by)
    a = (ax, ay)
    b = (bx, by)
    response.headers['Content-Type'] = 'application/json'
    properties = Properties()
    found = properties.search_prop_in_area(a, b)
    return json.dumps(found)
