#! /usr/bin/env python
# _*_ coding: utf-8 _*_

import os
import json
from spotippos import app
from bottle import debug, run

debug(True)


if __name__ == '__main__':
    run(app, reloader=True, host='localhost', port=8000)

