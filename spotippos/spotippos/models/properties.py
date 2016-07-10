# _*_ coding: utf-8 _*_
import json
#from spotippos import *
from spotippos import data


class Properties(object):
    '''Define model for properties set'''
    def __init__(self):
        self._properties = data._properties

    def _point_in_area(self, p, upperLeft, bottomRight):
        '''Verify if point p is inside the area defined by upperLeft
            and bottomRight
        '''
        if ((p[0] >= upperLeft[0]) and
            (p[0] <= bottomRight[0]) and
            (p[1] <= upperLeft[1]) and
            (p[1] >= bottomRight[1])):
            return True
        return False

    def add_property(self, prop):
        #prop = prop.__dict__
        nprops = len(self._properties['properties']) + 1
        prop['id'] = nprops
        self._properties['properties'].append(prop)
        self._properties['totalProperties'] += 1
        return prop

    def get_property_by_id(self, id):
        idx = id - 1
        prop = self._properties['properties'][idx]

        # Find and populate provinces
        coord = (prop['x'], prop['y'])
        prop['provinces'] = self.get_provinces(coord)

        return prop

    def search_prop_in_area(self, upperLeft, bottomRight):
        properties_found = []
        for prop in self._properties['properties']:
            p = (prop['x'], prop['y'])
            if self._point_in_area(p, upperLeft, bottomRight):
                properties_found.append(prop)
        resultset = {'foundProperties' : len(properties_found),
                'properties' : properties_found
                }
        return resultset

    def get_provinces(self, p):
        '''Given a point p, find what provinces this point is in'''
        provinces = []
        for prov in data._provinces:
            province = data._provinces[prov]
            upperLeft = (province['boundaries']['upperLeft']['x'],
                        province['boundaries']['upperLeft']['y']
                        )
            bottomRight = (province['boundaries']['bottomRight']['x'],
                        province['boundaries']['bottomRight']['y']
                        )
            if self._point_in_area(p, upperLeft, bottomRight):
                provinces.append(str(prov))
        return provinces


