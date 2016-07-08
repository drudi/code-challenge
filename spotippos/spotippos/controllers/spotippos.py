# _*_ coding: utf-8 _*_

from spotippos import app
from bottle import request, response
from spotippos.models.properties import *
from spotippos import data
from voluptuous import *
import json

post_schema = Schema({
    Required('x'): All(int, Range(min=0, max=1400)),
    Required('y'): All(int, Range(min=0, max=1000)),
    Required('beds'): All(int, Range(min=1, max=5)),
    Required('baths'): All(int, Range(min=1, max=4)),
    Required('squareMeters'): All(int, Range(min=20, max=240)),
    'title': str,
    'price': int,
    'description': str
    })


@app.get('/hello')
def hello():
    return (json.dumps(data._properties['totalProperties']))

@app.post('/properties')
def create_propertie():
    response.headers['Content-Type'] = 'application/json'
    dat = request.json

    # Input validation
    try:
        post_schema(dat)
    except MultipleInvalid as e:
        response.status = 422
        return json.dumps({
            'message' : 'Unprocessable input: {0}'.format(e)
            })

    p = Properties()
    prop = p.add_property(dat)
    resource_url = '/properties/' + str(prop['id'])
    response.status = 201
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
    response.headers['Content-Type'] = 'application/json'

    # Input Validation
    try:
        ax = int(request.query.ax)
        ay = int(request.query.ay)
        bx = int(request.query.bx)
        by = int(request.query.by)
    except ValueError as e:
        response.status = 400
        return json.dumps({'message' : 'Only integers allowed'})

    if not(ax <= bx) or not(by <= ay):
        response.status = 422
        return json.dumps({
            'message' : '(ax, ay) must be the upper Left point and (bx, by) must be the bottom right point'
            })
    elif (not (0 <= ax <= 1400) or not (0 <= bx <= 1400)
            or not (0 <= ay <= 1000) or not (0 <= by <= 1000)):
        response.status = 422
        return json.dumps({
            'message' : 'Invalid search parameters. You are searching properties beyond the limits os Spotippos'
            })

    a = (ax, ay)
    b = (bx, by)
    properties = Properties()
    found = properties.search_prop_in_area(a, b)
    return json.dumps(found)
